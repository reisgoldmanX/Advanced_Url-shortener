import pyshorteners
import pyperclip
from colorama import init, Fore, Style
init(convert=True)
s = pyshorteners.Shortener()
cp = pyperclip.copy
# Prints Logo and options.
print(Fore.RED + '''                           
\t________________       ______     __     ______    
\t   Option list  |     /      \  _/  |   /      \                      
\t________________|    /$$$$$$  |/ $$ |  /$$$$$$  |            
\t[1] Chilp.it    |    $$ ___$$ |$$$$ |  $$ ___$$ |
\t[2] Qps.ru      |     /   $$<   $$ |    /   $$< 
\t[3] TinyURl.com |     _$$$$$  |  $$ |   _$$$$$  |
\t[4] Da.gd       |    /  \__$$ | _$$ |_ /  \__$$ |
\t[5] Os.db       |    $$    $$/ / $$   |$$    $$/
\t[6] Is.gd       |     $$$$$$/  $$$$$$/  $$$$$$/
\t----------------
''')
print(Style.RESET_ALL + Style.BRIGHT + Fore.YELLOW + "\t\t\t\t\t\tAdvanced Link Shortener")
print(Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + "\t\t\t\t\t\t----------------------")
print(Style.RESET_ALL + Style.BRIGHT + Fore.LIGHTRED_EX + "\t\t\t\t\t\tCoded By: ReisgoldmanX")
print(Fore.YELLOW + "Chose a shortener API.!\n")
# User input for option.
option = input("\t")
print(Fore.YELLOW + "Paste link here.\n")
# User input for link.
link = input("\t")
# Sets option results
if option == "1":
    print(Fore.CYAN + s.chilpit.short(link) + "\t<--  Short Url")   # Shortens the link with "Chilp.it" API
    cp((s.chilpit.short(link)))     # Copy's the shortened link to clipboard
    print(Fore.RED + "\tLink copied to clipboard.!")

if option == "2":
    print(Fore.CYAN + s.qpsru.short(link) + "\t<--  Short Url")     # Shortens the link with "Qps.ru" API
    cp(s.qpsru.short(link))     # Copy's the shortened link to clipboard
    print(Fore.RED + "\tLink copied to clipboard.!")

if option == "3":
    print(Fore.CYAN + s.tinyurl.short(link) + "\t<--  Short Url")   # Shortens the link with "TinyURL.com" API
    cp(s.tinyurl.short(link))       # Copy's the shortened link to clipboard
    print(Fore.RED + "\tLink copied to clipboard.!")

if option == "4":
    print(Fore.CYAN + s.dagd.short(link) + "\t<--  Short Url")      # Shortens the link with "Da.gd" API
    cp(s.dagd.short(link))      # Copy's the shortened link to clipboard
    print(Fore.RED + "\tLink copied to clipboard.!")

if option == "5":
    print(Fore.CYAN + s.osdb.short(link) + "\t<--  Short Url")      # Shortens the link with "Os.db" API
    cp(s.osdb.short(link))      # Copy's the shortened link to clipboard
    print(Fore.RED + "\tLink copied to clipboard.!")

if option == "6":
    print(Fore.CYAN + s.isgd.short(link) + "\t<--  Short Url")      # Shortens the link with "Is.gd" API
    cp(s.isgd.short(link))      # Copy's the shortened link to clipboard
    print(Fore.RED + "\tLink copied to clipboard.!")
