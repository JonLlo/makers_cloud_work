from random import *

class GuessingGame():

  def __init__(self):
    self.playerName = None
    self.currentNumber = Random().randint(1, 10)
    self.gameOver = False
    self.playerScore = 0

  def updateScore(self, value):
    self.playerScore += value

  def isNotOver(self):
    return not self.gameOver

  def getPlayerName(self):
    self.playerName = input("what is your name? ")
    
  def nextGuess(self):
    playerGuess = input("Please guess a number between 1 and 10 (inclusive)")
    if int(playerGuess) == self.currentNumber:
      self.updateScore(10)
      print(f"Well done, you guessed {playerGuess}, which was correct")
      print(f"You scored {self.playerScore}")
      self.gameOver = True
    else:
      print(f"Nope, you lose 1 pt. Try again {self.playerName}!")
      self.updateScore(-1)
