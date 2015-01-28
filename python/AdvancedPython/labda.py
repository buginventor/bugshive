t = lambda x: x*2
print(t(3))

#normal method
def add(x,y):
    return x+y
print(add(15,3))


result = lambda x,y: (x+y,x-y)
print(result(10,10)[0]) #bez [0] wyswietli oba wyniki (+rx,-rx)

q=tuple(range(25)) #this is a TUPLE, list - cannot change elements
print(type(q))
print(10 in q)
print(25 in q)
print(2436 not in q)

for n in q:
    print(n)
c=list(range(25)) # this is an ARRAY tuple, mozna dodawać i pop'owac
print(type(c))
print(c)

print(c.count(20))
print(c.index(20))
