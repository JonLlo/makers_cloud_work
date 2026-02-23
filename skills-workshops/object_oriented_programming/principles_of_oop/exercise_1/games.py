from random import *

print("First we'll play a guessing game, then we'll do a quiz!")
input("Press return to start")
currentNumber = Random().randint(1, 10)
playerName = input("what is your name? ")
playerGuess = input("Please guess a number between 1 and 10 (inclusive)")
playerScore = 0

while int(playerGuess) != currentNumber:
  playerScore -= 1
  print(f"Nope, you lose 1 pt. Try again {playerName}!")
  playerGuess = input("Please guess a number between 1 and 10 (inclusive)")
print(f"Well done {playerName}, you guessed {playerGuess}, which was correct")
playerScore += 10

print(f"Your score so far is {playerScore}")

print("OK well done, now it's quiz time")
input("Press return to start")


answer1 = input("What is the capital Greenland?")
if answer1 == "Nuuk":
  print("correct, you scored 1pt")
  playerScore += 1
else:
  print("incorrect - nil points!")


answer2 = input("What is the largest planet in our Solar System?")
if answer2 == "Jupiter":
    print("correct, you scored 1pt")
    playerScore += 1
else:
    print("incorrect - nil points!")


answer3 = input("Who wrote the play 'Romeo and Juliet'?")
if answer3 == "William Shakespeare":
    print("correct, you scored 1pt")
    playerScore += 1
else:
    print("incorrect - nil points!")


answer4 = input("What is the chemical symbol for gold?")
if answer4 == "Au":
    print("correct, you scored 1pt")
    playerScore += 1
else:
    print("incorrect - nil points!")


answer5 = input("In which year did the Titanic sink?")
if answer5 == "1912":
    print("correct, you scored 1pt")
    playerScore += 1
else:
    print("incorrect - nil points!")

print(f"You scored {playerScore}")