def filter_prime(x):
    if x > 3:
        a = int(math.sqrt(x))
        for i in range(2, a + 1):
            if x % i == 0:
                return False
    else:
        return True
    return True
        
list = []
while True:
    x = int(input())
    if not x:
        break
    else: 
        if filter_prime(x):
            list.append(x)
for i in range(len(list)):
    print(list[i])

