import sys
sys.path.append('../')

import py_compile
from recommender.recommender import Day
from recommender.recommender import Day_comparer as comp
from recommender.recommender import day_evaluator
import unittest

class test_day_comparer(unittest.TestCase):

    def test_chooseBetter(self):
        cmp = comp.Day_comparer(maxtemp=25, maxwind=15)
        lst1 = ['Selkeää', 'Poutaa', 'Selkeää ja poutaa']
        lst2 = ['Selkeää', 'Puolipilvistä', 'Sateista', 'Sateista']
        lst3 = ['Puolipilvistä', 'Sateista', 'Puolipilvistä']
        lst4 = ['Sateista', 'Sateista']
        self.assertTrue(len(cmp.chooseBetter(lst1, lst2))==3)
        self.assertEqual(cmp.chooseBetter(lst1, lst2), lst1)
        self.assertTrue(len(cmp.chooseBetter(lst2, lst3))==4)
        self.assertTrue(len(cmp.chooseBetter(lst1, lst4))==3)
        self.assertTrue(len(cmp.chooseBetter(lst4, lst1))==2)
        self.assertTrue('Selkeää' in cmp.chooseBetter(lst2, lst3))
        self.assertTrue('Puolipilvistä' in cmp.chooseBetter(lst3, lst1))

    def test_chooseFromBoth(self):
        cmp = comp.Day_comparer(maxtemp=25, maxwind=15)
        lst1 = ['Selkeää', 'Poutaa', 'Selkeää ja poutaa']
        lst2 = ['Selkeää', 'Puolipilvistä', 'Sateista', 'Sateista']
        lst3 = ['Puolipilvistä', 'Sateista', 'Puolipilvistä']
        lst4 = ['Sateista', 'Sateista']
        self.assertTrue(len(cmp.chooseFromBoth(lst1, lst2))==1)
        self.assertEqual(cmp.chooseFromBoth(lst1, lst2), ['Selkeää'])
        self.assertTrue(len(cmp.chooseFromBoth(lst2, lst3))==2)
        self.assertTrue(len(cmp.chooseFromBoth(lst1, lst4))==3)
        self.assertTrue(len(cmp.chooseFromBoth(lst4, lst1))==1)
        self.assertTrue('Sateista' in cmp.chooseFromBoth(lst2, lst3))
        self.assertTrue('Puolipilvistä' in cmp.chooseFromBoth(lst3, lst2))

    def test_bestDay(self):
        cmp = comp.Day_comparer(maxtemp=25, maxwind=15)
        d1 = Day.Day('Ke 2.3. ', 'Poutaa', 9, 5)
        d2 = Day.Day('To 3.3.', 'Puolipilvistä ja sateista', 4, 5)
        d3 = Day.Day('Pe 4.3.', 'Selkeää ja poutaa', 3, 5)
        d4 = Day.Day('La 5.3.', 'Selkeää', 4, 6)
        d5 = Day.Day('Su 6.3.', 'Selkeää ja poutaa', 8, 5) 
        d6 = Day.Day('Ma 7.3.', 'Selkeää ja poutaa', 9, 20)
        self.assertEqual(d5, cmp.bestDay([d1, d2, d3, d4, d5, d6])) 
        d7 = Day.Day('Ti 8.3.', 'Puolipilvistä ja poutaa', 4, 6)
        d8 = Day.Day('Ke 9.3.', 'Puolipilvistä ja poutaa', 30, 6)
        self.assertEqual(d1, cmp.bestDay([d1, d2, d7, d8]))
        self.assertEqual(d7, cmp.bestDay([d2, d7, d8]))

    def test_clearAndFairs(self):
        cmp = comp.Day_comparer(maxtemp=25, maxwind=15)
        d1 = Day.Day('Ke 2.3. ', 'Poutaa', 5, 5)
        d2 = Day.Day('To 3.3.', 'Puolipilvistä ja sateista', 4, 5)
        d3 = Day.Day('Pe 4.3.', 'Selkeää ja poutaa', 3, 5)
        d4 = Day.Day('La 5.3.', 'Selkeää', 4, 6)
        d5 = Day.Day('Su 6.3.', 'Puolipilvistä', -1, 5)
        self.assertTrue(len(cmp.clearAndFairs([d1, d2, d5]))==1)
        self.assertEqual(cmp.clearAndFairs([d1, d2, d5]), [d1])
        self.assertTrue(len(cmp.clearAndFairs([d3, d4, d5]))==1)
        self.assertEqual(cmp.clearAndFairs([d3, d4, d5]), [d3])
        self.assertTrue(len(cmp.clearAndFairs([d1, d3, d5]))==1)
        self.assertEqual(cmp.clearAndFairs([d1, d3, d5]), [d3])
        d6 = Day.Day('Ma 7.3.', 'Puolipilvistä ja poutaa', 1, 1)
        d7 = Day.Day('Ti 8.3.', 'Puolipilvistä ja poutaa', 1, 2)
        self.assertTrue(len(cmp.clearAndFairs([d2, d5, d6, d7]))==2)
        self.assertTrue(d6 in cmp.clearAndFairs([d2, d5, d6, d7]))
        self.assertTrue(d7 in cmp.clearAndFairs([d2, d5, d6, d7]))
        d8 = Day.Day('Ke 9.3.', 'Selkeää ja poutaa', 2, 5)
        self.assertTrue(len(cmp.clearAndFairs([d1, d3, d4, d8]))==2)
        self.assertTrue(d3 in cmp.clearAndFairs([d1, d3, d4, d8]))
        self.assertTrue(d8 in cmp.clearAndFairs([d1, d3, d4, d8]))


if __name__=='__main__':
    unittest.main()