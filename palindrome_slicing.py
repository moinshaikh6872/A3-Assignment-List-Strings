word = input("Enter a word to check if it's a palindrome: ")

# Using string slicing to reverse the word
if word == word[::-1]:
    print(f"'{word}' is a palindrome.")
else:
    print(f"'{word}' is not a palindrome.")
