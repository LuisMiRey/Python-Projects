print("Tuples exercise_09_02")

fname = input('Ingresa el nombre de archivo: ')

try:
    fhand = open(fname)

except:
    print('El archivo no se puede abrir:', fname)
    exit()

counts = dict()
contador = None
time = None

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    word = words[5]
    #print(word)
    counts[word] = counts.get(word,0) + 1

print(counts,"\n\n\n")

hours = dict()
for address in counts :
    print(address)
    dele = address[:2]
    print(dele)
    hours[dele] = hours.get(dele,0)+1

print(hours,"\n\n")


prov = list()

for time,contador in list(hours.items()):
    prov.append((time,contador))

prov.sort(reverse=True)

print(prov)
