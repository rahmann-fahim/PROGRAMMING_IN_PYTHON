def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

text = input("Enter a string: ")

if palindrome(text):
    print("Palindrome")
else:
    print("Not Palindrome")
