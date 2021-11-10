print("Obtener el nombre de base de datos de correo\n")

name = input("Introduzca el nombre del archivo: ")

try:
    file = open(name)
    print(file)
except:
    print("Escriba un nombre valido")
    exit()

email = list()
contador = 0

for line in file:
    if line.startswith("From") :
        first_p = line.find(" ")
        second_p = line.find(" ",first_p+1)
        third_p = line[first_p+1:second_p]
        email.append(third_p)
        contador = contador + 1

print(email)
print("Se encontrador ",contador," coincidencia con la palabra From")
