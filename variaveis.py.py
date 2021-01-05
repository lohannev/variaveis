a = int(input('primeiro bimestre: '))
if a > 10:
    a = int (input('você digitou errado. primeiro bimestre: '))

b = int (input ('segundo bimestre: '))
if b > 10:
    b = int (input('você digitou errado. segundo bimestre: '))

c = int (input ('terceiro bimestre: '))
if c > 10:
    c = int (input('você digitou errado. terceiro bimestre: '))

d = int (input ('quarto bimestre: '))
if d > 10:
    d = int (input('você digitou errado. quarto bimestre: '))

media = (a + b + c + d) / 4

print ('media: {}'.format(media))

