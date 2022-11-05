num = int(input('ENTER THE NUMBER = '))
num1 = num
rev = 0 
#logic here
while num != 0:
    ld = num % 10
    num //= 10
    rev = rev * 10 + ld
print(rev)
if num1 == rev:
    print('the given number is plindrone')
else:
    print('number is not polindrone')
        