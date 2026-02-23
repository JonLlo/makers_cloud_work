from random import *
from game import Game

class GuessingGame(Game):

  def __init__(self):
    self.currentNumber = Random().randint(1, 10)
    self.gameOver = False
    super().__init__()

  def isNotOver(self):
    return not self.gameOver
  
  def printScore(self):
    print(f"You scored {self.playerScore}")
    
  def nextGuess(self):
    playerGuess = input("Please guess a number between 1 and 10 (inclusive)")
    if int(playerGuess) == self.currentNumber:
      self.updateScore(10)
      print(f"Well done {self.playerName}, you guessed {playerGuess}, which was correct")
      self.printScore()
      self.gameOver = True
    else:
      self.updateScore(-1)
      print(f"Nope, you lose 1 pt. Try again {self.playerName}!")
