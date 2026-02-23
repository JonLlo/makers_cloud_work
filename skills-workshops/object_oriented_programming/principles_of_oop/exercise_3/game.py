class Game:
  def __init__(self):
    self.playerName = None
    self.playerScore = 0

  def getPlayerName(self):
    self.playerName = input("what is your name? ")

  def updateScore(self, value):
    self.playerScore += value
  
  # is there anything else you can move here?
