import re
text = str(input('enter the string: '))

# text_2 = []
# text_2 = re.findall('[A-Z][a-z]*', text)
# print(text_2)

new_text = re.sub(r'(\w)([A-Z])', r'\1 \2', text )
print(new_text)