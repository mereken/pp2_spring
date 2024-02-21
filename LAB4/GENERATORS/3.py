def divisible_by(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0:
            yield i
n = int(input('enter the number: '))
for num in divisible_by(n):
    print(num, end=' ')