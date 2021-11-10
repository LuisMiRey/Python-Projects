print("This is Tuples")

fname = input('Ingresa el nombre de archivo: ')

try:
    fhand = open(fname)

except:
    print('El archivo no se puede abrir:', fname)
    exit()

counts = dict()
contador = None
mail = None

for line in fhand:
    line = line.rstrip()
    words = line.split()
    if len(words) < 3 or words[0] != 'From':
        continue
    word = words[1]
    #print(word)
    counts[word] = counts.get(word,0) + 1
    '''    if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1 '''

print(counts,"\n\n\n")
prov = list()

for mail,contador in list(counts.items()):
    prov.append((contador,mail))

prov.sort(reverse=True)

print(prov)

'''
for address in counts :
    print(address)
    pos = address.find("@")
    dele = address[pos+1:]
    print(dele)
    emails[dele] = emails.get(dele,0)+1

print(emails)'''
