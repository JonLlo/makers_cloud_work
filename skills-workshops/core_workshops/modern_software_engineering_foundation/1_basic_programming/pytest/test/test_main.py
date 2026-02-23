from lib.main import *

# N.B. these tests are all correctly written - if there's any problem, it's in our code...

def test_return_simple_string():
    assert return_simple_string() == "foo", "returns the string \"foo\""

def test_return_another_string():
    assert return_another_string() == "abcdefghijk", "returns letters in the alphabet up to and including k"

def test_return_simple_integer():
    assert return_simple_integer() == 5, "returns the integer 5"

def test_make_and_return_simple_dictionary():
    assert make_and_return_simple_dictionary("mykey", "myvalue") == {"mykey": "myvalue"}, "takes two arguments, uses the 1st as a key and 2nd as a value"

def test_make_and_return_complex_dictionary():
    assert make_and_return_complex_dictionary(["greeting", "name", "role"], ["hello", "Paul", "coach"]) == {"greeting":"hello", "name":"Paul", "role":"coach"}, "convert two lists into key-value pairs in a dictionary"

def test_triangle_number():
    assert triangle_number(5) == 15, "the triangle number of 5 is 15 from 5+4+3+2+1=15"
    assert triangle_number(0) == 0, "the triangle number of 0 is a special case, returning 0"

def test_sort_this_list():
    assert sort_this_list([]) == [], "sorting an empty list returns an empty list"

def test_check_for_chocolate_cakes():
    assert check_for_chocolate_cakes(["chocolate fudge", "vanilla"]) == True, "chocolate fudge is chocolate based so return True"
    assert check_for_chocolate_cakes(["vanilla", "ube"]) == False, "no cakes with chocolate so return False"
    assert check_for_chocolate_cakes(["ube", "lemon drizzle", "white chocolate"]) == True, "white chocolate is chocolate based and is last cake in list, return True"

def test_check_password_manager():
    pm = PasswordManager()
    assert pm.pwd == {}, "check its password dictionary is initially empty"
    assert pm.get_for_service("unknown") == None, "getting password for unknown service returns None"
    pm.add("boogle", "12345678!")
    assert pm.pwd == {"boogle": "12345678!"}, "check one service with valid password is added to dictionary"
    assert pm.get_for_service("boogle") == "12345678!", "get password for known service"
    pm.add("placebook", "1234")
    assert pm.get_for_service("placebook") == None, "invalid password means service isn't added"
    pm.add("placebook", "12345678@")
    pm.update("placebook", "@87654321")
    assert pm.get_for_service("placebook") == "@87654321", "password can be updated"
    assert pm.list_services() == ["boogle", "placebook"], "both added and updated service are listed"