def main():
	infile = open('file1.txt')
	outfile = open('newfile.txt','w')
	
	for line in infile: # lub f.readlines()
			print(line,file=outfile,end='')
	print('Completed writing to new file')
			
	
main()