# Question: Check Perfect Number

def is_perfect(num):
    if num <= 0:
        return False
    divisors_sum = 0
    for i in range(1, num):
        if num % i == 0:
            divisors_sum += i
    return divisors_sum == num

# Input
n = int(input("Enter a number: "))

# Output
if is_perfect(n):
    print("Perfect number")
else:
    print("Not a perfect number")
