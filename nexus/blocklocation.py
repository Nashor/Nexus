class BlockLocation:
   
   def __init__(self, x, y, z, world):
      self.x = x
      self.y = y
      self.z = z
      self.world = world
   
   def compare(self, other):
      if self.x == other.x:
         if self.y == other.y:
            return self.z - other.z
         else:
            return self.y - other.y
      else:
         return self.x - other.x
   
   def __lt__(self, other):
      return self.compare(other) < 0
   
   def __gt__(self, other):
      return self.compare(other) > 0
   
   def __eq__(self, other):
      return self.compare(other) == 0
   
   def __le__(self, other):
      return self.compare(other) <= 0
   
   def __ge__(self, other):
      return self.compare(other) >= 0
   
   def __ne__(self, other):
      return self.compare(other) != 0
   
   def __repr__(self):
      return '[{},{},{}]({})'.format(self.x, self.y, self.z, self.world)
