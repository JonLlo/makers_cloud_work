# A2: What are the divisors of 111?
# 
# N.B. the divisors of a number are those that leave an integer when the number
# is divided i.e. 6's divisors are 1, 2, 3 and 6.

n = 111
c = 0
while c <= n:
    c += 1
    if n % c == 0:
        print(c)
