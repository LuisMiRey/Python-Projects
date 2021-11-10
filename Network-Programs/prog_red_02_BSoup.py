import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ct = 0
# Ignorar errores de certificado SSL
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Introduzca - ')
html = urllib.request.urlopen(url, context=ctx).read()
sopa = BeautifulSoup(html, 'html.parser')
# Recuperar todas las etiquetas de anclaje
etiquetas = sopa('p')
for etiqueta in etiquetas:
    print(etiqueta.get('href', None))
    ct= ct + 1

print("El numero de links son = ",ct)
