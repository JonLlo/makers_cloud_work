class Quiz():

  def __init__(self):
    self.playerName = None
    self.playerScore = 0

  def printScore(self):
     print(f"You scored {self.playerScore}")

  def getPlayerName(self):
    self.playerName = input("what is your name? ")

  def updateScore(self, value):
    self.playerScore += value
  
  def questionOne(self):
    answer1 = input("What is the capital Greenland?")
    if answer1 == "Nuuk":
      print("correct, you scored 1pt")
      self.updateScore(1)
    else:
      print("incorrect - nil points!")
    
  def questionTwo(self):
    answer2 = input("What is the largest planet in our Solar System?")
    if answer2 == "Jupiter":
        print("correct, you scored 1pt")
        self.updateScore(1)
    else:
        print("incorrect - nil points!")

  def questionThree(self):
    answer3 = input("Who wrote the play 'Romeo and Juliet'?")
    if answer3 == "William Shakespeare":
        print("correct, you scored 1pt")
        self.updateScore(1)
    else:
        print("incorrect - nil points!")

  def questionFour(self):
    answer4 = input("What is the chemical symbol for gold?")
    if answer4 == "Au":
        print("correct, you scored 1pt")
        self.updateScore(1)
    else:
        print("incorrect - nil points!")

  def questionFive(self):
    answer5 = input("In which year did the Titanic sink?")
    if answer5 == "1912":
        print("correct, you scored 1pt")
        self.updateScore(1)
    else:
        print("incorrect - nil points!")
