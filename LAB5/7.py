import re
text = str(input("enter the string: "))
print("the snake case string: ", text)

temp = re.split('_+', text)

result = temp[0] + ''.join(map(lambda x: x.title(), temp[1:]))
print("the camel string is: " + str(result))