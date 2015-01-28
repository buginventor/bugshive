import sys

print("script name is : ", sys.argv[0])

if len(sys.argv)>1:
	print("there are",len(sys.argv)-1,"arguments")
	for arg in sys.argv[1:]:
		print(arg)
else:
	print("there are no arguments")
	
	
old = sys.stdout
sys.stdout = open("output.txt",'w')
print ('this line should be in the output.txt file')
sys.stdout = old
print('this is printed on the console')

print(sys.float_info.dig)

s = '3.14756872356762857632'
print(format(float(s),'.15g'))

counter=0
try:
	fh = open('dsag.txt','r')
except:
	counter+=1
	pass
finally:
	sys.exit("there were %d errors" %counter)
	