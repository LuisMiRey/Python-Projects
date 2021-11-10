print("Calificaciones")

cal = input("Introduzca la calificacion de 0.0 a 1.0 :  ")

try:
    def calcula_calificacion(num):
        if 0.9 <= float(num) <= 1.0 :
            print("Sobresaliente")
        elif  0.8 < float(num) < 0.9 :
            print("Notable")
        elif 0.7 < float(num) <= 0.8 :
            print("Bien")
        elif 0.6 < float(num) <= 0.7 :
            print("Suficiente")
        elif float(num) < 0.6 :
            print("Insuficiente")

    calcula_calificacion(cal)

except:
    print("Introduzca un numero ")
