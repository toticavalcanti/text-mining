# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 09:52:24 2017

@author: toti.cavalcanti
"""

# encoding: utf-8
import csv
import string
import operator
import re
from functools import reduce
import nltk
from nltk import word_tokenize

lista = []
#util
with open('C:/Users/toti.cavalcanti/Downloads/Compressed/2014_2016_balanceada.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        if len(row) > 1:
            lista.append(','.join(row).split(";"))
        else:
            lista.append(row[0].split(";"))

#lista de stopwords em português
stopwords = nltk.corpus.stopwords.words('portuguese')
stopwords.append('/')
stopwords.append("-")
stopwords.append("–")
stopwords.append(',')
stopwords.append("(")
stopwords.append(")")

#tupla com dois elementos, uma lista com as palavras de um texto tokenizado e
#o segundo elemento, a sua classificação (lista_de_tuplas)
#exemplo
#(['palavra_1', 'palavra_2',..., 'palavra_n'], '1')
#equivale a um document em vários documents do exemplo NLTK do movie_reviews
#featuresets = [(document_features(d), c) for (d,c) in documents] 
#d é o primeiro elemento da tupla(a lista dentro da tupla) 
#c é o segundo elemento da lista (0 ou 1) lembrando que está em string ('0' ou '1')
lista_de_tuplas = []
todas_palavras = []
for item in lista[1:]:
    lista_aux = []
    item[1] =  word_tokenize(item[1].lower())
    item[1] = [word for word in item[1] if not re.fullmatch('[' + string.punctuation + ']+', word)]
    item[1] = [word for word in item[1] if word not in stopwords]

    #alguns registros tem palavras com a '/' colada na última letra
    #impossibilitando que a '/' não seja retirada pelo processo de stopword
    #por isso o 'for' abaixo
    for p in item[1]:
        if p[-1] == '/':
            item[1][item[1].index(p)] = p.replace('/', ' ')

    lista_aux.append(item[1])
    lista_aux.append(item[2])
    lista_de_tuplas.append(tuple(lista_aux))
    todas_palavras.append(item[1])
  
#reduce faz um flat da lista de lista
todas_palavras = reduce(operator.add, todas_palavras)

#distribuicao_frequencia_todas_palavras
#FreqDist({'palavra': frequência})
distribuicao_frequencia_todas_palavras = nltk.FreqDist(todas_palavras)

#Cada tupla da lista é um registro com sua classificação
#A lista dentro da tupla( primeiro elemento da tupla) é o que tem que 
#ser passado a função document_features( )

word_features = list(distribuicao_frequencia_todas_palavras)[:2000]

def document_features(document):
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains({})'.format(word)] = (word in document_words)
    return features

featuresets = [(document_features(d), c) for (d,c) in lista_de_tuplas]
train_set, test_set = featuresets[11789:], featuresets[:11789]
classifier = nltk.NaiveBayesClassifier.train(train_set)
nltk.classify.accuracy(classifier, train_set)

classifier.show_most_informative_features(5)



