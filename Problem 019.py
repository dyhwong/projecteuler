months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

def modifyCalendar(year):
    #changes calendar depending on whether or not it is a leap year
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        months[2] = 29
    else:
        months[2] = 28

def countSundays(startingDay, startYear, endYear):
    #takes day of January 1st of start year (Monday = 1, Tuesday = 2, etc.)
    #loops until December 31st of end year
    #returns number of Sundays in the duration
    numberOfSundays = 0
    remainder = startingDay % 7
    year = startYear
    while year <= endYear:
        modifyCalendar(year)
        for i in range(1, 13):
            remainder += months[i]
            remainder = remainder % 7
            if remainder == 0:
                numberOfSundays += 1
        year += 1
    return numberOfSundays

def main():
    print countSundays(2, 1901, 2000)

main()
        
