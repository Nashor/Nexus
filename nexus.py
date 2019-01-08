from math import exp, log
import numpy as np
import matplotlib.pyplot as plt

class Nexus:
   
   def __init__(self, minfluence, maxfluence, radius):
      self.minfluence = minfluence
      self.maxfluence = maxfluence
      self.radius = radius
      
      self.diffuse = -(radius * radius) / log(minfluence / maxfluence)
   
   def influence(self, dist):
      if dist > self.radius:
         return 0
      else:
         return self.maxfluence * exp(-(dist * dist) / self.diffuse)

class Nexus2:
   
   def __init__(self, minfluence, maxfluence, radius):
      self.minfluence = minfluence
      self.maxfluence = maxfluence
      self.radius = radius
      
      self.diffuse = -(radius * radius) / log(.1 / maxfluence)
   
   def influence(self, dist):
      if dist > self.radius:
         return 0
      else:
         return (self.maxfluence - self.minfluence + 1) * exp(-(dist * dist) / self.diffuse) + (self.minfluence - 1)

class Nexus3:
   
   def __init__(self, minfluence, maxfluence, radius, diffuse):
      self.minfluence = minfluence
      self.maxfluence = maxfluence
      self.radius = radius
      self.diffuse = diffuse
      
      self.a = maxfluence - minfluence + diffuse
      self.b = minfluence - diffuse
      self.c = (radius * radius) / log(diffuse / self.a)
   
   def influence(self, dist):
      if dist > self.radius:
         return 0
      else:
         return self.a * exp((dist * dist) / self.c) + self.b

def main():
   minfluence = 10
   maxfluence = 30
   radius = 20
   
   nexus = Nexus(minfluence, maxfluence, radius)
   nexus2 = Nexus2(minfluence, maxfluence, radius)
   nexus3 = Nexus3(minfluence, maxfluence, radius, 0.01)
   
   assert nexus.influence(0) == maxfluence
   assert nexus3.influence(0) == maxfluence
   assert nexus.influence(radius) == minfluence
   assert nexus3.influence(radius) == minfluence
   assert nexus.influence(radius + 1) == 0
   assert nexus3.influence(radius + 1) == 0
   
   x = np.arange(0, radius + 2, 0.1)
   y1 = np.array([nexus.influence(xi) for xi in x])
   y2 = np.array([nexus2.influence(xi) for xi in x])
   y3 = np.array([nexus3.influence(xi) for xi in x])
   plt.plot(x, y1)
   plt.plot(x, y2)
   plt.plot(x, y3)
   plt.legend(['Nexus', 'Nexus2', 'Nexus3'])
   plt.show()

if __name__ == '__main__':
   main()
