import unittest
from nexus.nexus import Nexus
from nexus.database import Database

class TestDatabase(unittest.TestCase):
   
   def setUp(self):
      self.db = Database(':memory:')
   
   def test(self):
      self.assertEqual(True, True)

if __name__ == '__main__':
   unittest.main()
