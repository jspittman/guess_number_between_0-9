# a program to test infinate loops
# i is start
# j equals guess
# loopNum for number of tries
# m is random number

import time
from secrets import randbelow

i = 1
loopNum = 1
m = (randbelow(10))

#works
print ("Try to guess a number betwe1en 0 and 9 (you get 3 tries)")
time.sleep(.4)

#works
if i == 1:
  print ("")
  j = int(input("please type a value: "))

#works  
if j == m:
  print ("correct, that answer was ", m)
elif j != m:
  print ("wrong answer - try again")

while j != m:
  if loopNum < 3 and j != m:
    j = int(input("try to guess the number again: "))
    loopNum = loopNum + 1
    if j == m:
      print ("correct, that answer was ", m)
  else:
    print ("you lose")
    time.sleep(.4)
    print ("the answer was: ", m)
    j = m
