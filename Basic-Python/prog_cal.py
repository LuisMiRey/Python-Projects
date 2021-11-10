print("Programa de calificaciónes ")

nun = input("Ingrese la puntuacion entre 0.0 y 1.0  ",)
try :
    num= float(nun)
    if 0.9 <= num <= 1.0 :
        print("\nSobresaliente")
    elif  0.8 < num < 0.9 :
        print("\nNotable")
    elif 0.7 < num <= 0.8 :
        print("\nBien")
    elif 0.6 < num <= 0.7 :
        print("\nSuficiente")
    elif num < 0.6 :
        print("\nInsuficiente")
except :
        print("\nIntroduce un numero")
