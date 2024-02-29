import re

text = str(input('enter the string: '))

print(re.sub("[ ,.]", ":", text))