import sys
sys.path.append('../')

import re
from recommender.recommender.Day import Day
from bs4 import BeautifulSoup

class foreca_extractor:

    @staticmethod
    def getDay(days_text):                  # returns a Day object extracted from a section of page
        try:
            day = Day()                 
            soup = BeautifulSoup(days_text, 'html.parser')
#            date = foreca_extractor.getPart(days_text, '<h5>', '</h5>')
#            description = foreca_extractor.getPart(days_text, '<div class="s"><img alt="', '" class="fluid"')
#            windspeed = int(foreca_extractor.getPart(days_text, '<div class="ws"><em>', '</em> m/s'))
#            rainstr = foreca_extractor.getPart(days_text, '/><em>', '</em> mm')
            day.setDate(foreca_extractor.getDate(soup))                                       # Set date
            day.setDesc(foreca_extractor.getDescription(soup))                                # Set description of days weather
            day.setWarmest(foreca_extractor.hightemp(days_text))                              # Set highest temperature of the day
            day.setWindSpeed(int(foreca_extractor.getWindSpeed(soup)))                        # Set wind speed
            rain = foreca_extractor.rainToFloat(foreca_extractor.getRain(soup))
            day.setRainFall(rain)
            day.rate()
            return day
        except Exception as e:
            print("Error creating Day: {}".format(e))
            return None

    @staticmethod
    def getDate(days_text):                 # Get the date from html with BeautifulSoup
        try:
            date = days_text.find("h5").get_text()
            return date
        except Exception as e:
            print("Error getting date: {}".format(e))
            return None

    @staticmethod
    def getDescription(days_text):          # Get description of days weather from html with BeautifulSoup
        try:
            description = days_text.img['alt']
            return description
        except Exception as e:
            print("Error getting description: {}".format(e))
            return None

    @staticmethod
    def getWindSpeed(days_text):            # Get windspeed from html with BeautifulSoup
        try:
            ws = days_text.find("div", attrs={"class": "ws"}).em.get_text()
            return ws
        except Exception as e:
            print("Error getting windspeed: {}".format(e))
            return None

    @staticmethod
    def getRain(days_text):               # Get days rainfall from html with BeautifulSoup
        try:
            raindiv = days_text.find("div", attrs={"class": "rain"})
            rain = raindiv.get_text()
            return rain
        except Exception as e:
            print("Error getting rainfall: {}".format(e))
            return None

    @staticmethod
    def getPart(days_text, startpart, endpart):
        try:
            match = re.search(startpart, days_text)
            st1, e1 = match.span()
            match2 = re.search(endpart, days_text[e1:])
            st2, e2 = match2.span()
            return days_text[e1:(e1+st2)]                # Part in the middle of two elements
        except Exception as e:
            print("Error getting text part: {} {}".format(e, days_text))
            return None

    @staticmethod
    def hightemp(days_text):                  # returns highest temperature of the day extracted from a section of page
        try:
            warm = re.search('Ylin: <span class="warm">', days_text)
            if warm:
                span = warm.span()
                st, e = span
                return foreca_extractor.warmthToInt(days_text[e:(e+2)])
            else:
                cold = re.search('Ylin: <span class="cold">', days_text)
                span = cold.span()
                st, e = span
                return foreca_extractor.warmthToInt(days_text[e:(e+2)])
        except Exception as e:
            print("Error getting highest temperature: {}".format(e))
            return None

    @staticmethod
    def warmthToInt(warmth):        # 3 character string as parameter to get Temperature as Int
        try:
            dec = ''
            for i in warmth:
                if i.isdecimal():
                    dec += i 
            if warmth[0]=='+':                  # + degrees
                return int(dec)
            elif warmth[0]=='-':                # - degrees
                r = 0-int(dec)
                return r
            else:                               # 0 temperature
                return 0                    
        except Exception as e:
            print("Error converting warmth to Int: {}".format(e))
            return None

    @staticmethod
    def rainToFloat(rain):
        try:
            dec = ''
            for i in rain:
                if i==',':
                    dec += '.'
                if i.isdecimal():
                    dec += i
            return float(dec)
        except Exception as e:
            print("Error converting rain to float: {}".format(e))
            return None


