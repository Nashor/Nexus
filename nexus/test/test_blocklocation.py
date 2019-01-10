import unittest
from random import shuffle
from nexus.blocklocation import BlockLocation

class TestBlockLocation(unittest.TestCase):
   
   def setUp(self):
      self.bllist = [
         BlockLocation(0, 0, 0, 'world'),
         BlockLocation(0, 0, 1, 'world'),
         BlockLocation(0, 1, 0, 'world'),
         BlockLocation(0, 1, 1, 'world'),
         BlockLocation(1, 0, 0, 'world'),
         BlockLocation(1, 0, 1, 'world'),
         BlockLocation(1, 1, 0, 'world'),
         BlockLocation(1, 1, 1, 'world')
      ]
   
   def test_sorted(self):
      '''The list, which is already in sorted order, should not change order
      when it is sorted again.'''
      self.assertEqual(
         self.bllist,
         sorted(self.bllist)
      )
   
   def test_randomsorted(self):
      '''The list is randomized and then sorted once again. The final result
      should be the same as the original sorted list.'''
      rand_bllist = self.bllist.copy()
      shuffle(rand_bllist) # Randomize the order of the copied list
      
      self.assertEqual(
         self.bllist,
         sorted(rand_bllist)
      )

if __name__ == '__main__':
   unittest.main()
