print("Calculo de MAXIMO y MINIMO")

print("Introduzca una serie de número ")
print("Para finalizar escriba la palabra fin ")

x = None
mayor = None
menor = None

print("Comenzamos valor actual = ",x)

while x != "fin" :
    x = input("Intruzca un numero : ")
    try:
        if x == "fin" :
            print("Se termino el programa ",x)
            print("El valor Maximo es = ",mayor)
            print("El valor Minimo es = ",menor)
        else :
            y = float(x)
            #print(y)
            if menor is None or  y < menor :
                #menor = mayor
                menor = y
            elif mayor is None or y > mayor :
                mayor = y

    except:
        print("Ingrese un valor valido")
