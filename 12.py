a=input('Enter a string: ')
c=list(a)
sum=0
print(c)
for i in c:
    if(ord(i)>=65 and ord(i)<=90):
        sum=sum+ord(i)-64

    elif((ord(i)>=97 and ord(i)<=122)):
        sum=sum+ord(i)-96
    else:
        pass
print(sum)
import random
x=random.randint(20,100)

print(x)
