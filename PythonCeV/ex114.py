import urllib.request

try:
    urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mNão está acessivel :( \033[m')
else:
    print('\033[32mEstá acessivel!\033[m')