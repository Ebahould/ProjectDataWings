
import json
import csv
from flatten_json import flatten
from amadeus import Client, ResponseError

class Apiutility:
    #FileTarget = 'data.csv'
    def WriteInCsvFile(self,json_flatten_data, firstRow, fileTarget):
        file =open(fileTarget,"a",newline ='')
        all_keys = []
        for element in json_flatten_data:
            all_keys.append(element)
        writter = csv.DictWriter(file,all_keys)
        '''Si c'est la première ligne => Ajoute l'en-tête'''
        if firstRow :
            writter.writeheader()

        writter.writerow(json_flatten_data)
        file.close()

    #Fichier texte
    def WriteIntextFile(self,flights,Nomdufichier, mode='w'):
        f = open(Nomdufichier,mode)
        f.write(flights)
        f.close()

