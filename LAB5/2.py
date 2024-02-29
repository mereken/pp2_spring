import re
pattern = re.compile("ab{2,3}")
n = str(input("enter the string: "))
print(pattern.match(n))
