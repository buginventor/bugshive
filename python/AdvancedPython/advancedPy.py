def fileOpen(filename):
    global fh
    try:
        fh=open(filename)
        #tu moze byc wszystko co ma sie wykonac
    except IOError as e: #e - dostaje msg od IOError i wyswietla nizej
        print(e,"Brak pliku!")
    #else: #if NO errors do this below

def fileRead(filename):
    fileOpen(filename)
    for l in fh:
        print(l.strip())


def main():

    fileRead('loops.py')


main()

