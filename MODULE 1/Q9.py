# Program to sort (name, age, height) tuples by name > age > height

# Take comma-separated input from user
print("Enter records in format: name,age,height (separated by semicolons):")
data = input().split(";")   # allow multiple tuples separated by ;

# Convert to list of tuples
tuples_list = [tuple(item.split(",")) for item in data]

# Sort by name, then age, then height
sorted_list = sorted(tuples_list, key=lambda x: (x[0], int(x[1]), int(x[2])))

print(sorted_list)