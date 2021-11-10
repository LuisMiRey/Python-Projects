print("Programa de reconocimiento de archivos\n")
''' #Contador de lineas
file = open('mboxshort.txt')
contador=0
for lines in file :
    contador = contador + 1
print("Lineas en el archivo = ",contador)   '''

''' #Llamar archivo
narchivo = input('Ingresa un nombre de archivo: ')
try:
    man_a = open(narchivo)
except:
    print('No se puede abrir el archivo:', narchivo)
    exit()
contador = 0
for linea in man_a:
    if linea.startswith('Subject:'):
        contador = contador + 1
print('Hay', contador, 'líneas de asunto (subject) en', narchivo)
'''
'''
fsal = open('salida.txt', 'w')
print(fsal)
linea1 = "Aquí esta el zarzo,\n"
fsal.write(linea1)
linea2 = "\n123\nAqui esta la cuarta parte\n"
fsal.write(linea2)
'''
fsal = open('mboxshort.txt')
for lines in fsal:
    lx = lines.rstrip()
    print(lx.upper())
