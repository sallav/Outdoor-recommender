import sys
sys.path.append('../')

import requests
from bs4 import BeautifulSoup
from recommender.recommender.text_extractor import foreca_extractor as extr

class scraper:

    @staticmethod
    def ses(url):
        try:
            s = requests.Session()
            response = s.get(url)
            status = response.status_code
            if status==200:
                return response.content
            else:
                return None
        except Exception as e:
            print("Error in getting responce: {}".format(e))
            return None

    @staticmethod
    def getDays(content):               # Return a list of Day -objects
        try:
            soup = BeautifulSoup(content, 'html.parser')
            days = []
            for item in soup.find_all("div", attrs={"class": "day"}):
                day = extr.getDay(str(item))       # Use the text_extractor to create Day -objects
                days.append(day)
            return days
        except Exception as e:
            print("Error getting days: {}".format(e))
            return None
