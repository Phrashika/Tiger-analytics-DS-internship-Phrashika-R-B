# Program to sort comma-separated words alphabetically

# Take input from user
items = input("Enter words separated by commas: ")

# Split into list
words = items.split(",")

# Sort alphabetically
words.sort()

# Join back with commas and print
print(",".join(words))