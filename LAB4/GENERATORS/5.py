def return_number(n):
    while n>=0:
        yield n
        n-=1

n = int(input('n = '))
for i in return_number(n):
    print(i, end=' ')
