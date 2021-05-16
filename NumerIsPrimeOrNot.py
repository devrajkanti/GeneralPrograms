mylist = [1,7,10,39,42,26,57,109]
for num in mylist:
    if num > 1:
        for i in range (2,num):
            if num % i == 0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is prime")
    else:
        print("Number less than equal to 1 are not considered")