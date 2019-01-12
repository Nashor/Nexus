import unittest
from nexus.nexus import Nexus

class TestNexus(unittest.TestCase):
   
   minfluence = 10
   maxfluence = 20
   radius = 10
   diffuse = 1
   
   def setUp(self):
      self.nexus = Nexus(
         self.minfluence,
         self.maxfluence,
         self.radius,
         self.diffuse
      )
   
   def test_minfluence(self):
      '''The influence at the radius of the Nexus should equal the minimum
      influence (minfluence) of the Nexus.'''
      self.assertEqual(
         self.minfluence,
         self.nexus.influence(dist=self.radius)
      )
   
   def test_maxfluence(self):
      '''The influence at the centre of the Nexus should equal the maximum
      influence (maxfluence) of the Nexus.'''
      self.assertEqual(
         self.maxfluence,
         self.nexus.influence(dist=0)
      )
   
   def test_noinfluence(self):
      '''The influence outside the radius of the Nexus should equal 0. The
      Nexus has no influence outside the radius.'''
      self.assertEqual(
         0,
         self.nexus.influence(dist=self.radius + 1)
      )

if __name__ == '__main__':
   unittest.main()
