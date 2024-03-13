Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
... import time
... 
... # Define characters
... characters = ["Scorpion", "Sub-Zero", "Raiden", "Liu Kang", "Sonya Blade"]
... 
... # Define moves and their damage
... moves = {
...     "punch": 10,
...     "kick": 15,
...     "block": 5,
...     "special": 20
... }
... 
... # Function to simulate a fight
... def fight(player1, player2):
...     print(f"A fight between {player1} and {player2} begins!\n")
...     time.sleep(1)
... 
...     player1_health = 100
...     player2_health = 100
... 
...     while player1_health > 0 and player2_health > 0:
...         print(f"{player1}'s health: {player1_health}")
...         print(f"{player2}'s health: {player2_health}")
...         print("\nWhat move will you choose?")
...         print("1. Punch")
...         print("2. Kick")
...         print("3. Block")
...         print("4. Special")
...         choice = input("Enter your choice (1-4): ")
... 
...         enemy_choice = random.choice(list(moves.keys()))
... 
...         if choice == '1':
...             player2_health -= moves["punch"]
            print(f"{player1} punched {player2}!")
        elif choice == '2':
            player2_health -= moves["kick"]
            print(f"{player1} kicked {player2}!")
        elif choice == '3':
            player1_health += moves["block"]
            print(f"{player1} blocked the attack!")
        elif choice == '4':
            player2_health -= moves["special"]
            print(f"{player1} used a special move against {player2}!")
        else:
            print("Invalid choice. Try again.")

        time.sleep(1)

        if player2_health <= 0:
            print(f"\n{player1} wins!")
            break

        # Enemy's turn
        print(f"{player2} chose to {enemy_choice}!")
        if enemy_choice == 'punch':
            player1_health -= moves["punch"]
            print(f"{player2} punched {player1}!")
        elif enemy_choice == 'kick':
            player1_health -= moves["kick"]
            print(f"{player2} kicked {player1}!")
        elif enemy_choice == 'block':
            player2_health += moves["block"]
            print(f"{player2} blocked the attack!")
        elif enemy_choice == 'special':
            player1_health -= moves["special"]
            print(f"{player2} used a special move against {player1}!")

        time.sleep(1)

        if player1_health <= 0:
            print(f"\n{player2} wins!")
            break

# Main function
def main():
    print("Welcome to Mortal Kombat Text Edition!\n")

    print("Choose your character:")
    for i, character in enumerate(characters):
        print(f"{i+1}. {character}")

    player_choice = int(input("Enter the number of your choice: "))
    player1 = characters[player_choice - 1]

    remaining_characters = characters[:player_choice - 1] + characters[player_choice:]
    player2 = random.choice(remaining_characters)

    print(f"\nYou've chosen {player1}. Your opponent is {player2}.\n")

    fight(player1, player2)

if __name__ == "__main__":
    main()
