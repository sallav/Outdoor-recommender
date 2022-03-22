
class Locations:

    def __init__(self):
        self.area = 'Finland'
        self.locations = paikat = ['Espoo', 'Helsinki', 'Hyvinkää', 'Hämeenlinna', 'Joensuu', 'Jyväskylä', 'Kotka', 'Kuopio', 'Lahti', 'Lappeenranta', 'Mikkeli', 'Oulu', 'Pori', 'Porvoo', 'Tampere', 'Turku', 'Vaasa', 'Vantaa']

    def setArea(self, area):
        try:
            self.area = area
        except Exception as e:
            print("Error setting area: {}".format(e))

    def setLocations(self, list):
        try:
            self.locations = list
        except Exception as e:
            print("Error setting locations: {}".format(e))

    def getArea(self):
        return self.area
        
    def getLocations(self):
        return self.locations

    