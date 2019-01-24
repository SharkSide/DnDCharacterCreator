import game.affects as affects
import game.units as units
import game.evaluators as evals


class Spell(object):
  def __init__(self, description, affect):
      self.description = description
      self.affect = affect
      self.input = self.affect.getInput()
      self.range = evals.EvaluateViewDist
      self.entityfilter = self.affect.getEntityFilter()
  
  def cast(self, caster, game):
    entities = []
    if isinstance(self.range, function):
      entities = game.getEntitiesInRangeOfPlayer(caster, self.range(caster))
    
    else:
      entities = game.getEntitiesInRangeOfPlayer(caster, self.range)
    
    filtered = []
    for e in entities:
      if self.entityfilter(e):
        filtered.append(e)
    
    for ef in filtered: ef.applyAffect(self.affect(self.input(caster, game)))
    
  def setRange(self, range):
    self.range = range
  
  def getSpellStats(self, getDesc = False):
    if getDesc:
      print(self.description)
    
    print("Affect Range: {}".format(self.range.readableformat()))
    print("Affect Input: {}".format(self.input.readableformat()))
    print("Affect Special Info: {}".format(self.affect.getSpecialInfo().readableformat()))
    
  def setInput(self, input):
    self.input = input
  
  def setFilter(self, filter):
    self.entityfilter = filter

    
    
    
