# coding=utf-8
# scrypt created by Lukman-xd

# IMPORT MODULE-
import requests, os, sys, random, json, re, concurrent, time, shutil
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from random import randrange as rr
from random import choice as rc
ses = requests.Session()

# WARNA TOOLS-
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI :V

# MULAI MAIN-
class main:
	def __init__(self):
		self.loop = 1
		self.menu()
		
	# LOGO
	def loogo(self):
		try:os.system("clear")
		except:pass
		print(f'''
[{O}•{N}] Author  : {H}Lukman-xd{N}
[{O}•{N}] Github  : {H}Private{N}
[{O}•{N}] Whatsap : {H}6283878903922 {N}''')

	# LOGIN COOKIE-
	def login_cookie(self):
		self.loogo()
		cookie = input(f'\n[{O}?{N}] Cookies : ')
		try:
			ses.headers.update({"Accept-Language": "id,en;q=0.9","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36","Referer": "https://www.instagram.com/","Host": "www.facebook.com","Sec-Fetch-Mode": "cors","Accept": "*/*","Connection": "keep-alive","Sec-Fetch-Site": "cross-site","Sec-Fetch-Dest": "empty","Origin": "https://www.instagram.com","Accept-Encoding": "gzip, deflate"})
			link = ses.get("https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/", cookies={"cookie": cookie})
			if '"access_token":' in str(link.headers):
				token = re.search('"access_token":"(.*?)"', str(link.headers)).group(1)
				open('cookie.txt','w').write(cookie);open('token.txt','w').write(token)
				exit(f'\n[{H}+{N}] Login menggunakan cookie berhasil')
			else:exit()
		except Exception as e:
			exit(f'\n[{M}!{N}] Login menggunakan cookie gagal!')
	
	# MENU DUMP-
	def menu(self):
		try:self.cookie = open('cookie.txt','r').read();self.token = open('token.txt','r').read()
		except:self.login_cookie()
		self.loogo()
		try:
			link = ses.get(f"https://graph.facebook.com/v18.0/me?fields=id,name&access_token={self.token}", cookies={"cookie": self.cookie}).json()
			uid, name = link["id"], link["name"]
		except:
			os.system('rm -f cookie.txt')
			exit(f'\n[{M}!{N}] Cookie akun tumbal kamu kadaluarsa')
		print(f'''
[{O}*{N}] Name : {name}{N}
[{O}*{N}] Uid  : {uid}{N}

	[{H}1{N}] Dump dari teman publik
	[{H}2{N}] Dump dari teman massal
	[{H}3{N}] Dump dari total pengikut
					''')
		menu = input(f'[{O}?{N}] Pilih : ')
		if menu in[""," "]:self.menu()
		elif menu in["1","01"]:
			user_id=1
			print(f'\n[{O}*{N}] Masukan nama file contoh : dump.txt')
			name_file = input(f'[{O}?{N}] Masukan nama file : ')
			if name_file in[""," "]:self.menu()
			elif ".txt" not in name_file:self.menu()
			else:file = name_file.replace(' ','_')
			uid = input(f'[{O}?{N}] Masukan uid : ')
			if uid in[""," "]:self.menu()
			else:
				try:
					link = ses.get(f"https://graph.facebook.com/{uid}?fields=friends&access_token={self.token}", cookies={"cookie": self.cookie}).json()
					for z in link['friends']['data']:
						try:
							open('/sdcard/'+file,'a').write(z["id"]+'|'+z["name"]+'\n')
							print(f'\r[{O}*{N}] sedang mengumpulkan {H}{user_id} {N}uid...', end='');sys.stdout.flush()
							user_id+=1
						except:pass
				except Exception as e:
					exit(f'[{M}!{N}] Maaf dump id target gagal')
		elif menu in["2","02"]:
			outfit=[]
			print(f'\n[{O}*{N}] Masukan nama file contoh : dump.txt')
			name_file = input(f'[{O}?{N}] Masukan nama file : ')
			if name_file in[""," "]:self.menu()
			elif ".txt" not in name_file:self.menu()
			else:file = name_file.replace(' ','_')
			try:jum = input(f'[{O}?{N}] Masukan jumlah target : ')
			except ValueError:jum = 1
			jum_target = int(jum);no=0
			for z in range(jum_target):
				no+=1
				uid = input(f'[{H}{no}{N}] Masukan uid : ')
				outfit.append(uid)
			for xd in outfit:
				try:
					user = self.convert(uid)
					self.dump_teman(user, file)
				except:pass
			try:hasil = open('/sdcard/'+file,'r').read()
			except:exit(f'[{M}!{N}] Maaf dump id target gagal')
			if hasil == 0:
				exit(f'[{M}!{N}] Maaf dump id target gagal')
			else:pass
		elif menu in["3","03"]:
			print(f'\n[{O}*{N}] Masukan nama file contoh : dump.txt')
			name_file = input(f'[{O}?{N}] Masukan nama file : ')
			if name_file in[""," "]:self.menu()
			elif ".txt" not in name_file:self.menu()
			else:file = name_file.replace(' ','_')
			
		return self.simpan(file)
				
	def simpan(self, file):
		exit(f'\n[{O}*{N}] Berhasil menyimpan file uid ke /sdcard/{file}')

main()
