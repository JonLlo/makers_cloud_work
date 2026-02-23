# A1: Given the input string
# 
# "Here is a string Paul wrote. It has CAPITAL letters in it... Wow."
# 
# print out all the capital letters from that string.

s = "Here is a string Paul wrote. It has CAPITAL letters in it... Wow."

# Let's use string
import string

# We can use the REPL to check what this returns
uppers = string.ascii_uppercase

for c in s:
    if c in uppers:
        print(c)
