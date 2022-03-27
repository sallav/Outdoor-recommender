import Locations
import scraper
import Locations 
import Day_comparer

def main():

    loc = Locations.Locations()
    scrpr = scraper.scraper()
    comparer = Day_comparer.Day_comparer()

    best_days = []
    locations = loc.getLocations()
    area = loc.getArea()

    for (index, location) in enumerate(locations):                          # Get days with the best weather
        url = "https://www.foreca.fi/{}/{}/10vrk".format(area, location)
        page = scrpr.ses(url)
        days = scrpr.getDays(page)
        bestday = comparer.bestDay(days)
        bestday.setLocation(location)
        best_days.append(bestday)

    sorted_days = sorted(best_days, key=lambda x: (x.getRating(), x.getWarmest()), reverse=True)    # Sort by rating and warmth

    for day in sorted_days:
        print(day.toString())

if __name__ == "__main__":
    main()