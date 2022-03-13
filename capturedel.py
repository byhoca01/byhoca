import time
import os,sys,ctypes
import linecache
import random,string
try:
    from colorama import Fore
except Exception:
    isletim = os.name
    if isletim=="nt":
        os.system('pip install colorama')
    else:
        os.system('pip3 install colorama')
from colorama import Fore
bannerst = """
██████╗ ██╗      █████╗  ██████╗██╗  ██╗███████╗████████╗ ██████╗ ███╗   ██╗███████╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝██╔════╝╚══██╔══╝██╔═══██╗████╗  ██║██╔════╝
██████╔╝██║     ███████║██║     █████╔╝ ███████╗   ██║   ██║   ██║██╔██╗ ██║█████╗  
██╔══██╗██║     ██╔══██║██║     ██╔═██╗ ╚════██║   ██║   ██║   ██║██║╚██╗██║██╔══╝  
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗███████║   ██║   ╚██████╔╝██║ ╚████║███████╗
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝
"""
def slowprints(s):
   for c in s + '\n':
       sys.stdout.write(c)
       sys.stdout.flush()
       time.sleep(1./99)
isletim = os.name
if isletim=="nt":
    def clear():
        os.system('cls')
else:
    def clear():
        os.system('clear')
clear()
print(Fore.BLUE+bannerst)
toplamhesap = 0
islem = 0
valid = 0
invalid = 0
slowprints('')
slowprints(Fore.CYAN+'-------------------------')
slowprints(Fore.CYAN+'[+] Made by BlackStone')
slowprints(Fore.CYAN+'[+] Capture Silici')
slowprints(Fore.CYAN+'-------------------------')
slowprints('')
comboyer = input("Lütfen Capture Silinecek Combolistin Ismini Giriniz : ")
try:
    f = open(comboyer)
    for x in f:
        toplamhesap = toplamhesap + 1
except IOError:
    print(f"{Fore.RED}Combolist Bulunamadı!{Fore.RESET}")
    exit()
slowprints(f"{Fore.BLUE}Combolistte bulunan tahmini hesap sayısı : {Fore.WHITE}{toplamhesap}")
clear()
print(Fore.BLUE+bannerst+Fore.RESET)
letters = string.ascii_lowercase
randomtext = "".join( [random.choice(letters) for i in range(10)] )
dosya = open(f'capturesiz_{randomtext}.txt', 'a+')
while islem<toplamhesap:
    islem = islem + 1
    hesapp = linecache.getline(comboyer, islem)
    hesap = hesapp[:-1].split(":")
    if os.name=="nt":
        ctypes.windll.kernel32.SetConsoleTitleW(f"Capture Silici by BlackStone  |  Hesap: {islem}/{toplamhesap}  |  Geçerli: {valid}  |  Geçersiz: {invalid}")
    try:
        if hesap[1]:
            mail = hesap[0]
            hesappas = hesap[1].split(" ")
            password = hesappas[0]
            dosya.write(mail+":"+password+"\n")
            valid = valid+1
            print(f"{Fore.CYAN}> Hesap --{Fore.RESET}> {mail}:{password} | {Fore.GREEN} Geçerli{Fore.RESET}")
    except IndexError:
        print(f"{Fore.CYAN}> Hesap --{Fore.RESET}> {mail} | {Fore.RED} Geçersiz Hesap Türü{Fore.RESET}")
        invalid = invalid + 1
slowprints('')
slowprints(Fore.CYAN+'-------------------------------------------------')
slowprints(Fore.CYAN+'[+]          ~ Made by BlackStone ~')
slowprints(Fore.CYAN+'[+]   ~ W7rthy & L4ncelot & Diablo & Yoseff ~')
slowprints(Fore.CYAN+'-------------------------------------------------')
slowprints('')
print(f"""{Fore.CYAN}> Sonuç --{Fore.RESET}> {Fore.BLUE}Kontrol Edilen Toplam Hesap : {Fore.WHITE}{toplamhesap}
{Fore.CYAN}> Sonuç --{Fore.RESET}> {Fore.BLUE}Kontrol Edilen Toplam Geçersiz Hesap : {Fore.WHITE}{invalid}
{Fore.CYAN}> Sonuç --{Fore.RESET}> {Fore.BLUE}Kontrol Edilen Toplam Geçerli Hesap : {Fore.WHITE}{valid}
""")