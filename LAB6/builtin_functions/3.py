
# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]

# string = str(input('string: '))
# if is_palindrome(string):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

def isPalindrome(s):
    reverse = ''.join(reversed(s))
    if(s == reverse):
        return True
    return False
s = str(input('string is: '))
if (isPalindrome(s)):
    print("Palindrome")
else: 
    print("Not Palindrome")
