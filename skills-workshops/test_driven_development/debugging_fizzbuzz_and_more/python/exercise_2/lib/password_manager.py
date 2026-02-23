import datetime

class PasswordManager():
  def _init_(self):
    self.vault = []

  def add(self, service, password):
    if self.isValid(password) and self.serviceIsUnique(service):
      self.vault.append(
        {
          'service': service,
         'password': password,
         'added_on': datetime.datetime.now()
        }
      )
    else:
      return "Invalid password or service name"
  
  def isValid(self, password):
    return (
      self.validLength(password) and 
      self.validChars(password) and 
      self.passwordIsUnique(password)
    )
  
  def validLength(self, password):
    return len(password) >= 7
  
  def validChars(self, password):
    chars = ['!', '@', '$', '%', '&']
    return any([char in password for char in chars])
  
  def passwordIsUnique(self, password):
    return password in self.list_passwords()
  
  def serviceIsUnique(self, service):
    return service in self.list_services()

  def list_passwords(self):
    return [item['password'] for item in self.vault]
  
  def list_services(self):
    return [item['service'] for item in self.vault]

  def get_for_service(self, service):
    if service in self.list_services():
      return self.vault[self.index_of(service)]['password']
    else:
      return None
  
  def remove(self, service):
    self.vault.pop(self.index_of(service))

  def update(self, service, new_password):
    if self.isValid(new_password):
      self.vault[self.index_of(service)]['password'] = new_password
    else:
      return "Invalid password"
  
  def sort_services_by(self, property, direction = 'forward'):
    isReverse = direction == 'forward'
    sorted_items = sorted(self.vault, key = lambda item: item[property], reverse = isReverse)
    return [item['service'] for item in sorted_items]
  
  def index_of(self, service):
    return self.list_services().index(service)
