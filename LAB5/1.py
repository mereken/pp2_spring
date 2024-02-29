# import re
# word = "AbcAbccccabc"
# print(re.match("Abc", word))

# import re
# pattern = re.compile("^[a-zA-Z\s]+$")
# print(pattern.search("Hello Everyone"))
# print(pattern.search("hello everyone"))
# print(pattern.search("helloeveryone"))

import re
pattern = re.compile("ab*")
n = str(input("enter the word: "))
print(pattern.match(n))
# print(pattern.match("abbbb"))
# print(pattern.match("a bc"))
# print(pattern.match("bdkmeo"))
# print(pattern.match("a bbbbbb"))
# print(pattern.match("a bbbbbbd"))






