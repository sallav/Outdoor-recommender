import sys
sys.path.append('../')

from recommender.recommender import Day
from recommender.recommender import day_evaluator as deval
import unittest

class test_day_evaluator(unittest.TestCase):

    def test_fairDays(self):
        d1 = Day.Day('Ke 2.3.', 'Poutaa', 5, 5)
        d2 = Day.Day('To 3.3.', 'Sateista', 4, 5)
        d3 = Day.Day('Pe 4.3.', 'Selkeää ja poutaa', 4, 5)
        list = [d1, d2, d3]
        fair = deval.day_evaluator().fairDays(list)
        self.assertTrue(2==len(fair))

    def test_clearDays(self):
        d1 = Day.Day('Ke 2.3.', 'Poutaa', 5, 5)
        d2 = Day.Day('To 3.3.', 'Sateista', 4, 5)
        d3 = Day.Day('Pe 4.3.', 'Selkeää ja poutaa', 4, 5)
        list = [d1, d2, d3]
        clear = deval.day_evaluator().clearDays(list)
        self.assertTrue(1==len(clear))        

    def test_halfCloudyDays(self):
        d1 = Day.Day('Ke 2.3.', 'Poutaa', 5, 5)
        d2 = Day.Day('To 3.3.', 'Melko pilvistä', 4, 5)
        d3 = Day.Day('Pe 4.3.', 'Selkeää ja poutaa', 4, 5)
        list = [d1, d2, d3]        
        hfcl = deval.day_evaluator().halfCloudyDays(list)
        self.assertTrue(len(hfcl)==1)

    def test_dayWithBestTemp(self):
        d1 = Day.Day('Ke 2.3.', 'Poutaa', -5, 5)
        d2 = Day.Day('To 3.3.', 'Melko pilvistä', 9, 5)
        d3 = Day.Day('Pe 4.3.', 'Selkeää ja poutaa', 6, 5)
        list = [d1, d2, d3]
        best = deval.day_evaluator().dayWithBestTemp(list, 8)
        self.assertEquals(best, d3)
        best = deval.day_evaluator().dayWithBestTemp(list, 10)
        self.assertEquals(best, d2)

    def test_removeWindyDays(self):
        d1 = Day.Day('Ke 2.3.', 'Poutaa', 5, 5)
        d2 = Day.Day('To 3.3.', 'Melko pilvistä', 9, 10)
        d3 = Day.Day('Pe 4.3.', 'Selkeää ja poutaa', 6, 12)
        list = [d1, d2, d3]
        mild = deval.day_evaluator().removeWindyDays(list, 10)
        self.assertTrue(2==len(mild))
        mild = deval.day_evaluator().removeWindyDays(list, 20)
        self.assertTrue(3==len(mild))
        mild = deval.day_evaluator().removeWindyDays(list, 5)
        self.assertTrue(1==len(mild))

if __name__=='__main__':
    unittest.main()
