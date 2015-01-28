def readFile(filename):
    if filename.endswith('.py'):
        fh=open(filename)
        return fh.readlines()
    else:
        raise ValueError('Filename must end with .py.')
        
def main():
    try:
        for line in readFile('loops.py'):
            print(line.strip())
    except IOError as e:
        print('cannot read file: ',e)
    except ValueError as e:
        print('Wrong, file extension is not .py.',e)

main()
