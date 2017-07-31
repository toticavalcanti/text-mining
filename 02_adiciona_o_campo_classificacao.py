# encoding: utf-8
import csv

lista = []
with open('C:/Users/toti.cavalcanti/Downloads/Compressed/2014_2016_dois_campos.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        if len(row) > 1:
            lista.append(','.join(row).split(";"))
        else:
            lista.append(row[0].split(";"))

listaNova = []
#Adiciona o campo Classificação
lista[0].append('Classificação')
for item in lista[1:]:
    if item[0] == 'Telecomunicações':
        item.append(1)
    else:
        item.append(0)
#Escreve o arquivo 2014_2016_coluna_classificacao.csv adicionando a coluna Classificação
with open("C:/Users/toti.cavalcanti/Downloads/Compressed/2014_2016_coluna_classificacao.csv", 'a') as outcsv:
    #configure writer to write standard csv file
    writer = csv.writer(outcsv, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    for item in lista:
        #Write item to outcsv
        writer.writerow([item[0], item[1], item[2]])
