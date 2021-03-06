import re

class Day:

    def __init__(self, date=None, description=None, warmest=None, wind_speed=None, rain_fall=None, location=''):
        self.date = date
        self.description = description
        self.warmest = warmest
        self.wind_speed = wind_speed
        self.rain_fall = rain_fall
        self.location = location
        self.rating = 0

    def setDate(self, date):
        try:
            self.date = date
        except Exception as e:
            print(e)

    def setDesc(self, description):
        try:
            self.description = description
        except Exception as e:
            print(e)

    def setWarmest(self, warmest):
        try:
            self.warmest = warmest
        except Exception as e:
            print(e)

    def setWindSpeed(self, wind_speed):
        try:
            self.wind_speed = wind_speed
        except Exception as e:
            print(e)

    def setRainFall(self, rain_fall):
        try:
            self.rain_fall = rain_fall
        except Exception as e:
            print(e)

    def setLocation(self, location):
        try:
            self.location = location
        except Exception as e:
            print(e)

    def getDate(self):
        return self.date

    def getDescription(self):
        return self.description

    def getWarmest(self):
        try:
            return int(self.warmest)
        except Exception as e:
            print(e)

    def getWindSpeed(self):
        try:
            return int(self.wind_speed)
        except Exception as e:
            print(e)

    def getRainFall(self):
        try:
            return int(self.rain_fall)
        except Exception as e:
            print(e)

    def getLocation(self):
        return self.location
        
    def warmer(self, other):
        try:
            if int(self.warmest)>other.getWarmest():
                return True
            else:
                return False
        except Exception as e:
            print("Error comparing Days: {}".format(e))
    
    def clear(self):
        try:
            if re.search('selke????', self.description, re.I) is not None:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def fair(self):
        try:
            if re.search('poutaa', self.description, re.I) is not None:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def halfCloudy(self):
        try:
            if re.search('puolipilvist??', self.description, re.I) is not None:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False

    def toString(self):
        try:
            st = self.location + " " + self.date + " " + self.description + ", Ylin l??mp??tila: " + str(self.warmest) + " Tuulen nopeus: " + str(self.wind_speed) + " Sadekertym??: " + str(self.rain_fall) 
            return st
        except Exception as e:
            print(e)
            return ''

    def rate(self):
        if re.search('Melkein selke????', self.description, re.I) is not None:
            self.rating += 3
        elif re.search('Selke????', self.description, re.I) is not None:
            self.rating += 4
        elif re.search('puolipilvist??', self.description, re.I):
            self.rating += 2
        elif re.search('melko pilvist??', self.description, re.I):
            self.rating += 1
        if re.search('poutaa', self.description, re.I) is not None:
            self.rating += 1
        elif re.search('sadetta', self.description, re.I) is not None:
            self.rating -= 1
        if self.getRainFall()>0:
            self.rating -= 1

    def getRating(self):
        return self.rating
