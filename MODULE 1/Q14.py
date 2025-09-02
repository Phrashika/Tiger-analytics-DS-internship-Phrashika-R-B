# Program to find minimum possible denominations for given valid currency

def find_denominations(valid_currency, money):
    valid_currency.sort(reverse=True)  # sort in descending order
    result = []
    
    for coin in valid_currency:
        if money >= coin:
            count = money // coin
            money = money % coin
            result.append((coin, count))
    
    return result

# Input example
valid_currency = list(map(int, input("Enter valid currency (comma separated): ").split(",")))
money = int(input("Enter money: "))

result = find_denominations(valid_currency, money)

for coin, count in result:
    print(f"{coin}-{count}")
