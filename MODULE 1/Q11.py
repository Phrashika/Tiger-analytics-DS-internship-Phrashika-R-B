# Program to find continuous occurrence of characters (Run-Length Encoding)

s = input("Enter a string: ")

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        result += s[i-1] + str(count)
        count = 1

# Add the last character and its count
result += s[-1] + str(count)

print(result)

