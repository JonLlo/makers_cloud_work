from lib.cipher import Cipher

def test_encoding_hello_with_qwerty_key():
  cipher = Cipher()
  actual = cipher.encode("hello", "qwerty")
  expected = [12, 2, 16, 16, 19]
  assert actual == expected

def test_decoding_encoded_hello_with_qwerty_key():
  cipher = Cipher()
  actual = cipher.decode([12, 2, 16, 16, 19], "qwerty")
  expected = "hello"
  assert actual == expected

def test_encoding_encoded_hello_everyone_with_qwerty_key():
  cipher = Cipher()
  actual = cipher.encode("hello everyone", "qwerty")
  expected = [12, 2, 16, 16, 19, 26, 2, 23, 2, 3, 5, 19, 18, 2]
  assert actual == expected

def test_decoding_encoded_hello_everyone_with_qwerty_key():
  cipher = Cipher()
  actual = cipher.decode([12, 2, 16, 16, 19, 26, 2, 23, 2, 3, 5, 19, 18, 2], "qwerty")
  expected = "hello everyone"
  assert actual == expected
