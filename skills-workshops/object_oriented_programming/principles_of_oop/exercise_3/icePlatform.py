# At the moment, this doesn't work. It's possible
# to fix it byintroducing one 'term'
# I.e. You don't even need a whole new line

from quiz import Quiz
from guessingGame import GuessingGame

class IcePlatform():
  def __init__(self):
    self.games = [Quiz(), GuessingGame()]

  # there is some type checking going on in this method
  # refactor this class along with Game and GuessingGame
  # to remove the need for type checking
  def playAll(self):
    for game in self.games:
      # check if the game is a Quiz
      if isinstance(game, Quiz):
        game.getPlayerName()
        game.questionOne()
        game.questionTwo()
        game.questionThree()
        game.questionFour()
        game.questionFive()
        game.printScore()
      # check if the game is a GuessingGame
      elif isinstance(game, GuessingGame):
        game.getPlayerName()
        while game.isNotOver():
          game.nextGuess()

platform = IcePlatform()
platform.playAll()
