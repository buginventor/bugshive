import operator

getSecondItem = operator.itemgetter(1) #1 -seconditem
ls = ['a','b','c','d']

print(getSecondItem(ls))

print(operator.itemgetter(1,3,5)('abcdfg')) #extract only with these numbers

