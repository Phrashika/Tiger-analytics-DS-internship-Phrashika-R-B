import math

# Take n and m as input
n = int(input("Enter n: "))
m = int(input("Enter m: "))

# Apply formula: C(n - m + 1, m)
if n - m + 1 >= m:
    result = math.comb(n - m + 1, m)
else:
    result = 0

print("Output:", result)
