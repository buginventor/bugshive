class data:
    def __init__(self,value): #constructor is runned when instance is created
        self._v=value
        print("constructor")
    def create(self):
        print("creating data ",self._v)
    def update(self):
        print("update",self._v)
    def delete(self):
        print("remove data ",self._v)

class files:
    def __init__(self,ftype='text'):
        self._ftype='text' #tu chyba moze byc =ftype, bo tak to dwa razu jest
    def move(self):
        print("move files")
    def copy(self):
        print("copying files")

    def set_ftype(self,ftype):
        self._ftype=ftype
    def get_ftype(self):
        return self._ftype

class fileSystem:
    def convertTo(self):
        print('Converted to unknown file system - PARENT')
    def dynPartition(self):
        print('Changing partition')
    def status(self):
        print('Status')
    def virtual(self):
        print("Now it's virtual file system")

# klasa typu inheritance - wykorzystuje po podanej klasie - nadpisuje metody
class NTFS(fileSystem):
    def convertTo(self):
        super().convertTo() #EXEC from parent class
        print('Converted to NTFS - CHILD')
    def defrag(self):
        print('Defragmenting')
    
# polymorfizm uzywa odpowiedniej metody do typu obiektu

class network:
    def cable(self):
        print('Cable')
    def router(self):
        print('Router')
    def switch(self):
        print('Switch')
    def wifi(self):
        print("WIFI")

class tokenRing(network):
    def cable(self): print('Tokenring cable')
    def router(self): print('Tokenring router')

class ethernet(network):
    def cable(self): print('ETH cable')
    def router(self): print("ETH router")
    def wifi(self): print("ETH WIFI")
    
    
def main():
    customerData=data(23563) #instance of data class
    customerData.create()
    customerData.update()
    customerData.delete()

    AcustomerData=data(555) #another instance of data class
    AcustomerData.create()
    AcustomerData.update()
    AcustomerData.delete()

    print("====================")

    testFiles=files() #instance of files class
    testFiles.move()
    testFiles.copy()
    print(testFiles.get_ftype()) # przy returnie musi byc print
    testFiles.set_ftype('.mov')
    print(testFiles.get_ftype())

    print("====================")          

    myFs=fileSystem()
    myFs.convertTo()
    myFS2=NTFS()
    myFS2.convertTo()
    myFS2.virtual() # pobrane z parent class a wywolane w child

    print("====================")
    
    windows=tokenRing()
    mac=ethernet()
    for obj in (windows, mac):
        obj.cable()
        obj.router()
        obj.wifi()

    print("===================")
    print(sorted([1,4,9,8,5,6]))

main()
