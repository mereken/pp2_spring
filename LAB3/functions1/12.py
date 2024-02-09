def histogram(x):
    result = []
    for i in range(len(x)):
        m = ''
        for j in range(int(x[i])):
            m += '*'
        print(m)

x = input()
list = [i for i in x.split()]
histogram(list)