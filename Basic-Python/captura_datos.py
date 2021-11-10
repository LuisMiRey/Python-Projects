print("Captura de datos")

print("Introduzca una serie de número ")
print("Para finalizar escriba la palabra fin ")

x = None
total = 0
contar = 0
average = 0
print("Comenzamos valor actual = ",x)

while x != "fin" :
    x = input("Introduzca cualquier numero : ")
    try:
        if x == "fin":
            print(x)
            average = total/contar
            print("El total es = ",total)
            print("El numero de objetos es = ",contar)
            print("El promedio es = ",average)

        else :
            y = float(x)
            contar = contar + 1
            total = total + y
            print("El numero es = ",y)
    except:
        print("Introduzca un valor valido ")

print("Fin del programa")
