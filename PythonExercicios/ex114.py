import urllib
import urllib.request
import urllib.error

try:
    site = urllib.request.urlopen("https://www.youtube.com/")
except urllib.error.URLError:
    print("O site Pudim NÃO está acessível no momento.")
else:
    print("Consegui acessar o site com sucesso!")
