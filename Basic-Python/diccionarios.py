
print("Diccionarios")
'''
import string
fname = input('Ingresa el nombre de archivo: ')

try:
    fhand = open(fname)
except:
    print('El archivo no se puede abrir:', fname)
    exit()

counts = dict()

for line in fhand:
    if line.startswith("From"):
        line = line.rstrip()
        line = line.translate(line.maketrans('', '', string.punctuation))
        line = line.lower()
        words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print(counts)
'''
import string
fname = input('Ingresa el nombre de archivo: ')

try:
    fhand = open(fname)

except:
    print('El archivo no se puede abrir:', fname)
    exit()

counts = dict()
emails = dict()
emails_1 = dict()

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    word = words[1]
    #print(word)
    counts[word] = counts.get(word,0) + 1
    pos_1 = line.find("@")
    dele_1 = line[pos_1+1:]
    emails_1[dele_1] =emails_1.get(dele_1,0)+1

    '''    if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1 '''

print(counts)
print(emails_1)

for address in counts :
    print(address)
    pos = address.find("@")
    dele = address[pos+1:]
    print(dele)
    emails[dele] = emails.get(dele,0)+1

print(emails)


# Parte para encontrar el maximo y el minimo
max_res = 0
max_name = None
min_res = 0
min_name = None


for k,v in counts.items() :
    if (min_res == 0) or (v < min_res)  :
        min_res = v
        min_name = k

    elif v > max_res :
        max_res = v
        max_name = k

print("El valor maximo es = ",max_res," de ",max_name)
print("El valor minimo es = ", min_res," de ",min_name)
