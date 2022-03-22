import sys
sys.path.append('../')

from recommender.recommender import Day
import unittest

class test_day(unittest.TestCase):

    def test_warmer(self):
        day1 = Day.Day("Pe 4.3.", "Selkeää ja poutaa", +5, 20)
        day2 = Day.Day("To 3.3.", "Melko pilvistä", -1, 21)
        self.assertTrue(day1.warmer(day2))
        self.assertFalse(day2.warmer(day1))

    def test_clear(self):
        day1 = Day.Day("Pe 4.3.", "Selkeää ja poutaa", +5, 20)
        self.assertTrue(day1.clear())

    def test_fair(self):
        day1 = Day.Day("Pe 4.3.", "Selkeää ja poutaa", +5, 20)
        self.assertTrue(day1.fair())      

    def test_halfCloudy(self):
        day = Day.Day("To 3.3.", "Sateista ja melko pilvistä", -2, 5)
        self.assertTrue(day.halfCloudy())  

    def test_toString(self):
        day = Day.Day("To 3.3.", "Sateista ja melko pilvistä", -2, 5)
        st = day.toString()
        self.assertTrue("To 3.3." in st)
        self.assertTrue("Sateista ja melko pilvistä" in st)
        self.assertTrue("-2" in st)
        self.assertTrue("5" in st)

    def test_rate(self):
        pass

if __name__=='__main__':
    unittest.main()
