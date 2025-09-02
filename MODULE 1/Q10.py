import math

# Program to calculate robot distance from origin

x, y = 0, 0

print("Enter moves (format: DIRECTION steps) separated by commas:")
moves = input().split(",")

for move in moves:
    move = move.strip()
    if not move:
        continue
    direction, steps = move.split()
    steps = int(steps)

    if direction.upper() == "UP":
        y += steps
    elif direction.upper() == "DOWN":
        y -= steps
    elif direction.upper() == "LEFT":
        x -= steps
    elif direction.upper() == "RIGHT":
        x += steps

# Compute Euclidean distance
distance = round(math.sqrt(x**2 + y**2))

print(distance)


