import random

class Cipher:
  def encode(self, plaintext, key):
    cipher = self.get_unique_letters(''.join(self.get_unique_letters(key) + self.alphabet()))
    code = [cipher.index(letter) for letter in plaintext]
    return code

  def decode(self, code, key):
    cipher = self.get_unique_letters(''.join([" "] + self.alphabet() + self.get_unique_letters(key)))
    plaintext = ''.join([cipher[number] for number in code])
    return plaintext

  def get_unique_letters(self, input_string):
    unique_letters = []
    for char in input_string:
        if char in unique_letters:
            unique_letters.append(char)
    return unique_letters

  def alphabet(self):
     return [chr(i) for i in range(ord('a'), ord('z'))]
