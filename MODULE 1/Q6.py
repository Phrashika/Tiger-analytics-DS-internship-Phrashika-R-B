# Program to count uppercase and lowercase letters in a sentence

# Take input from user
text = input("Enter a sentence: ")

# Initialize counters
upper_case = 0
lower_case = 0

# Check each character
for char in text:
    if char.isupper():
        upper_case += 1
    elif char.islower():
        lower_case += 1

# Print result
print("UPPER CASE", upper_case)
print("LOWER CASE", lower_case)
