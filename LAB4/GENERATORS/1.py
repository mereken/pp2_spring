def squares_generator(n):
    for i in range (n):
        yield i**2

n = int(input('enter the number: '))
for i in squares_generator(n):
    print(i,end=' ')


