#from autologin import AutoLogin
import requests
from lxml import html
import re

url = "https://www.thegioiic.com/login"

session_requests = requests.session()
login_url = url
result = session_requests.get(login_url)
tree = html.fromstring(result.text)
f = open("out/tg.html", "w", encoding='utf8')
f.write(result.text)
f.close()
#print(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='_token']/@value")))[0]


payload = {
    "email":"bigboy.061293@gmail.com",
    "password":"runtoyou",
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
		#print(url)
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
				#pass
		except:
			#print("No found receipts")
			pass
		
		try:
			tittle = doc.xpath('.//div[@class="text-medium text-gray"]')
		
			for suba in tittle:
				
				try:
					mdh = suba.xpath('.//b[@class="text-gray mr-1"]/text()')[0]
					mdh = mdh.strip()
					
				except:
					pass
					
				try:
					ngaydat = suba.xpath('.//b[@class="text-success text-small"]')[0]
					ngaydat = str(ngaydat.text_content())
					ngaydat = ngaydat.strip()
					ngaydat = " ".join(ngaydat.split())
					ngaydat = ngaydat[2:len(ngaydat) - 2]
					
				except:
					pass

				try:
					tete = suba.xpath('//div[(@class="mt-1" and contains(.//b[contains(@class, "leftInfoText")])]')
					print(tete)
				except:
					print("hihi")
				#try:

			print(mdh)		
			print(ngaydat)	
		except:
			pass

		#print(str(nott4.text_content()))
		outfile = "out/" + str(i) + ".html"
		f = open(outfile, "w", encoding='utf8')
		f.write(result.text)
		f.close()
		if i == 180499:
			exit()

#username = 'https://www.thegioiic.com/login'
#password = 'runtoyou'
#al = AutoLogin()
#cookies = al.auth_cookies_from_url(url, username, password)