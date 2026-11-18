
print("================================")
print("       ROCK PAPER SCISSORS")
print("================================")

player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name: ")

print("\nChoices:")
print("1. Rock")
print("2. Paper")
print("3. Scissors")

choice1 = input("\n" + player1 + ", enter your choice: ")
choice2 = input(player2 + ", enter your choice: ")

if choice1 == choice2:
    print("\nResult: It's a tie!")

elif choice1 == "Rock" and choice2 == "Scissors":
    print("\nWinner:", player1)

elif choice1 == "Paper" and choice2 == "Rock":
    print("\nWinner:", player1)

elif choice1 == "Scissors" and choice2 == "Paper":
    print("\nWinner:", player1)

elif choice1 == "Rock" and choice2 == "Paper":
    print("\nWinner:", player2)

elif choice1 == "Paper" and choice2 == "Scissors":
    print("\nWinner:", player2)

elif choice1 == "Scissors" and choice2 == "Rock":
    print("\nWinner:", player2)

else:
    print("\nInvalid choice! Please try again.")

print("\n       GAME OVER")
print("================================")
