def unique(x):
    list = []
    n = 1
    for i in range(len(x)):
        n = 1
        for j in range(len(x)):
            if i != j:
                if x[i] == x[j]:
                    break
                else:
                    n += 1
        if n == len(x):
            list.append(x[i])
    return list

x = input()
list = [str(a) for a in x.split()]
print(unique(list))