# Program to find alphabet pairs where sum of digits between them = 9

s = input("Enter an alphanumeric string: ")

pairs = []
i = 0

while i < len(s):
    if s[i].isalpha():  # found a letter
        j = i + 1
        digits = ""
        while j < len(s) and s[j].isdigit():  # collect digits
            digits += s[j]
            j += 1
        if j < len(s) and s[j].isalpha() and digits:  # next is a letter
            digit_sum = sum(int(d) for d in digits)  # sum of digits
            if digit_sum == 9:
                pairs.append((s[i], s[j]))
        i = j
    else:
        i += 1

# Print results
for p in pairs:
    print(f"{p[0]},{p[1]}")
