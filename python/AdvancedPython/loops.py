def main():
    data="this is where I want to break"
    for char in data:
        if char=='b': break
        print(char,end='')
        
main()
