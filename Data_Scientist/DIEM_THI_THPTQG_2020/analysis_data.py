import csv

with open('kqthi_thptqg_2020.csv','r',encoding='utf-8') as file:
	data = [row for row in csv.reader(file,delimiter=',')]