from lib.car import Car
from lib.person import Person

def test_setDriver_with_over_18():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 20})
  car.setDriver(person)
  assert car.driver == person

def test_setDriver_with_under_18():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 17})
  try:
    car.setDriver(person)
  except Exception as e:
    assert str(e) == 'Driver Age Error'

def test_driver_name_with_driver():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 20})
  car.setDriver(person)
  assert car.driver_name() == 'John Doe'

def test_driver_name_without_driver():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  try:
    car.driver_name()
  except Exception as e:
    assert str(e) == 'No Driver Error'

def test_turn_on_engine_with_driver():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 20})
  car.setDriver(person)
  car.turn_on_engine()
  assert car.engine_on == True

def test_turn_on_engine_without_driver():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  try:
    car.turn_on_engine()
  except Exception as e:
    assert str(e) == 'No Driver Error'

def test_turn_off_engine_with_driver():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 20})
  car.setDriver(person)
  car.turn_on_engine()
  car.turn_off_engine()
  assert car.engine_on == False

def test_turn_off_engine_without_driver():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 20})
  car.setDriver(person)
  car.turn_on_engine()
  car.person = None
  try:
    car.turn_off_engine()
  except Exception as e:
    assert str(e) == 'No Driver Error'

def test_accelerate_with_engine_off():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 20})
  car.setDriver(person)
  try:
    car.accelerate(3, 3)
  except Exception as e:
    assert str(e) == 'Engine Off Error'

def test_accelerate_with_engine_on():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 20})
  car.setDriver(person)
  car.turn_on_engine()
  car.accelerate(2, 5)
  assert car.speed == 10

def test_accelerate_with_top_speed():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 20})
  car.setDriver(person)
  car.turn_on_engine()
  car.accelerate(5, 40)
  assert car.speed <= 100

def test_brake_with_engine_off():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 20})
  car.setDriver(person)
  try:
    car.brake(3)
  except Exception as e:
    assert str(e) == 'Engine Off Error'

def test_brake_with_engine_on():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 20})
  car.setDriver(person)
  car.turn_on_engine()
  car.accelerate(5, 8)
  car.brake(3)
  assert car.speed == 37
  
def test_brake_with_negative_speed():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 20})
  car.setDriver(person)
  car.turn_on_engine()
  car.brake(100)
  assert car.speed >= 0

def test_add_with_passenger():
  car = Car({'top_speed': 100, 'passenger_limit': 4})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 20})
  car.add(person)
  assert person in car.passengers

def test_add_with_full_passenger():
  car = Car({'top_speed': 100, 'passenger_limit': 0})
  person = Person({'first_name': 'John', 'last_name': 'Doe', 'age': 20})
  try:
    car.add(person)
  except Exception as e:
    assert str(e) == 'Limit Reached Error'
