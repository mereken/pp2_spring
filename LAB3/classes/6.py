def isPrime(num):

    if num > 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
        
lst = [1, 3, 4, 6, 10, 11, 15, 17, 19]

new_lst = list(filter(lambda x: (isPrime(x) == True), lst))

print(new_lst)