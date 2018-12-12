from random import randint


for x in  range(int(input('How many dicesets: '))):
  diceset = []
  for y in range(4):
    diceset.append(randint(2,7))

  result = sum(diceset)
  print("You rolled a {}".format(result))

