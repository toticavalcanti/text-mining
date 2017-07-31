# encoding: utf-8
import csv
import random

lista = []

with open('C:/path/para/o/arquivo/2014_2016_coluna_classificacao.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
        if len(row) > 1:
            lista.append(','.join(row).split(";"))
        else:
            lista.append(row[0].split(";"))

areas = {'Telecomunicações': [], 'Produtos de Telefonia e Informática': [], 'Educação': [], 'Demais Serviços ': [],
         'Demais Produtos': [], 'Água, Energia, Gás': [],
         'Alimentos': [], 'Transportes': [], 'Produtos Eletrodomésticos e Eletrônicos': [],
         'Turismo/Viagens': [], 'Saúde': [], 'Serviços Financeiros': []}

for item in lista[1:]:
    if item[0] == 'Habitação':
        areas['Demais Produtos'].append(item)
    elif item[2] == '0' and item[0] != 'Área' and len(areas[item[0]]) < 2000:
        areas[item[0]].append(item)
    elif len(areas['Telecomunicações']) < 20000:
        areas['Telecomunicações'].append(item)

listaBalanceada = []
for valor in areas.values():
    for item in valor:
        listaBalanceada.append(item)
random.shuffle(listaBalanceada)

with open("C:/path/para/o/arquivo/2014_2016_balanceada.csv", 'a') as outcsv:
    #configure writer to write standard csv file
    writer = csv.writer(outcsv, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow(('Área', 'Descrição do problema', 'Classificação'))
    for each_list in listaBalanceada:
        writer.writerow(each_list)
