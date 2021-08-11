#from autologin import AutoLogin
import requests
from lxml import html
import re

url = "https://www.thegioiic.com/login"
#190221
#21703
session_requests = requests.session()
login_url = url
result = session_requests.get(login_url)
tree = html.fromstring(result.text)
f = open("out/tg.html", "w", encoding='utf8')
f.write(result.text)
f.close()
#print(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='_token']/@value")))[0]
tongcong = 0

payload = {
	"email":"bigb***@gmail.com",
	"password":"***",
	"_token":authenticity_token
}
result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
)
print(result)
tree = html.fromstring(result.content)
bucket_names = tree.xpath("//div[@class='a']/a/text()")

#print(bucket_names)


url = 'https://www.thegioiic.com/users/4310'
result = session_requests.get(
	url, 
	headers = dict(referer = url)
)

f = open("out/rs.html", "w", encoding='utf8')
f.write(result.text)
f.close()

#orderUrl = "https://www.thegioiic.com/orders/180456"
orderUrl = "https://www.thegioiic.com/orders/"


url = orderUrl + str(180452)
print(url)
result = session_requests.get(
	url, 
	headers = dict(referer = url)
)

doc = html.fromstring(result.content)

nott = doc.xpath('//div[@id="wrapper"]')[0]

nott2 = nott.xpath('.//div[@class="container-fluid"]')[0]
nott3 = nott2.xpath('.//div[@class="mt-2"]')[0]
nott4 = doc.xpath('.//h2[@class="text-danger text-center"]')[0]
detectError = str(nott4.text_content())


while True:
	print("Start scraping")
	for i in range(180400,180500):
		
		url = orderUrl + str(i)
		print(url)
		result = session_requests.get(
			url, 
			headers = dict(referer = url)
		)

		doc = html.fromstring(result.content)
		
		try:
			nott4 = doc.xpath('.//h2[@class="text-danger text-center"]')[0]
			getError = str(nott4.text_content())
			getError = getError.strip()
			#if detectError == detectError:
			#error hia:
			print (getError)
			continue
		except:
			#print("No found receipts")
			
			pass
		
		#//div[@class="head"][@id="top"]

		#nott4 = doc.xpath('//div[@class="mt-1"]/b[@class="leftInfoText"]')
		listl = []

		mdh = doc.xpath('//b[@class = "text-gray mr-1"]/text()')[0]
		ttmdh = doc.xpath('//b[@class = "text-success text-small"]/span/text()')[0]

	
		listl.append({mdh:ttmdh})
		nott4 = doc.xpath('//div[@class="mt-1"]')

		for nott44 in nott4:
			try:
				temp1 = nott44.xpath('.//b[@class="leftInfoText"]/text()')[0].strip()
				temp2 = nott44.xpath('.//span[@class="rightInfoText"]/text()')[0].strip()
				listl.append({temp1:temp2})
				#print (temp1)
				#print(temp2)
			except:
				ee = nott44.text_content().strip()
				listl.append({"Khác":ee})
		#print(listl)

		try:
			#tr = doc.xpath('//table[@class = "table-list mt-1"]/tr/th/text()')
			#for trc in tr:
			#	print((trc))
			#print("there table")

			tb = []
			tr = doc.xpath('//table[@class = "table-list mt-1"]/tr')

			for i in range(1,len(tr)-1):
				#print(i)
			
				if (len(tr[i]) == 5):
					
					tdd = tr[i].xpath('.//td')
					# print(tdd[0].xpath('.//text()')[0])
					stt = tdd[0].xpath('.//text()')[0]
					# print(tdd[1].xpath('.//a/text()')[0].strip())
					nome = tdd[1].xpath('.//a/text()')[0].strip()
					# print(tdd[1].xpath('.//@href')[0])
					link = tdd[1].xpath('.//@href')[0]
					# print(" ".join(((tdd[2].xpath('.//text()')[0]).strip()).split()))
					quan = " ".join(((tdd[2].xpath('.//text()')[0]).strip()).split())
					# print(tdd[3].xpath('.//text()')[0].strip())
					price = tdd[3].xpath('.//text()')[0].strip()
					# print(tdd[4].xpath('.//text()')[0].strip())
					cost = tdd[4].xpath('.//text()')[0].strip()
					tb.append({'Order':stt})
					tb.append({'Name':nome})
					tb.append({'Link':link})
					tb.append({'Quant':quan})
					tb.append({'Price':price})
					tb.append({'Cost':cost})
					
					pass
				else:
					try:
						tde = tr[i].xpath('.//td/text()')[0].strip()
						
						tdf = tr[i].xpath('.//td/text()')[1].strip()
						#print(tde,tdf)
						tb.append({tde:tdf})
					except IndexError  as e:
						print(e)
						pass
			tt1 = tr[len(tr) - 1].xpath('.//td[@class = "text-danger text-right"]/text()')[0].strip()
			tt2 = tr[len(tr) - 1].xpath('.//td[@class = "text-danger text-right"]/text()')[1].strip()
			#print(tt1,tt2)
			tb.append({tt1:tt2})
			lala = tt2[:len(tt2)-1]
			print(lala)
			lala = lala.replace(".", "")
			lala=float(lala)
			tongcong+=lala
			
			
			# for i in range(len(tr)):
			# 	if (i >= 1) and (i < (len(tr))):

			# 		try:
			# 			tdcoln = tr[i].xpath('.//td[@colspan="4" and @style="text-align:right;"]')
			# 			print(len(tdcoln))
			# 			#tdcols = tr[i].xpath('.//td[@colspan="4"]')
			# 			#for tt in range(len(tdcoln)):
			# 				#print(tdcoln[tt].xpath('.//text()')[0])
			# 				#print(tdcols[i].xpath('.//text()'))
			# 		except:
			# 			pass
			# 		try:
			# 			tdd = tr[i].xpath('.//td')
			# 			print(tdd[0].xpath('.//text()')[0])
			# 			print(tdd[1].xpath('.//a/text()')[0].strip())
			# 			print(tdd[1].xpath('.//@href')[0])
						
			# 			print(" ".join(((tdd[2].xpath('.//text()')[0]).strip()).split()))
						
			# 			print(tdd[3].xpath('.//text()')[0].strip())
			# 			print(tdd[4].xpath('.//text()')[0].strip())
			# 		except:
			# 			pass
					
					
				#elif i == (len(tr) - 1):
					#process tổng tiền
					#pass
		except IndexError  as e:
			print(e)
		#print(listl)
		#print(tb)
		#print(tongcong)
		#for k in listl:
		#	print(k)
		# sttt = str(nott4.text_content())
		# if sttt.find("Ngày đặt"):
		# 	nott5 = doc.xpath('//div[@class="mt-1"]/span[@class="rightInfoText"]')
		# 	print(str(nott5.text_content()))
		
		#print(str(nott4.text_content()))
	print(tongcong)
	exit()
		
		
		

#username = 'https://www.thegioiic.com/login'
#password = 'runtoyou'
#al = AutoLogin()
#cookies = al.auth_cookies_from_url(url, username, password)