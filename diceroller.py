from random import randint

results = []

for x in  range(int(input('How many dicesets: '))):
  diceset = []
  for y in range(4):
    diceset.append(randint(2,7))

  result = sum(diceset)
  results.append(result)
  print("You rolled a {}".format(result))

