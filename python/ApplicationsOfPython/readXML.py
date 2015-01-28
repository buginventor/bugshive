import codecs,encodings,sys

xmlfile = sys.argv[1] #odwolanie sie do pierwszego argumentu wpisanego z palca

fh = open(xmlfile)

counter=0
for line in fh:
	if (counter == 0):
		firstLine = line.split("\n")[0]
	counter += 1

print(firstLine)

if (firstLine.startswith("<?xml")):
	print("yes, this is an XML file")
else:
	print("this is NOT an XML file")
