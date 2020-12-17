import urllib.request as urlib
import urllib.parse as urlparse
from bs4 import BeautifulSoup
import csv
import time

# startpoint = 2000000
# endpoint = 2074718
url = "http://diemthi.hcm.edu.vn/Home/Show"
data_human = []
block = []
title = ['Số báo danh','tên','ngày sinh']
while startpoint < endpoint:
	startpoint+=1
	code = '0'+str(startpoint)
	data = urlparse.urlencode({"SoBaoDanh":code})
	data = data.encode('ascii')
	html = urlib.urlopen(url, data).read()
	soup = BeautifulSoup(html,"html.parser")
	#delay time avoid Dos
	time.sleep(1)
	print(code)
	try:
		#tag td is list 
		name = soup('td')[3].string.strip()
		birthday = soup('td')[4].string.strip()
		mark = soup('td')[5].string.strip()
		#adding row data in block
		block.append(code)
		block.append(name)
		block.append(birthday)
		listmark = mark.split(":")
		for mark in listmark:
			detail = mark.strip().split("   ")
			for x in detail:
				block.append(x)
		header = 3
		while header < len(block):
			if block[header] not in title:
				title.append(block[header])
			header+=2
		data_human.append(block.copy())
		block.clear()
	except Exception as e:
		print('Khong ton tai!',e)

with open('kqthi_thptqg_2020.csv','a',encoding='utf-8') as file:
	writer = csv.writer(file,lineterminator='\n')
	writer.writerow(title)
	for block_data in data_human:
		for value in block_data[:3]:
			block.append(value)
		for value in title[3:]:
			if value in block_data:
				block.append(block_data[block_data.index(value)+1])
			else:
				block.append('-1')
		writer.writerow(block)
		block.clear()