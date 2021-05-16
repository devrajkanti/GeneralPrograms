def reverse(num):
    rev = 0
    reminder = 0
    while num > 0:
        reminder = num%10
        rev = rev * 10 + reminder
        num = num//10
        print(num)
    print(rev)

reverse(1234)