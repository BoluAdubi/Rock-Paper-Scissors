#Boluwatife Adubi
#08/17/18
#This program will simulate a game of rock paper scissors between the user and the PC
import random

#This function tells the computer to pick a random string from the list each time it is called upon
def compChoice():

  options = ["r", "p", "s"]
  return random.choice(options)#This is returned so I can assign a variable to the function later


def RPS():
  
  print("")
  intro = input("Would you like to play rock, paper, scissors? y or n?: ")

  if intro == "y":
    comp = compChoice()
    print("")
    print("Awesome! r is Rock, p is Paper, and s is Scissors.")
    print("")
    print("Rules:")
    print("Rock beats Scissors")
    print("Paper beats Rock")
    print("Scissors beats Paper")
    print("Type 'quit' at anytime to end the game")
    print("")

    while True:#Makes it an infinite loop until broken
      print("")
      turn = str(input("1! 2! 3! Shoot!: "))

      #Tie statement
      if turn == comp:
        print("")
        print("You played " + turn + " and the computer played " + comp + "...So it's a tie")
        ##########################
        comp = compChoice()

      #statements for computer = rock
      elif turn == "r":
        if comp == "s":
          print("")
          print("You played " + turn + " and the computer played " + comp + ". So you won!")
          ##########################
          comp = compChoice()
        elif comp == "p":
          print("")
          print("You played " + turn + " and the computer played " + comp + ". So you lost")
          ##########################
          comp = compChoice()

      #statements for computer = paper
      elif turn == "p":
        if comp == "s":
          print("")
          print("You played " + turn + " and the computer played " + comp + ". So you lost")
          ##########################
          comp = compChoice()
        elif comp == "r":
          print("")
          print("You played " + turn + " and the computer played " + comp + ". So you won!")
          ##########################
          comp = compChoice()

      #statements for computer = scissors
      elif turn == "s":
        if comp == "p":
          print("")
          print("You played " + turn + " and the computer played " + comp + ". So you won!")
          ##########################
          comp = compChoice()
        elif comp == "r":
          print("")
          print("You played " + turn + " and the computer played " + comp + ". So you lost")
          ##########################
          comp = compChoice()
      elif turn == "quit":
        print("")
        print("Aww:( Next time then.")
        break
      else:
        print("")
        print("Please pick 'r', 'p', or 's'")
  elif intro == "n":
    print("")
    print("Aww:( Next time then.")
  else:
    print("")
    print("Please choose either 'y' or 'n'")
    RPS()
RPS()
