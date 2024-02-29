import re
pattern = re.compile("[a-z]+_[a-z]+")
n = str(input("enter the string: "))
print(pattern.findall(n))