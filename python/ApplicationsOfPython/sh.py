import shutil#,os
from os import path

def main():
	if path.exists("file1.txt"):
		src = path.realpath("file1.txt")
		location, filename = path.split(src)
		print("SRC: ", src)
		print("Directory: ",location)
		print("Filename: ",filename)
		print("Copying data")
		dst = src + ".bak"
		shutil.copy(src,dst) #kopiowanie zawartosci
		shutil.copystat(src,dst) # kopiowanie atrybutow
		print("Creating ZIP archive")
		root_dir, tail = path.split(src)
		shutil.make_archive("archive","zip",root_dir) # przyjmuje chyba tylko foldery
	else:
		src = "nowhere"
	print('It is in: ',location)
	


main()