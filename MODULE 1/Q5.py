# Program to count letters and digits in a sentence

# Take input from user
text = input("Enter a sentence: ")

# Initialize counters
letters = 0
digits = 0

# Check each character
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

# Print result
print("LETTERS", letters)
print("DIGITS", digits)
