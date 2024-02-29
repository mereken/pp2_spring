import re
# text = str(input("enter the string: "))
# print("the camel case string: ", text)

# text_2 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text).lower()


# print("the snake case string is: " + str(text_2))

 
def change_case(text):
    text_2 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', text_2).lower()
     
text = str(input('enter the camel case string: '))
print(change_case(text))