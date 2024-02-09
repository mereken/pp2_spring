from itertools import permutations

def all_permutations(string):
    charlist = list(string)
    perm = permutations(charlist, len(charlist))
    result = list(perm)
    return result
x = input()
print(all_permutations(x))