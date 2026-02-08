#RPS.py
#Name:Zane Serhan
#Date:2/7/2026
#Assignment:Lab3 RPS
#Purpose: Play RPS with user vs random computer choice with many rounds and display results at end.

import random

def main():
  wins = 0
  ties = 0
  losses = 0
  PlayAgain = True

  #Create a loop that continues as long as the user wants to play.

  while PlayAgain:

  #Randomly choose the computer between 'R', 'P', or 'S'

    Computer = random.choice(['R','P','S'])

  #Prompt the user for their RPS selection

    User = input("Select Rock, Paper, or Scissors (R, P, S)   ").upper()

    if User == 'R' or User == 'P' or User == 'S':
      if User == 'R':
       UserChoice = "Rock"
      elif User == 'P':
       UserChoice = "Paper"
      elif User == 'S':
        UserChoice == "Scissors"

      if Computer == 'R':
        ComputerChoice = "Rock"
      elif Computer =='P':
        ComputerChoice == "Paper"
      elif Computer == 'S':
        ComputerChoice == "Scissors"

      print("Player chose: ", UserChoice)
      print("Computer chose: ", ComputerChoice)

  #Determine winner and state what happened to the user

      if User == Computer:
        print("It's a tie!")
        ties = ties + 1
      elif((User == 'R' and Computer == 'S') or
         (User == 'P' and Computer == 'R') or
         (User == 'S' and Computer == 'P')):
        print("You win!")
        wins = wins + 1
      else:
        print("You lose!")
        losses = losses + 1

  #Ask the user if they would like to play again.

      Ask = input("Would you like to play again? (Y/N)").upper()
      if Ask != 'Y':
        PlayAgain = False

  else:
    print("Invalid choice. Try again. Enter R or P or S")


  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
