def main():
    books = [('book1','a',7),('book2','f',9),('book3','a',2)]
    from operator import itemgetter,attrgetter
    print(sorted(books,key=itemgetter(2))) #sort by 3rd (2nd) element in tuple
    print(sorted(books,key=itemgetter(2),reverse=True))

main()
