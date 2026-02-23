def return_simple_string():
    return "bar"








































def return_another_string():
    return "abcdefghjik"








































def return_simple_intager():
    return 5








































def make_and_return_simple_dictionary(key, value):
    return "{" + key + ": " + value + "}"








































def make_and_return_complex_dictionary(keys, values):
    my_dict = {}
    for i in range(len(keys)):
        my_dict[keys[i]] = values[i]
    my_dict["background"] = "testing"
    del(my_dict["name"])
    return my_dict








































def triangle_number(n):
    answer = n
    while True:
        n -= 1
        answer += n
        if n < 1:
            break
    return answer








































def sort_this_list(mylist):
    return mylist.sort()








































def check_for_chocolate_cakes(cake_list):
    for cake in cake_list:
        if "chocolate" in cake.lower():
            return True
        else:
            return False








































class PasswordManager():
    def __init__(self):
        self.pwd = {}
    def __is_valid(self, password):
        return (len(password) > 7 and any(char in "!@$%&" for char in password))
    def add(self, service, password):
        if __is_valid(password):
            self.pwd[service] = password
    def update(self, service, password):
        self.add(service, password)
    def list_services(self):
        return self.pwd.keys()
    def get_for_service(self, service):
        return self.pwd.get(service)
