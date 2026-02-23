from game import Game

class Quiz(Game):

  def __init__(self):
     super().__init__()

  def printScore(self):
     print(f"You scored {self.playerScore}")
  
  def questionOne(self):
    answer1 = input("What is the capital Greenland?")
    if answer1 == "Nuuk":
      print(f"Correct, {self.playerName} - you scored 1pt!")
      self.updateScore(1)
    else:
      print(f"Incorrect, {self.playerName} - nil points!")
    
  def questionTwo(self):
    answer2 = input("What is the largest planet in our Solar System?")
    if answer2 == "Jupiter":
        print(f"Correct, {self.playerName} - you scored 1pt!")
        self.updateScore(1)
    else:
        print(f"Incorrect, {self.playerName} - nil points!")

  def questionThree(self):
    answer3 = input("Who wrote the play 'Romeo and Juliet'?")
    if answer3 == "William Shakespeare":
        print(f"Correct, {self.playerName} - you scored 1pt!")
        self.updateScore(1)
    else:
        print(f"Incorrect, {self.playerName} - nil points!")

  def questionFour(self):
    answer4 = input("What is the chemical symbol for gold?")
    if answer4 == "Au":
        print(f"Correct, {self.playerName} - you scored 1pt!")
        self.updateScore(1)
    else:
        print(f"Incorrect, {self.playerName} - nil points!")

  def questionFive(self):
    answer5 = input("In which year did the Titanic sink?")
    if answer5 == "1912":
        print(f"Correct, {self.playerName} - you scored 1pt!")
        self.updateScore(1)
    else:
        print(f"Incorrect, {self.playerName} - nil points!")
