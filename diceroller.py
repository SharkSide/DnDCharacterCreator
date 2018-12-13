from random import randint

results = []

for x in range(6):
  result = sum([randint(2,7) for y in range(4)])
  if result > 19:
    while result > 19:
      result = sum([randint(2,7) for y in range(4)])

  results.append(result)
  print("You rolled a {}".format(result))

print(results)

attribs = {0:"strength", 1:"dexterity", 2:"constitution", 3:"intelligence", 4:"wisdom", 5:"charisma"}
print("Available Attributes:")
for x, a in attribs.items():
  print("{0}: {1}".format(x, a))

end_attribs = {}

for n in results:
  print("What attribute do you wish to put {} into".format(n), end=": ")
  atrb = input("")
  if attribs[int(atrb)] in end_attribs:
    print("choose again")
  end_attribs[attribs[int(atrb)]] = n

print(n)

