# Question 22: Convert Decimal to Binary (without inbuilt function)

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary   # remainder becomes the next binary digit
        n //= 2
    return binary

# Input
num = int(input("Enter a decimal number: "))

# Output
print(decimal_to_binary(num))

