import csv
from bs4 import BeautifulSoup

point = 2000000
with open('raw_thptqg_2020.txt','r',encoding='utf-8') as file:
	raw_data=(file.readlines())
	
title = ['Số báo danh','tên','ngày sinh']
data_human = []
block = []

for raw in raw_data:
	point+=1
	#un-escape raw data in file -> raw type binary
	soup = BeautifulSoup(eval(raw),"html.parser")
	code = '0'+str(point)
	print(point)
	try:
		#tag td is list 
		name = soup('td')[3].string.strip()
		birthday = soup('td')[4].string.strip()
		mark = soup('td')[5].string.strip()
		#adding row data in block
		block.append(code)
		block.append(name)
		block.append(birthday)
		#split list mark
		listmark = mark.split(":")
		for mark in listmark:
			detail = mark.strip().split("   ")
			for x in detail:
				block.append(x)
		#Check title and if not adding title 
		header = 3
		while header < len(block):
			if block[header] not in title:
				title.append(block[header])
			header+=2
		data_human.append(block.copy())
		block.clear()
	except Exception as e:
		print('Khong ton tai!',e)
#Write data in file csv
with open('kqthi_thptqg_2020.csv','a',encoding='utf-8') as file:
	writer = csv.writer(file,lineterminator='\n')
	writer.writerow(title)
	for block_data in data_human:
		for value in block_data[:3]:
			block.append(value)
		#split mark without list mark(title)
		for value in title[3:]:
			if value in block_data:
				block.append(block_data[block_data.index(value)+1])
			else:
				block.append('-1')
		writer.writerow(block)
		block.clear()