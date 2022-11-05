#reverse the digit of the number
num = 1234
#logic here
while num != 0:
    ld = num % 10
    num //= 10
    print(ld, end= 'dr')