print("1 programa del tema listas\n")

name = input("Escriba el nombre del archivo : ")

try:
    file = open(name)
    print(file)
except:
    print("Introduzca un nombre valido ")
    exit()

text = list()
text1 = list()
for line in file:
    #nex = line.split()
    text.extend(line.split())



text1 = sorted(set(text))
print(text1)
