# encoding: utf-8
import csv

lista = []
#Ler o arquivo CSV com todos os 592895 com seus 19 campos e armazena em lista
with open('C:/path/do/arquivo/2014_2015_2016.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        if len(row) > 1:
            lista.append(','.join(row).split(";"))
        else:
            lista.append(row[0].split(";"))

with open("C:/path/do/arquivo/2014_2016_dois_campos.csv", 'a') as outcsv:
    #configura a escrita para standard csv file
    writer = csv.writer(outcsv, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    for item in lista:
        #Escreve em 2014_2016_dois_campos.csv apenas os campos 9 (área) e 12 (Problema)
        writer.writerow([item[9], item[12]])
