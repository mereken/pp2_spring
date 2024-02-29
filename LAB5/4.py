import re
pattern = re.compile("[A-Z][a-z]+")
n = str(input("enter the string: "))
print(pattern.findall(n))