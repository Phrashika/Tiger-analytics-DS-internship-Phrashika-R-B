# Question 21: Check Armstrong Number

def is_armstrong(num):
    digits = str(num)               # convert number to string
    power = len(digits)             # number of digits
    total = sum(int(d)**power for d in digits)  # sum of digits^power
    return total == num

# Input
num = int(input("Enter a number: "))

# Check and Output
if is_armstrong(num):
    print("Armstrong number")
else:
    print("Not an Armstrong number")
