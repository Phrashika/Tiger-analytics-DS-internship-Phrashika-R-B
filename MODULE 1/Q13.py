# Program to count pairs in a binary string that start and end with 1

s = input("Enter a binary string: ")

# Count number of '1's
count_ones = s.count('1')

# Number of pairs = nC2 = n*(n-1)/2
pairs = count_ones * (count_ones - 1) // 2

print(pairs)
