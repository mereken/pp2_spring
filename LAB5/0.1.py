import re
# meta characters
# * + . ? ^ $ { } [ ] ( ) |
# quantifiers
# * - 0 or more occurences
# + - 1 or more occurences
# ? - 0 or 1 occurence

# word = "AAbbAbbbbabbbb"
# print(re.findall("Ab*", word))
# print(re.findall("Ab+", word))
# print(re.findall("Ab?", word))


# . - any symbol
# ^ - matches only at the beginning of the string
# $ - matches only at the end of the string

# word = "AAbbAbbbbabbbb"
# print(re.findall("ab*$", word))
# print(re.findall("A.+", word))
# print(re.findall("^Ab?", word))


# | - either or

# word = "roses are red, violets are blue"
# print(re.findall("roses|violets", word))

# [ ] - set of symbols

# word = "R0ses are r3d, v1olets are blu3"
# print(re.findall("[abc]", word))
# print(re.findall("[a-z]", word))
# print(re.findall("[a-zA-Z0-9]", word))

# {n} - n number of occurences
# {n,m} - from n to m number of occurences

# word = "R0ses are r3d, v1olets are blu3"
# print(re.findall("[a-zA-Z0-9]{2}", word))
# print(re.findall("[a-zA-Z0-9]{2,6}", word))


# ( ) - grouping
word = r"R0ses are r3d, v1olets are blu3"
print(re.findall(r"([a-zA-Z0-9]{2})", word))
print(re.findall(r"([a-zA-Z0-9]{2})+", word))

pattern = re.compile(r"([a-zA-Z0-9]{2})+")
matches = pattern.finditer(word)
for match in matches:
    print(match.group(), end=" ")



