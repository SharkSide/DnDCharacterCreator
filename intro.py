r = 0
while r == 0:
  print("What race will you be?")
  race = input().capitalize()
  if race == "Dragonborn":
    print("Dragonbord selected")
    r = 1
  elif race == "Dwarf":
    print("Dwarf selected")
    r = 1.
  elif race == "Elf":
    print("Elf selected")
    r = 1
  elif race == "Gnome":
    print("Gnome selected")
    r = 1
  elif race == "Half Elf":
    print("Half Elf selected")
    r = 1
  elif race == "Half Orc":
    print("Half Orc selected")
    r = 1
  elif race == "Halfling":
    print("Halfling selected")
    r = 1
  elif race == "Human":
    print("Human selected")
    r = 1
  elif race == "Tiefling":
    print("Tiefling selected")
    r = 1
  else:
    print("That is not an accepted race")
c = 0
while c == 0:
  print("What class will you be?")
  job = input().capitalize()
  if job == "Barbarian":
    print("Barbarian selected")
    c = 1
  elif job == "Bard":
    print("Bard selected")
    c = 1
  elif job == "Cleric":
    print("Cleric selected")
    c = 1
  elif job == "Druid":
    print("Druid selected")
    c = 1
  elif job == "Monk":
    print("Monk selected")
    c = 1
  elif job == "Paladin":
    print("Paladin selected")
    c = 1
  elif job == "Ranger":
    print("Ranger selected")
    c = 1
  elif job == "Rogue":
    print("Rogue selected")
    c = 1
  elif job == "Sorcerer":
    print("Sorcerer selected")
    c = 1
  elif job == "Warlock":
    print("Warlock selected")
    c = 1
  elif job == "Wizard":
    print("Wizard selected")
    c = 1
  else:
    print("That is not an accepted class")
a = 0
while a == 0:
  print("What allignment will you be?")
  at = input()
  if at == "Lawfull Good":
    print("Lawfull Good selected")
    a = 1
  elif at == "Neutral Good":
    print("Neutral Good selected")
    a = 1
  elif job == "Chaotic Good":
    print("Chaotic Good selected")
    a = 1
  elif at == "Lawfull Neutral":
    print("Lawfull Neutral selected")
    a = 1
  elif at == "Neutral":
    print("Neutral selected")
    a = 1
  elif at == "Chaotic Neutral":
    print("Chaotic Neutral selected")
    a = 1
  elif at == "Lawfull Evil":
    print("Lawfull Evil selected")
    a = 1
  elif at == "Neutral Evil":
    print("Neutral Evil selected")
    a = 1
  elif at == "Chaotic Evil":
    print("Chaotic Evil selected")
    a = 1
  else:
    print("That is not an accepted allignment")
l = 0

def numeric(inp):
  try: int(inp)
  except: return False
  return True

while l == 0:
  print("What level is the character?")
  level = input()
  if numeric(level):
    if int(level)> 0:
      print("Character Level", level)
      l = 1
    else:
      print("That is not a level")
  
  else:
    print("That is not a level")
