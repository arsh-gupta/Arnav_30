x=int(input('Enter the number of rows: '))
for i in range(0,x):
    for j in range(0,i+1):
        if(i%2!=0):
            print('0',end="")
        else:
            print(i+1,end="")
        j+=1
    print('\n')
    i+=1
