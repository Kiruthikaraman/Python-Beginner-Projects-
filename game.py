import random
import sys

# Game Title
GAME_TITLE = "Data Saga Adventure"

# Characters
CHARACTERS = [
    {"name": "Algo Knight", "special": "Fast Sorting"},
    {"name": "Stack Mage", "special": "Undo Spell"},
    {"name": "Queue Ranger", "special": "First-In Arrow"},
]

# Levels and Challenges
LEVELS = [
    {
        "name": "Level 1: Array Arena",
        "challenge": "Reverse the array: [1, 2, 3, 4, 5]",
        "solution": lambda: [5, 4, 3, 2, 1]
    },
    {
        "name": "Level 2: Stack Summit",
        "challenge": "Simulate stack push/pop: push 1,2,3 then pop once.",
        "solution": lambda: [1, 2]
    },
    {
        "name": "Level 3: Queue Quest",
        "challenge": "Simulate queue enqueue/dequeue: enqueue 4,5,6 then dequeue once.",
        "solution": lambda: [5, 6]
    },
    {
        "name": "Level 4: Linked List Labyrinth",
        "challenge": "Insert 7 after 2 in [1,2,3]",
        "solution": lambda: [1, 2, 7, 3]
    },
    {
        "name": "Level 5: Binary Search Battle",
        "challenge": "Find index of 8 in [2,4,6,8,10] using binary search.",
        "solution": lambda: 3
    }
]

def print_title():
    print("=" * 40)
    print(f"{GAME_TITLE:^40}")
    print("=" * 40)

def choose_character():
    print("\nChoose your character:")
    for idx, char in enumerate(CHARACTERS):
        print(f"{idx+1}. {char['name']} - Special: {char['special']}")
    while True:
        choice = input("Enter character number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(CHARACTERS):
            return CHARACTERS[int(choice)-1]
        print("Invalid choice. Try again.")

def play_level(level):
    print(f"\n{level['name']}")
    print(f"Challenge: {level['challenge']}")
    user_input = input("Your answer (as Python list or value): ")
    try:
        user_answer = eval(user_input)
    except Exception:
        print("Invalid input format.")
        return False
    correct = level['solution']()
    if user_answer == correct:
        print("Correct! You advance to the next level.")
        return True
    else:
        print(f"Incorrect. The correct answer was: {correct}")
        return False

def main():
    print_title()
    character = choose_character()
    print(f"\nWelcome, {character['name']}! Your adventure begins...\n")
    for level in LEVELS:
        if not play_level(level):
            print("Game Over. Try again!")
            sys.exit()
    print("\nCongratulations! You completed Data Saga Adventure!")

if __name__ == "__main__":
    pygame.init()
    main()
    pygame.quit()