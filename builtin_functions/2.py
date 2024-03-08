string = str(input("string: " ))
upper_count = sum(1 for c in string if c.isupper())
lower_count = sum(1 for c in string if c.islower())

print("Upper case letters:", upper_count)
print("Lower case letters:", lower_count)
