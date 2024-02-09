def polindrome(x):
    m = ''.join(reversed(x))
    if x == m:
        return True
    return False

x = input()
if polindrome(x):
    print('yes')
else:
    print('no')