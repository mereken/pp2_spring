def even_nums(n):
    for i in range(n):
        if i%2==0:
            yield i

n = int(input('enter the number: '))
even = even_nums(n)
for i in even:
    print(i, end=',')