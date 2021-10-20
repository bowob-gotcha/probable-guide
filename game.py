from random import randrange
x = randrange(999)
while True:
  r = int(input())
  if x==r:
    print("BINGO BABY")
    break
  print("SMALLER BRO" if (x < r) else "BIGGER BRO")
