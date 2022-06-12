
import re

class day_evaluator:
        
    @staticmethod
    def fairDays(day_list) -> list:             # Resurns all fair Days from a list
        try:
            fairs = []
            for day in day_list:
                if day.fair():
                    fairs.append(day)
            return fairs
        except Exception as e:
            print("Error getting fair days: {}".format(e))
            return None

    @staticmethod                       # Returns all clear Days from a list
    def clearDays(day_list) -> list:
        try:
            clears = []
            for day in day_list:
                if day.clear():
                    clears.append(day)
            return clears
        except Exception as e:
            print("Error getting clear days: {}".format(e))
            return None

    @staticmethod                       # Return all half cloudy Days from a list
    def halfCloudyDays(day_list) -> list:
        try:
            halfcls = []
            for day in day_list:
                if day.halfCloudy():
                    halfcls.append(day)
            return halfcls
        except Exception as e:
            print("Error getting half cloudy days: {}".format(e))
            return None

    @staticmethod
    def dayWithBestTemp(day_list, maxtemp) -> object:           # Returns the warmest Day from a list
        try:
            best_temp = -100
            best_day = day_list[0]                  # If all days are equal choose first
            for day in day_list:
                days_warmest = day.getWarmest()
                if days_warmest>maxtemp:            # Don't exceed maximum temperature
                    continue
                if best_temp<days_warmest:
                    best_temp = days_warmest
                    best_day = day
            return best_day
        except Exception as e:
            print("Error getting warmest day: {}".format(e))
            return None

    @staticmethod
    def removeWindyDays(day_list, maxwind) -> list:             # Remove days that have windspeed over maximum
        try:
            good_days = []
            for day in day_list:
                if day.getWindSpeed()<=maxwind:
                    good_days.append(day)
            return good_days
        except Exception as e:
            print("Error removing windy days: {}".format(e))
            return None
