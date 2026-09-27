import random
from collections import Counter

# Valid moves
MOVES = ["rock", "paper", "scissors"]

# Tracks the player's move history
player_history = []

def get_ai_move():
    """
    AI predicts the player's most common move
    and plays the move that beats it.
    """
    if not player_history:
        return random.choice(MOVES)

    # Find the player's most frequently used move
    most_common = Counter(player_history).most_common(1)[0][0]

    # Counter strategy
    if most_common == "rock":
        return "paper"
    elif most_common == "paper":
        return "scissors"
    else:
        return "rock"

def determine_winner(player, ai):
    if player == ai:
        return "tie"

    winning_moves = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if winning_moves[player] == ai:
        return "player"
    else:
        return "ai"

def play_game():
    player_score = 0
    ai_score = 0

    print("=== Rock Paper Scissors ===")
    print("Type rock, paper, scissors, or quit to exit.\n")

    while True:
        player = input("Your move: ").lower().strip()

        if player == "quit":
            break

        if player not in MOVES:
            print("Invalid move! Try again.\n")
            continue

        ai = get_ai_move()
        player_history.append(player)

        print(f"AI chose: {ai}")

        result = determine_winner(player, ai)

        if result == "player":
            print("You win this round!")
            player_score += 1
        elif result == "ai":
            print("AI wins this round!")
            ai_score += 1
        else:
            print("It's a tie!")

        print(f"Score -> You: {player_score} | AI: {ai_score}")
        print("-" * 30)

    print("\nFinal Score")
    print(f"You: {player_score}")
    print(f"AI: {ai_score}")
    print("Thanks for playing!")

if __name__ == "__main__":
    play_game()
