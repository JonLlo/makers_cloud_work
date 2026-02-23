from lib.fizzbuzz import FizzBuzz

def test_play_given_1_returns_1():
  fizzBuzz = FizzBuzz()
  actual = fizzBuzz.play(1)
  expected = 1
  assert actual == expected

def test_play_given_15_returns_FuzzBuzz():
  fizzBuzz = FizzBuzz()
  actual = fizzBuzz.play(15)
  expected = "FizzBuzz"
  assert actual == expected

def test_play_given_5_returns_Buzz():
  fizzBuzz = FizzBuzz()
  actual = fizzBuzz.play(5)
  expected = "Buzz"
  assert actual == expected

def test_play_given_3_returns_Fizz():
  fizzBuzz = FizzBuzz()
  actual = fizzBuzz.play(3)
  expected = "Fizz"
  assert actual == expected

def test_is_divisible_returns_true_for_3_and_3():
  fizzBuzz = FizzBuzz()
  actual = fizzBuzz.is_divisible(3,3)
  expected = True
  assert actual == expected

def test_is_divisible_returns_false_for_1_and_3():
  fizzBuzz = FizzBuzz()
  actual = fizzBuzz.is_divisible(1,3)
  expected = False
  assert actual == expected

def test_play_until_returns_sequence_to_limit():
  fizzBuzz = FizzBuzz()
  actual = fizzBuzz.play_until(3)
  expected = [1,2,"Fizz"]
  assert actual == expected

