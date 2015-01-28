def main():
    print('Sipmle generator function')
    for i in inc_range(0,25,1):
        print(i,end=' ')

def inc_range(start,stop,step):
    i = start
    while i<=stop:
        yield i
        i+=step

main()
        
