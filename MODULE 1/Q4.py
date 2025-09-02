# Program to find numbers between 1000 and 3000 where every digit is even

# Generate numbers between 1000 and 3000
result = []
for num in range(1000, 3001):  # inclusive of 3000
    # Check if all digits are even
    if all(int(digit) % 2 == 0 for digit in str(num)):
        result.append(str(num))

# Print as comma-separated values
print(",".join(result))