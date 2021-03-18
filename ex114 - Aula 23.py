import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')

except urllib.error.URLError:
    print('Deu ruim!')
else:
    print('Deu bom!')
