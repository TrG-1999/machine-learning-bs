import urllib.request as urlib
import urllib.parse as urlparse
from bs4 import BeautifulSoup

startpoint = 2000000
endpoint = 2074718

url = "http://diemthi.hcm.edu.vn/Home/Show"
raw_data = []
block = []
while startpoint < endpoint:
	startpoint+=1
	code = '0'+str(startpoint)
	data = urlparse.urlencode({"SoBaoDanh":code})
	data = data.encode('ascii')
	#get date from server /HTTP method POST/
	html = urlib.urlopen(url, data).read()
	raw_data.append(str(html)+'\n')
	print(code)
with open('raw_thptqg_2020.txt','a',encoding='utf-8') as file:
	file.writelines(raw_data)
