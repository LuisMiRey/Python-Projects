print("Programa para abrir archivos\n")
name = input("Escribe el nombre del archivo:  ")
try:
        if name == "un huevo":
            print("Te cache a ti bobo :D")
            exit()

        elif open(name) :
            file = open(name)
            print(file)

except:
    print("No se puede abrir el archivo\nIntente con un nombre valido")
    exit()

contador = 0
num = 0
sum = 0
for lines in file:
    if lines.startswith('X-DSPAM-Confidence:'):
        first_p = lines.find(':')
        second_p = lines[first_p+1:]
        #print(second_p)
        num = float(second_p)
        contador = contador + 1
        sum = sum + num

average = sum/contador
print("sta fue la suma total = ",sum)
print("numero de datos = ",contador)
print("El resultado es = ",average)
