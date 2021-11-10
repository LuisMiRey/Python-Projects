#Ejemplo de extracciond e datos de un XML
import xml.etree.ElementTree as ET

#datos =
''''
<cosa>
<usuarios>
<usuario x="2">
<id>001</id>
<nombre>Chuck</nombre>
</usuario>
<usuario x="7">
<id>009</id>
<nombre>Brent</nombre>
</usuario>
</usuarios>
</cosa>    ''

cosa = ET.fromstring(datos)
lst = cosa.findall('usuarios/usuario')
print('Total de usuarios:', len(lst))
for item in lst:
    print('Nombre', item.find('nombre').text)
    print('Id', item.find('id').text)
    print('Atributo', item.get('x'))

'''
file = input('Nombre o URL del archivo : ')
try :
    datos = open(file)
except :
    print('Ingresa un nombre o URL valida')
    exit()



comments = ET.fromstring(datos)
lst = comments.finall('count/count')
print('Total de coincidencia', len(lst))
for item in ist:
    print('item')

print('Fin del programa')
