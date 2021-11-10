import re

try:
    hand = input("Ente the name: ")
    if hand == "un huevo":
        print("Tienes cara de bola")

    else:
        man = open(hand)
except:
    print("Enter a valid name ")

count = 0
sum = 0
promedio = 0
average = 0
total = list()
avg = list()
#word = input('Intruduce una expresion regular: ')
for linea in man:
    linea = linea.rstrip()
    num = re.findall('New Revision: ([0-9]+)', linea)
    #print(num)
    if len(num) > 0 :
        #print(num)
        total.extend(num)
        count = count + 1

print(total,"\n\n")

for final in total:
    nm = float(final)
    promedio = nm + promedio

ab = promedio/count

print("El numero de coincidencias es = ",count,"\n\n")
print("Average is = ",ab)

     #new = re.findall(r'[a-zA-Z0-9]\S*@\S*[a-zA-Z]', linea)
    #if len(new)>0:
    #    print(new)
