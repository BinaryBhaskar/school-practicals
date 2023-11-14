def palindrome(string):
    return string.lower() == string[::-1].lower()

print("Hello:", palindrome("Hello"))
print("Nitin:", palindrome("Nitin"))