def pattern_a(rows):
    num = 1
    for i in range(1, rows+1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        print(" * ".join(row))


def pattern_b(rows):
    # upper part
    for i in range(1, rows+1):
        print(" "*(rows-i) + " ".join(["*"]*i))
    # lower part
    for i in range(rows-1, 0, -1):
        print(" "*(rows-i) + " ".join(["*"]*i))


def pattern_c(rows):
    num = 1
    result = []

    # upper half
    for i in range(1, rows+1):
        row = []
        for j in range(i):
            row.append(str(num))
            num += 1
        result.append(" * ".join(row))

    # lower half (reverse except top row)
    result += result[-2::-1]

    for line in result:
        print(line)


def pattern_d(rows):
    for i in range(rows):
        if i == 0:
            print(" " + "*"*3 + "  ")
        elif i == rows//2:
            print(" *" + "*"*3 + " ")
        elif i == rows-1:
            print("  * * *  ")
        elif i < rows//2:
            print(" *")
        else:
            print(" *    *")


def pattern_e(n):
    for i in range(n):
        row = []
        for j in range(n):
            if i == 0 or i == n-1 or j == n//2:
                row.append("1")
            else:
                row.append("0")
        print(" ".join(row))


# ---------------- MAIN MENU ----------------
while True:
    print("\nChoose a Pattern to Print:")
    print("a) Number Pyramid with *")
    print("b) Diamond * pattern")
    print("c) Number Pyramid + Reverse")
    print("d) Pattern 'G'")
    print("e) Matrix with 1s and 0s (Cross Shape)")
    print("q) Quit")

    choice = input("\nEnter choice (a-e/q): ").lower()

    if choice == 'a':
        rows = int(input("Enter number of rows: "))
        pattern_a(rows)
    elif choice == 'b':
        rows = int(input("Enter number of rows: "))
        pattern_b(rows)
    elif choice == 'c':
        rows = int(input("Enter number of rows: "))
        pattern_c(rows)
    elif choice == 'd':
        rows = int(input("Enter number of rows (e.g., 7): "))
        pattern_d(rows)
    elif choice == 'e':
        rows = int(input("Enter odd number of rows: "))
        pattern_e(rows)
    elif choice == 'q':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please select again.")
