def main():
	bufferSize=50000
	infile=open('bigfile.txt','r')
	outfile=open('newbig.txt','w')
	buffer=infile.read(bufferSize)
	
	while len(buffer):
		outfile.write(buffer)
		print('.',end='')
		buffer=infile.read(bufferSize)
	print()
	print('Done!')


main()