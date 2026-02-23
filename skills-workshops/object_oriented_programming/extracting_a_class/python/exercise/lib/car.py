class Car:
  PASSENGER_LIMIT_DEFAULT = 4
  TOP_SPEED_DEFAULT = 120

  def __init__(self, config):
    self.top_speed = config['top_speed'] or self.TOP_SPEED_DEFAULT
    self.passenger_limit = config['passenger_limit'] or self.PASSENGER_LIMIT_DEFAULT
    self.speed = 0
    self.engine_on = False
    self.driver = None
    self.passengers = []

  def setDriver(self, person):
    if person.age < 18:
      raise Exception('Driver Age Error')
    else:
      self.driver = person


  def driver_name(self):
    if not self.driver:
      raise Exception('No Driver Error')
    else:
      return self.driver.first_name + " " + self.driver.last_name

  def turn_on_engine(self):
    if not self.driver:
      raise Exception('No Driver Error')
    else:
      self.engine_on = True

  def turn_off_engine(self):
    if not self.driver:
      raise Exception('No Driver Error')
    else:
      self.engine_on = False

  def accelerate(self, increment, seconds):
    if not self.engine_on:
      raise Exception('Engine Off Error')

    for i in range(seconds):
      if self.speed >= self.top_speed:
        break
      self.speed += increment

  def brake(self, seconds):
    if not self.engine_on:
      raise Exception('Engine Off Error')

    for i in range(seconds):
      if self.speed <= 1:
        break
      self.speed -= 1

  def add(self, passenger):
    if len(self.passengers) >= self.passenger_limit:
      raise Exception('Limit Reached Error')
    self.passengers.append(passenger)
