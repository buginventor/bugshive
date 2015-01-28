def main():
	inputFile = open('binary.jpg','rb')
	outputFile = open('copiedB2.jpg','wb')
	
	bufferSize = 50000
	buffer = inputFile.read(bufferSize)
	while len(buffer):
		outputFile.write(buffer)
		print('.',end='')
		buffer = inputFile.read(bufferSize)
	print()
	print('Copy complete')

main()