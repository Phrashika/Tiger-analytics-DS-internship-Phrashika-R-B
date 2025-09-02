# Program to generate a 2D array based on multiplication of indices

# Take input from user in comma-separated form
x, y = map(int, input("Enter two numbers separated by a comma (X,Y): ").split(","))

# Generate the 2D array
result = [[i * j for j in range(y)] for i in range(x)]

# Print the result
print(result)
