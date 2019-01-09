from collections import namedtuple
from math import exp, log
import numpy as np
import matplotlib.pyplot as plt
import sqlite3

Coord = namedtuple('Coord', ['x', 'y', 'z'])

class Database:
   
   def __init__(self):
      self.conn = sqlite3.connect('nexus.db')
      self.c = self.conn.cursor()
      
      self.c.execute(
         '''
         CREATE TABLE IF NOT EXISTS nexus (
            x int NOT NULL,
            y int NOT NULL,
            z int NOT NULL,
            minfluence real,
            maxfluence real,
            radius real,
            diffuse real,
            CONSTRAINT id PRIMARY KEY (x, y, z)
         );
         '''
      )
      self.conn.commit()
   
   def clear(self):
      self.c.execute('DELETE FROM nexus')
      self.conn.commit()
   
   def get_nexus(self, coord):
      self.c.execute('SELECT * FROM nexus WHERE x=? AND y=? AND z=?', coord)
      tup = self.c.fetchone()
      
      nexus = Nexus(tup[3], tup[4], tup[5], tup[6])
      nexus.coord = Coord(tup[0], tup[1], tup[2])
      
      return nexus
   
   def put_nexus(self, nexus):
      self.c.execute(
         'INSERT INTO nexus VALUES (?,?,?,?,?,?,?)',
         (nexus.coord.x, nexus.coord.y, nexus.coord.z, nexus.minfluence,
          nexus.maxfluence, nexus.radius, nexus.diffuse)
      )
      self.conn.commit()

class Nexus:
   
   def __init__(self, minfluence, maxfluence, radius, diffuse):
      self.minfluence = minfluence
      self.maxfluence = maxfluence
      self.radius = radius
      self.radius2 = radius**2
      self.diffuse = diffuse
      self.coord = Coord(0, 0, 0)
      
      self.a = maxfluence - minfluence + diffuse
      self.b = minfluence - diffuse
      self.c = (radius**2) / log(diffuse / self.a)
   
   def dist2(self, coord):
      '''Returns the distance squared from the Nexus co-ordinate to the
      provided co-ordinate.
      
      The actual distance, which would be the square root of this result, is
      not required. The distance from the Nexus co-ordinate to the provided 
      co-ordinate is squared in the influence formula.'''
      return (
         (self.coord.x - coord.x)**2 + 
         (self.coord.y - coord.y)**2 + 
         (self.coord.z - coord.z)**2
      )
   
   def influence(self, dist=0, coord=None):
      '''Returns the influence the Nexus has on a co-ordinate. A distance can
      also be provided directly.'''
      if coord:
         d2 = self.dist2(coord)
      else:
         d2 = dist**2
         
      if d2 > self.radius2:
         return 0
      else:
         return self.a * exp(d2 / self.c) + self.b
      

def main():
   minfluence = 10
   maxfluence = 30
   radius = 20
   
   nexus1 = Nexus(minfluence, maxfluence, radius, 1)
   nexus1.coord = Coord(1, 2, 3)
   nexus2 = Nexus(minfluence, maxfluence, radius, 0.1)
   nexus2.coord = Coord(-3, 4, 7)
   nexus3 = Nexus(minfluence, maxfluence, radius, 5)
   
   for nexus in [nexus1, nexus2, nexus3]:
      assert nexus.influence(0) == maxfluence
      assert nexus.influence(radius) == minfluence
      assert nexus.influence(radius + 1) == 0
   
   db = Database()
   db.clear()
   db.put_nexus(nexus1)
   db.put_nexus(nexus2)
   db.put_nexus(nexus3)
   print(db.get_nexus(Coord(0, 0, 0)).diffuse)
   
   '''
   x = np.arange(0, radius + 2, 0.1)
   y1 = np.array([nexus1.influence(dist=xi) for xi in x])
   y2 = np.array([nexus2.influence(dist=xi) for xi in x])
   y3 = np.array([nexus3.influence(dist=xi) for xi in x])
   #y1 = np.array([nexus1.influence(coord=Coord(0,0,xi)) for xi in x])
   #y2 = np.array([nexus2.influence(coord=Coord(0,0,xi)) for xi in x])
   #y3 = np.array([nexus3.influence(coord=Coord(0,0,xi)) for xi in x])
   plt.plot(x, y1)
   plt.plot(x, y2)
   plt.plot(x, y3)
   plt.legend(['Nexus1', 'Nexus2', 'Nexus3'])
   plt.show()
   '''

if __name__ == '__main__':
   main()
