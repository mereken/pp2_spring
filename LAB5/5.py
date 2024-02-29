import re
pattern = re.compile("a.*b$")
n = str(input("enter the string: "))
print(pattern.match(n))