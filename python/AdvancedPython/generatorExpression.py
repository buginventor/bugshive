#generator_expr::= "(" express comp_for ")"

#(x*y for x in range(10) for y in bar(x))

#ENUMERATE
seasons=['spr', 'summ', 'aut', 'wint']
print(list(enumerate(seasons, start=1)))

#Evaluations - nie zmienia wartosci argumentu(obiektu) podaje tylko wynik
x=1
print(eval('x+1'))
print(x)

print(eval('x==2')) # sprawdzenie czy wartosc sie zgadza

with open('loops.py') as fh:
    for line in iter(fh.readline,''):
        print(line)

fh2=open('loops.py')
for line in fh2:
    print(line.split()) #each row in array with those elements
