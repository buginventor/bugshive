def main():
    global items

    items=['bread','cheese','milk']
    letters="abcdefghij"
    grocery=["bread","cheese","milk","eggs","corn","juice"]
    slice(letters)
    slice(items)
    sortInPlace(grocery)

def slice(tab):
    slice1=tab[1:3]
    slice2=tab[:3] #beginning to 3rd
    slice3=tab[:-1] #minus last letter

    print(slice1,'\t',slice2,'\t',slice3)

    items[1]='nothing' #replace object
    print(items)
    
def sortInPlace(items):
    print(items)
    
    items.sort()    #przypisanie wyniku do zmiennej nie ma sensu
                    #ta funkcja od razu porzadkuje obiekty w obiekcie
    print(items)
    newlist=sorted(items,key=lambda x: x,reverse=True)
    #inny sposob: items.sort(key=lambda x: x,reverse=True)
    print(newlist)
    
main()

