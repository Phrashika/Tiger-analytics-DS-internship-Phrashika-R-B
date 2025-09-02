# Program to remove duplicate words and sort them alphanumerically

# Take input from user (whitespace-separated words)
words = input("Enter words separated by spaces: ")

# Split into list
word_list = words.split()

# Remove duplicates using set, then sort
unique_sorted_words = sorted(set(word_list))

# Join back with space and print
print(" ".join(unique_sorted_words))