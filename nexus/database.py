import sqlite3
from nexus.nexus import Nexus

class Database:
   
   def __init__(self, dbname):
      self.dbname = dbname
      self.conn = sqlite3.connect(dbname)
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
