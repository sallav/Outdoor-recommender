import sys
sys.path.append('../')

from recommender.recommender import text_extractor
from recommender.recommender import Day
from recommender.recommender import scraper
from datetime import datetime
import unittest

class Test_text_extractor(unittest.TestCase):

    def test_getDay(self):
        extr = text_extractor.foreca_extractor()
        daytext = '</div><div class="day"><h5>Ke 9.3.</h5><div class="s"><img alt="Pilvistä ja poutaa" class="fluid"> Ylin: <span class="warm">+8</span><div class="ws"><em>4</em> m/s<div class="rain"><em>0,10</em> mm</div></div>'
        day = extr.getDay(daytext)
        self.assertEqual(day.getDate(), "Ke 9.3.")
        self.assertEqual(day.getDescription(), "Pilvistä ja poutaa")
        self.assertEqual(day.getWarmest(), 8)
        self.assertEqual(day.getWindSpeed(), 4)
        self.assertEqual(day.getRainFall(), 0.10)
 
    def test_getPart(self):
        extr = text_extractor.foreca_extractor()
        daytext = '</div><div class="day"><h5>Ke 9.3.</h5><img alt="Pilvistä ja poutaa" class="fluid"> Ylin: <span class="warm">+8</span><div class="ws"><em>4</em> m/s<img width="18"/><em>0,10</em> cm</div></div>'
        desc = extr.getPart(daytext, '<img alt="', '" class="fluid">')
        self.assertEqual("Pilvistä ja poutaa", desc)

    def test_hightemp(self):
        extr = text_extractor.foreca_extractor()
        daytext = '</div><div class="day"><h5>Ke 9.3.</h5><img alt="Pilvistä ja poutaa" class="fluid"> Ylin: <span class="warm">+8</span><div class="ws"><em>4</em> m/s<img width="18"/><em>0,10</em> cm</div></div>'
        temp = extr.hightemp(daytext)
        self.assertEqual(8, temp)
        daytext = '</div><div class="day"><h5>Ke 9.3.</h5><img alt="Pilvistä ja poutaa" class="fluid"> Ylin: <span class="cold">-8</span><div class="ws"><em>4</em> m/s<img width="18"/><em>0,10</em> cm</div></div>'
        temp = extr.hightemp(daytext)
        self.assertEqual(-8, temp)

    def test_warmthToInt(self):
        warmth = '+13d'
        extr = text_extractor.foreca_extractor()
        wint = extr.warmthToInt(warmth)
        self.assertEqual(13, wint)
        w = '-14refw'
        wint = extr.warmthToInt(w)
        self.assertEqual(-14, wint)
        w = '+8<'
        wint = extr.warmthToInt(w)
        self.assertEqual(8, wint)
        w = '-8aa'
        wint = extr.warmthToInt(w)
        self.assertEqual(-8, wint)
        w = '0f'
        wint = extr.warmthToInt(w)
        self.assertEqual(0, wint)

    def test_rainToFloat(self):
        extr = text_extractor.foreca_extractor()
        rain = 'jsaldijd<0,100jlkkasd'
        f = extr.rainToFloat(rain)
        self.assertTrue(f==0.100)


if __name__=='__main__':
    unittest.main()