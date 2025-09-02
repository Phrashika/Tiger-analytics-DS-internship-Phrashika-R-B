# Program to compute net amount from transaction logs

net_amount = 0

print("Enter transactions (D/W followed by amount), separated by commas:")
transactions = input().split(",")   # comma-separated input

for t in transactions:
    t = t.strip()   # remove extra spaces
    if not t:
        continue
    action, amount = t.split()
    amount = int(amount)

    if action.upper() == "D":
        net_amount += amount
    elif action.upper() == "W":
        net_amount -= amount

print(net_amount)