def to_centigrate (f):
    c = (5/9) * (f-32)
    return c
f = float(input("Enter the temperature: "))
print (to_centigrate(f))