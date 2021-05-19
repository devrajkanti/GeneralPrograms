num = 407
sum = 0

while num > 0:
    remainder = num % 10
    sum = sum + remainder ** 3
    num = num // 10

print(sum)
if num == sum:
    print("Armstrong")
else:
    print("Not Armstrong")