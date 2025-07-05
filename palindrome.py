def is_palindrome(self,x: int) bool:
    s = str(x)
    return s == s[::-1]

print(is_palindrome(1331))  # True
print(is_palindrome(1234))  # False
