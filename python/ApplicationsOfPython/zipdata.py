import zipfile

def makeZip():
	fh = zipfile.ZipFile('mydata.zip','w')
	fh.write('file1.txt') #nie dodawac kilku po przecinku
	fh.write('newfile.txt')
	fh.close()
	
def openZip():
	fh = zipfile.ZipFile('mydata.zip','r')
	names = fh.namelist()
	for name in names:
		print('processing %s ' %name)
		fh2=fh.open(name)
		contents=fh2.read()
	
def main():
	makeZip()
	openZip()

main()

