import re
text = str(input("enter the string: "))

text_2 = []
text_2 = re.findall('[A-Z][^A-Z]*', text)
print(str(text_2))