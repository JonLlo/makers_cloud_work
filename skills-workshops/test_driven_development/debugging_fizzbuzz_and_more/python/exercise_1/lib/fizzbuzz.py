class FizzBuzz:
  def play(self, number):
    if self.is_divisible(number, 3):
      return "Buzz"
    elif self.is_divisible(number, 5):
      return "Fizz"
    elif self.is_divisible(number, 15):
      return "FizzBuzz"
    else:
      return number

  def is_divisible(self, dividend, divisor):
    return dividend % divisor == 0

  def play_until(self, limit):
    return [self.play(limit) for number in range(1,limit)]
