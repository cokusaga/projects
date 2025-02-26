import random
import csv

answer = input("Welcome to my game of rock, paper, scissors but with a twist. You may have heard about the additional plays spock and lizard. I've added these two to my game to make it more interesting. Would you like to play?: ")

while answer.lower() != "yes":
  answer = input("Re-enter your answer or check your spelling: ")
print("YAYYY!!")

while True:
  ans = input("\nWould you like to play a single player game, two player or simulation play?(sp/tp/smp): ")
  while ans.lower() != "sp" and ans != "tp" and ans != "smp":
    print("Invalid response")
    ans = input("Please enter one of the abbreviations above and check your spelling: ")
  if ans == "sp":
    print("\nOk, you will be playing against a computer. Goodluck!")
    user_action = input("\nEnter your choice (rock, paper, scissors, lizard, spock): ")
    while user_action.lower() != "rock" and user_action != "scissors" and user_action != "paper" and user_action != "lizard" and user_action != "spock":
      user_action = input("You entered an invalid answer, please cheack your spelling: ")
    actions = ["rock", "paper", "scissors", "lizard", "spock"]
    computer_action = random.choice(actions)
    print(f"\n-------------------------------------\nYou chose {user_action}\ncomputer chose {computer_action}.\n-------------------------------------\n")
    if user_action == computer_action:
      print(f"Both players selected {user_action}. It's a tie!")
      winner = "tie"
    elif user_action == "rock":
      if computer_action == "scissors" or computer_action == "lizard":
        print("Rock smashes", computer_action, " You win!")
        winner = "Player"
      else:
        print(computer_action, "covers rock! HAHA you lose.")
        winner = "Computer"
    elif user_action == "paper":
      if computer_action == "rock" or computer_action == "spock":
        print("Paper covers", computer_action, " You win!")
        winner = "Player"
      else:
        print(computer_action, "cuts paper! You lose.")
        winner = "Computer"
    elif user_action == "scissors":
      if computer_action == "paper" or computer_action == "lizard":
        print("Scissors cuts", computer_action, " You win!")
        winner = "Player"
      else:
        print(computer_action, "crushes scissors!  You lose.")
        winner = "Computer"
    elif user_action == "lizard":
      if computer_action == "spock" or computer_action == "paper":
        print("Lizard eats", computer_action, " You win!")
        winner = "Player"
      else:
        print(computer_action, "cruches lizard! You lose.")
        winner = "Computer"
    elif user_action == "spock":
      if computer_action == "scissors" or computer_action == "rock":
        print("Spock vaporises", computer_action, " You win!")
        winner = "Player"
      else:
        print(computer_action, "kills spock! You lose.")
        winner = "Computer"
    
    file = open("singlePlay.csv", "a")
    file.write(user_action + "," + computer_action + "," + winner + "\n")
    file.close()
   
    play_again = input("\nPlay again? (yes or no): ")
    while play_again.lower() != "yes" and play_again != "no":
      play_again = input("Please check your spelling and only enter the words above: ")
    if play_again == "no":
      print("Thank your for playing, bye now.")
      break

  if ans == "tp":
    print("Ok, please decide who you are playing with.")
    player_1 = input("Who will be player 1?: ")
    player_2 = input("Who will be player 2?: ")
    print()
    print("Welcome", player_1,"and", player_2,)
    print(player_1, "will pick first, then it will be", player_2,"going after. To maintain the integrity of the game, please pick your choices now. After your choices are picked, enter them into the computer to determine the winner.")
    user_action1 = input("\nEnter your choice (rock, paper, scissors, spock, lizard): ")
    while user_action1.lower() != "rock" and user_action1 != "paper" and user_action1 != "spock" and user_action1 != "lizard" and user_action1 != "scissors":
      user_action1 = input("You entered an invalid answer, please cheack your spelling: ")
    user_action2 = input("\nEnter your choice (rock, paper, scissors, spock, lizard): ")
    while user_action2.lower() != "rock" and user_action2 != "paper" and user_action2 != "spock" and user_action2 != "lizard" and user_action2 != "scissors":
      user_action2 = input("You entered an invalid answer, please cheack your spelling: ")
    print(f"\n-------------------------------------\n{player_1} chose {user_action1}\n{player_2} chose {user_action2}.\n-------------------------------------\n")
    if user_action1 == user_action2:
      print(f"Both players selected {user_action1}. It's a tie!")
      winner = "tie"
    elif user_action1 == "rock":
      if user_action2 == "scissors" or user_action2 == "lizard":
        print("Rock smashes", user_action2, player_1, "wins! And", player_2,"lost, HAHA!")
        winner = "Player1"
      else:
        print(user_action2, "covers rock! HAHA", player_1, "lost and",player_2, "won.")
        winner = "Player2"
    elif user_action1 == "paper":
      if user_action2 == "rock" or user_action2 == "spock":
        print("Paper covers", user_action2, player_1, "wins! And", player_2,"lost, HAHA!")
        winner = "Player1"
      else:
        print(user_action2, "cuts paper! HAHA", player_1, "lost and", player_2,"won.")
        winner = "Player2"
    elif user_action1 == "scissors":
      if user_action2 == "paper" or user_action2 == "lizard":
        print("Scissors cuts", user_action2, player_1, "wins! And", player_2, "lost, HAHA!")
        winner = "Player1"
      else:
        print(user_action2, "crushes scissors! HAHA", player_1, "lost  and",player_2, "won.")
        winner = "Player2"
    elif user_action1 == "lizard":
      if user_action2 == "spock" or user_action2 == "paper":
        print("Lizard eats", user_action2, player_1, "wins! And", player_2,"lost, HAHA!")
        winner = "Player1"
      else:
        print(user_action2, "cruches lizard! HAHA", player_1, "lostand",player_2, "won.")
        winner = "Player2"
    elif user_action1 == "spock":
      if user_action2 == "scissors" or user_action2 == "rock":
        print("Spock vaporises", user_action2, player_1, "wins! And", player_2,"lost, HAHA!")
        winner = "Player1"
      else:
        print(user_action2, "kills spock! HAHA", player_1, "lost and",player_2, "won.")
        winner = "Player2"
        
    file = open("twoPlay.csv", "a")
    file.write(user_action1 + "," + user_action2 + "," + winner + "\n")
    file.close()

    play_again = input("\nPlay again? (yes or no): ")
    while play_again.lower() != "yes" and play_again != "no":
      play_again = input("Please check your spelling and only enter the words above: ")
    if play_again == "no":
      print("Thank your", player_1, "and", player_2, "for playing, bye now.")
      break

  if ans == "smp":
    bet = input("\nPlease place your bets on which computer you think will win (computer_1, computer_2 or a tie): ")
    while bet.lower() != "computer_1" and bet != "computer_2" and bet != "tie":
      bet = input("Invalid response, please enter one of the words above: ")
    actions = ["rock", "paper", "scissors", "lizard", "spock"]
    computer_action1 = random.choice(actions)
    computer_action2 = random.choice(actions)
    print(f"\n-------------------------------------\nComputer_1 chose {computer_action1}\nComputer_2 chose {computer_action2}.\n-------------------------------------\n")
    if computer_action1 == computer_action2:
      print(f"Both players selected {computer_action1}. It's a tie!")
      winner = "tie"
      if bet == "tie":
        print("\nYou chose", bet, "your bet was correct, welldone!")
      else:
        print("\nYou chose", bet, "your bet was wrong")
    elif computer_action1 == "rock":
      if computer_action2 == "scissors" or computer_action2 == "lizard":
        print("Rock smashes", computer_action2,
              "computer_1 wins! And computer_2 lost")
        winner = "computer_1"
        if bet == "computer_1":
          print("\nYou chose", bet, "your bet was correct, welldone!")
        else:
          print("\nYou chose", bet, "your bet was wrong")
      else:
        print(computer_action2,"covers rock! computer_1 wins! And computer_2 lost")
        winner = "computer_2"
        if bet == "computer_2":
          print("\nYou chose", bet, "your bet was correct, welldone!")
        else:
          print("\nYou chose", bet, "your bet was wrong")
    elif computer_action1 == "paper":
      if computer_action2 == "rock" or computer_action2 == "spock":
        print("Paper covers", computer_action2,"computer_1 wins! And computer_2 lost")
        winner = "computer_1"
        if bet == "computer_1":
          print("\nYou chose", bet, "your bet was correct, welldone!")
        else:
          print("\nYou chose", bet, "your bet was wrong")
      else:
        print(computer_action2,"cuts paper! computer_1 lost and computer_2 won.")
        winner = "computer_2"
        if bet == "computer_2":
          print("\nYou chose", bet, "your bet was correct, welldone!")
        else:
          print("\nYou chose", bet, "your bet was wrong")
    elif computer_action1 == "scissors":
      if computer_action2 == "paper" or computer_action2 == "lizard":
        print("Scissors cuts", computer_action2,"computer_1 wins! And computer_2 lost")
        winner = "computer_1"
        if bet == "computer_1":
          print("\nYou chose", bet, "your bet was correct, welldone!")
        else:
          print("\nYou chose", bet, "your bet was wrong")
      else:
        print(computer_action2, "crushes scissors! computer_1 lost and computer_2 won.")
        winner = "computer_2"
        if bet == "computer_2":
          print("\nYou chose", bet, "your bet was correct")
        else:
          print("\nYou chose", bet, "your bet was wrong")
    elif computer_action1 == "lizard":
      if computer_action2 == "spock" or computer_action2 == "paper":
        print("Lizard eats", computer_action2,"computer_1 wins! And computer_2 lost")
        winner = "computer_1"
        if bet == "computer_1":
          print("\nYou chose", bet, "your bet was correct")
        else:
          print("\nYou chose", bet, "your bet was wrong")
      else:
        print(computer_action2, "cruches lizard! computerer_1 lost and computer_2 won.")
        winner = "computer_2"
        if bet == "computer_2":
          print("\nYou chose", bet, "your bet was correct")
        else:
          print("\nYou chose", bet, "your bet was wrong")
    elif computer_action1 == "spock":
      if computer_action2 == "scissors" or computer_action2 == "rock":
        print("Spock vaporises", computer_action2, "computer_1 wins! And computer_2,lost")
        winner = "computer_1"
        if bet == "computer_1":
          print("\nYou chose", bet, "your bet was correct")
        else:
          print("\nYou chose", bet, "your bet was wrong")
      else:
        print(computer_action2,"kills spock! computer_1 lost and computer_2 won.")
        winner = "computer_2"
        if bet == "computer_2":
          print("\nYou chose", bet, "your bet was correct")
        else:
          print("\nYou chose", bet, "your bet was wrong")

    file = open("Simulationplay.csv", "a")
    file.write(computer_action1 + "," + computer_action2 + "," + winner + "\n")
    file.close()

    play_again = input("\nPlay again? (yes or no): ")
    while play_again.lower() != "yes" and play_again != "no":
      play_again = input(
        "Please check your spelling and only enter the words above: ")
    if play_again == "no":
      print("Thank you for playing simulation play, bye now.")
      break
