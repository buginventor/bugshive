class inclusive_range:
    def __init__(self,*args):
        numArgs=len(args)
        if numArgs < 1: raise TypeError('Requires at least one argument')
        elif numArgs == 1:
            self.stop=args[0]
            self.step=1
            self.start=1
        elif numArgs == 2:
            (self.start,self.stop) = args
            self.step=1
        elif numArgs == 3:
            (self.start,self.stop,self.step) = args
        else:
            raise TypeError('Requires max 3 parameters, while you passed {}'.format(numArgs))

    def __iter__(self):
        i = self.start
        while i <= self.stop:
            yield i
            i += self.step
            
def main():
    o = inclusive_range(5,25)
    for i in o:
        print(i,end=' ')

main()
