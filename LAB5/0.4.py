import re

text = r"""
Match objects always have a boolean value of True. Since match() and search() return None when there is no match, you can test whether there was a match with a simple if statement:

match = re.search(pattern, string)
if match:
    process(match)
class re.Match
Match object returned by successful matches and searches.

Changed in version 3.9: re.Match supports [] to indicate a Unicode (str) or bytes match. See Generic Alias Type.

Match.expand(template)
Return the string obtained by doing backslash substitution on the template string template, as done by the sub() method. Escapes such as \n are converted to the appropriate characters, and numeric backreferences (\1, \2) and named backreferences (\g<1>, \g<name>) are replaced by the contents of the corresponding group. The backreference \g<0> will be replaced by the entire match.
"""

pattern = r"[Mm]at[a-z]+"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.start())
    print(match.end())
    print(match.span())
    print(match.group())
    # print(match.string)
    print("---------")