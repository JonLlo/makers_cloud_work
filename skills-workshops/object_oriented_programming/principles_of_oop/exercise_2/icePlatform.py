from quiz import Quiz
from guessingGame import GuessingGame

class IcePlatform():
  def __init__(self):
    self.games = [Quiz(), GuessingGame()]

  def playAll(self):
    for game in self.games:
      if isinstance(game, Quiz):
        game.getPlayerName()
        game.questionOne()
        game.questionTwo()
        game.questionThree()
        game.questionFour()
        game.questionFive()
        game.printScore()
      elif isinstance(game, GuessingGame):
        game.getPlayerName()
        while game.isNotOver():
          game.nextGuess()

platform = IcePlatform()
platform.playAll()
