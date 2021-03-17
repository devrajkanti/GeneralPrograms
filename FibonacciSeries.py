n1, n2 = 0, 1
count = 0

nterms = int(input("How many terms?"))
if nterms < 0:
    print("Enter nterms greater than 0")
elif nterms == 1:
    print("Fibonacci series of", nterms, "is: ",n1)
else:
    while count < nterms:
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3

        count += 1