from recommender.recommender.day_evaluator import day_evaluator

class Day_comparer:

    def __init__(self, maxtemp=30, maxwind=20, maxrain=2.54):
        self.maxtemp = maxtemp
        self.maxwind = maxwind
        self.maxrain = maxrain

    def bestDay(self, days_list):
        goods = self.clearAndFairs(days_list)                             # Get nice weather days
        if len(goods)==0:
            goods = days_list    
        bests = day_evaluator.removeWindyDays(goods, self.maxwind)          # Remove too windy
        if len(bests)==0:
            bests = goods
        return day_evaluator.dayWithBestTemp(bests, self.maxtemp)         # Choose one with best temperature

    def clearAndFairs(self, days_list):
        fairs = day_evaluator.fairDays(days_list)
        clears = day_evaluator.clearDays(days_list)
        hfcl = day_evaluator.halfCloudyDays(days_list)
        if len(clears)==0:                                      # Choose intersection or the better option
            return self.chooseBetter(fairs, hfcl, days_list)
        else:
            return self.chooseFromBoth(fairs, clears, days_list)

    def chooseFromBoth(self, first, second, all):
        f = set(first)
        s = set(second)
        bests = f.intersection(s)
       # bests = []
       # for day in first:
        #    if day in second:
         #       bests.append(item) 
        if len(bests)==0:
            bests = f                   # Here fair is better than clear
        if len(bests)==0:
            bests = s
        if len(bests)==0:
            bests = sorted(all, key=lambda x: (x.getRating(), x.getWarmest()), reverse=True)[0]
        bests = list(bests)
        return bests

    def chooseBetter(self, first, second, all):
        bests = first
        if len(bests)==0:
            bests = second
        if len(bests)==0:
            bests = sorted(all, key=lambda x: (x.getRating(), x.getWarmest()), reverse=True)[0]
        return list(bests)

