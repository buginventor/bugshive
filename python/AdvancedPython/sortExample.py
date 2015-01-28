def main():
    print(sorted([1,4,9,8,5,6]))
    print(sorted(['a','z','h','b','0']))
    items=['bread','cheese','eggs','sausage']

    print(sorted(items))
    print('===================')
    books = [('book1','a',7),('book2','f',9),('book3','a',2)]
    print(books)
    
    #sort by 3rd element - the number in tuple
    print(sorted(books,key=lambda books: books[2])) 
main()
