d={'one':1,'two':2,'three':3}
x=dict(four=4,five=5,six=6)
print(d)
print(x)
d = dict(one=1,two=2,three=3,**x)
print(d)
for k in d:
    print(k)
for k,v in d.items():
    print(k,v)
    
print(d.get('three','not found in d'))
print(x.get('three','not found in x'))
print(x.pop('five')) #took 'five' out! remove!
print(x)
