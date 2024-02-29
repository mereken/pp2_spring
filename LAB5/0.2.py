# special sequences
# \d - any decimal digit [0-9]
# \D - any NON-digit character [^0-9]
# \s - any whitespace character 
# \S - any NON-whitespace character
# \w - any alphanumeric character [a-zA-Z0-9_]
# \W - any NON-alpanumeric character [^a-zA-Z0-9_]
# \b - matching patterns only at the beginning of the word
# \B - matching patterns only at the end of the word

import re

text = r"""
A regular expression (or RE) specifies a set of strings that matches it; the functions in this module let you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing).

Regular expressions can be concatenated to form new regular expressions; if A and B are both regular expressions, then AB is also a regular expression. In general, if a string p matches A and another string q matches B, the string pq will match AB. This holds unless A or B contain low precedence operations; boundary conditions between A and B; or have numbered group references. Thus, complex expressions can easily be constructed from simpler primitive expressions like the ones described here. For details of the theory and implementation of regular expressions, consult the Friedl book [Frie09], or almost any textbook about compiler construction.

A brief explanation of the format of regular expressions follows. For further information and a gentler presentation, consult the Regular Expression HOWTO.

Regular expressions can contain both special and ordinary characters. Most ordinary characters, like 'A', 'a', or '0', are the simplest regular expressions; they simply match themselves. You can concatenate ordinary characters, so last matches the string 'last'. (In the rest of this section, we’ll write RE’s in this special style, usually without quotes, and strings to be matched 'in single quotes'.)
"""
print(re.findall(r"\d", text))
print(re.findall(r"\s", text))
print(re.findall(r"\w", text))
print(re.findall(r"\breg", text))
print(re.findall(r"\Blar", text))
