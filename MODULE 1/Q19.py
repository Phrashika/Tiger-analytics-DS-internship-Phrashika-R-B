def cyclic_rotation(case, s, times):
    results = []
    n = len(s)

    for t in range(times):
        if case == 1:   # Left rotation (first -> last)
            s = s[1:] + s[0]
        elif case == 2: # Right rotation (last -> first)
            s = s[-1] + s[:-1]
        else:
            return ["Invalid case! Use 1 or 2."]
        results.append(s.capitalize())  # Capitalize first letter for output
    return results


# -------- MAIN --------
case = int(input("Enter case (1 for left, 2 for right): "))
s = input("Enter string: ").strip()
times = int(input("Enter number of times: "))

output = cyclic_rotation(case, s, times)
for o in output:
    print(o)
