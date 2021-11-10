print("Calculo salarial")

horas = input("Intruzca las horas =  ")
tarifa = input("Introduzca la tarifa = ")
try:

    def calculo_salario(hora,tarif) :
        if float(hora) <= 40 :
            res = float(hora) * float(tarif)
            return res
            #print("Salario = ",res)
        else :
            ext = float(hora) - 40
            res = (40 * float(tarif)) + (float(ext) *(1.5 * float(tarif)) )
            return res
            #print("Salario = ",res)

    x = calculo_salario(horas,tarifa)
    print("Salario = ",x)

except:
    print("Intruduzca un numero")
