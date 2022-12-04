# This Python file uses the following encoding: utf-8
import requests


class colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'

def banner():
    print(colors.GREEN+'''
   _____                      __    ____  _     
  / ___/___  ____ ___________/ /_  / __ \(_)____
  \__ \/ _ \/ __ `/ ___/ ___/ __ \/ / / / / ___/
 ___/ /  __/ /_/ / /  / /__/ / / / /_/ / / /    
/____/\___/\__,_/_/   \___/_/ /_/_____/_/_/     
                                                                                                                                                                                                                                                                   
''')

def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass
    except requests.exceptions.MissingSchema:
        quit()
    except KeyboardInterrupt:
    	quit()

banner()

print("Exemplo: https://www.google.com/\n")

targetURL = input("Digite a URL: ")
file = open("simple_wordlist.txt", "r")
for line in file:
    line = line.strip('\n')
    fullURL = targetURL + line
    response = request(fullURL)
    if response:
        print ('[+] Diretório encontrado: ' + fullURL)

