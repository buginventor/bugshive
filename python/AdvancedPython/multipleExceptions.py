def main():
    counter=0
    try:
        x=1/0
        f=open('zloops.py')
        for line in f:
            print(line.strip())
        print("----------------")
        
    except IOError as e:
        print('File does not exist!',e)
        counter+=1
    except ZeroDivisionError as e:
        print('Nie dziel przez zero cholero!',e,'Yo!')
        counter+=1
    except:
        print('Some problem occured')
        counter+=1
    print('test')
    #finally:
        #print('Passed! WARNING lines under error are not executed!')
        #print("Number of errors: %d" % counter)

main()
