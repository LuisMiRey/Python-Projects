import urllib.request, urllib.parse, urllib.error
img = urllib.request.urlopen('https://www.eltiempo.com/files/image_640_428/uploads/2019/04/11/5caf71d8f2fa7.jpeg')
man_a = open('gt2.jpeg', 'wb')
tamano = 0
while True:
    info = img.read(100000)
    if len(info) < 1: break
    tamano = tamano + len(info)
    man_a.write(info)
    if tamano > 5000:
        print("Llegamos a los 3000 caracteres ")

print(tamano, 'caracteres copiados.')
man_a.close()
