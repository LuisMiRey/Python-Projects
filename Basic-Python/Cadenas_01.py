''' fruta = 'banana'
indice = len(fruta)-1

while indice >= 0:
    letra = fruta[indice]
    print(letra)
    indice = indice - 1

fruta = 'banana'
for caracter in fruta:
    print(caracter)

num = [1;5]
type(num)
for algo in num:
    print(algo)
'''

# frase = 'Una multiplicacion 2x2=4'
'''
linea = 'Que tengas un buen día'
res = linea.startswith('Que')
print(type(res))
'''

phrase = '  X-DSPAM-Confidence:0.8475  '
sin= phrase.strip()
print(sin)
first = phrase.find(':')
print(first)
second = phrase[first+1:]
print(type(second))
num = float(second)
print(type(num),num)
