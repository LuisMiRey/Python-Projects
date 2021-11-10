print("Calculo salarial")

hrs = input("Introduzca las horas: ")
tas = input("Introduzca las tarifa por hora: ")
try :
    if float(hrs) <= 40 :
        res = float(hrs) * float(tas)
        print("Salario = ",res)
    else :
        ext = float(hrs) - 40
        #res = float(ext)
        res = (40 * float(tas)) + (float(ext) *(1.5 * float(tas)) )
        print("Salario = ",res)
    #print("Fin del programa")
except :
    print("introduzca un numero")
