def reverse_string(x):
    sentense = x.split()
    result = ' '.join(reversed(sentense))
    return result
sentense = input()
print(reverse_string(sentense))