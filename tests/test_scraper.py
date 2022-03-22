import sys
sys.path.append('../')

from recommender.recommender.scraper import scraper
from recommender.recommender.Day import Day
import unittest
from datetime import datetime

class test_scraper(unittest.TestCase):

    def test_ses(self):
        sc = scraper()
        responce = sc.ses('https://www.foreca.fi/Finland/Helsinki/10vrk')
        self.assertIsNotNone(responce)

    def test_getDays(self):
        sc = scraper()
        url = "https://www.foreca.fi/Finland/Helsinki/10vrk"
        content = sc.ses(url)
        days = sc.getDays(content)
        print(len(days))
 #       self.assertTrue(len(days)==10)
        self.assertTrue(isinstance(days[0], Day))
        self.assertTrue(isinstance(days[8], Day))
        self.assertTrue(isinstance(days[4].getDate(), str))
        self.assertTrue(isinstance(days[4].getDescription(), str))
        self.assertTrue(isinstance(days[4].getWarmest(), int))
        self.assertTrue(isinstance(days[4].getWindSpeed(), int))

    def test_getDays2(self):
        scrpr = scraper()
        url = "https://www.foreca.fi/Finland/Helsinki/10vrk"
        page = scrpr.ses(url)
        days = scrpr.getDays(page)
        now = datetime.now()
        today = "{}.{}.".format(now.day, now.month)
  #      self.assertTrue(len(days)==10)
        self.assertTrue(today in days[0].getDate())


if __name__=='__main__':
    unittest.main()
