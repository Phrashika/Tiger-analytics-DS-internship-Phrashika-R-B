# Stone-Paper-Scissor Game until one player scores 5 points

def find_winner(a, b):
    if a == b:
        return "DRAW"
    elif (a == "Stone" and b == "Scissor") or \
         (a == "Paper" and b == "Stone") or \
         (a == "Scissor" and b == "Paper"):
        return "Player A wins"
    else:
        return "Player B wins"

# Initialize scores
score_a, score_b = 0, 0

print("Game: Stone Paper Scissor (first to 5 points wins)")
print("Valid moves: Stone, Paper, Scissor\n")

while score_a < 5 and score_b < 5:
    move_a = input("Player A: ").capitalize()
    move_b = input("Player B: ").capitalize()

    result = find_winner(move_a, move_b)
    print("Result:", result)

    if result == "Player A wins":
        score_a += 1
    elif result == "Player B wins":
        score_b += 1

    print(f"Score -> Player A: {score_a}, Player B: {score_b}\n")

# Final result
if score_a == 5:
    print("🏆 Player A is the Champion!")
else:
    print("🏆 Player B is the Champion!")
