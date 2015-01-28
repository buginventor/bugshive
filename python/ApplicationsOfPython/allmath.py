class myMath:
	def add(self,x,y): #bez SELF mozna sie odwolac popzez nazwaPliku.nazwaKlasy.Metoda(arg,arg2)
		#result = lambda x,y: (x+y)
		#print(result)
		return x+y
	def sub(self,x,y):
		result = lambda x,y: (x-y)
		return result
	def mul(x,y):
		result = lambda x,y: (x*y)
		return result
	def div(x,y):
		result = lambda x,y: (x/y)
		return result		