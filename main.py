import whois
import json
import requests
import re

print("+-----------------------------------------------------+")

print("| 		 Developed by : vishal                |")

print("|   instagram : https://instagram.com/mr__nobody__23  |")

print("+-----------------------------------------------------+")
regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
 
def check_ip(ip):
	if(re.search(regex, ip)):
		print(f"[✓] Valid IP address.")
	else:
		print(f"[X] Invalid IP address.")
		quit()

ip = input("[+] Enter Public IP : ")

check_ip(ip)

try:

	url = "http://ip-api.com/json/"
	response = requests.get(url+ip)
	data = response.json()
except:
	print("[-] you are offline")
	quit()

print("")
print("[*] I P - I N F O R M A T I O N ")
print("-"*35)
if data['status'] == 'fail':
	print(f"[-] cannot retrive information for private ip {ip}. ")
	quit()
	
else:
	
	print(f"IP        :  {data['query']}")
	print(f"Status    :  {data['status']}")
	print(f"Country   :  {data['country']}")
	print(f"City      :  {data['city']}")
	print(f"Region    :  {data['region']}")
	print(f"Zip Code  :  {data['zip']}")
	print(f"Time Zone :  {data['timezone']}")
	print(f"ISP       :  {data['isp']}")
	print(f"ORG       :  {data['org']}")
	print(f"AS        :  {data['as']}")
	print(f"latitude  :  {data['lat']}")
	print(f"longitude :  {data['lon']}")
	print(f"location  :  {data['lat']},{data['lon']}")
	print('\n')


print("[*] I S P  -  E M A I L S  -  F R O M  -  I P ")
print("-"*50)
import whois
w = whois.whois(ip)
emails = w['emails']
count = 0
for mails in emails:
	count+=1
	print(f"[{count}] : {mails}")
	
