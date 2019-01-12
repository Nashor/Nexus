from math import exp, log
from nexus.blocklocation import BlockLocation

class Nexus(BlockLocation):
   
   def __init__(self, minfluence, maxfluence, radius, diffuse):
      super().__init__(0, 0, 0, 'world')
      
      self.minfluence = minfluence
      self.maxfluence = maxfluence
      self.radius = radius
      self.radius2 = radius**2
      self.diffuse = diffuse
      
      self.a = maxfluence - minfluence + diffuse
      self.b = minfluence - diffuse
      self.c = (self.radius2) / log(diffuse / self.a)
   
   def influence(self, loc=None, dist=None, dist2=0):
      '''Returns the influence the Nexus has on a location. A distance, or
      distance squared can also be provided.
      
      This result of this function is based on the Gaussian function.
      '''
      if loc:
         dist2 = self.dist2(loc)
      elif dist:
         dist2 = dist**2
         
      if dist2 > self.radius2:
         return 0
      else:
         return self.a * exp(dist2 / self.c) + self.b

   def upkeep(self):
      pass
