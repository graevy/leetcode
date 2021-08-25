import _timedPrint
from itertools import permutations


class Date():
    def __init__(self, mm, dd, yyyy):
        self.month = int(mm)
        self.day = int(dd)
        self.year = int(yyyy)

def month(date):
    return date.month

def day(date):
    return date.day

def year(date):
    return date.year

# you know, this actually fails one of the test cases
@_timedPrint.timed
def distance1(date1, date2):
    # MMDDYYYY
    if abs(year(date1) - year(date2)) <= 1:
        print('years close')
        if abs((month(date1) % 12) - (month(date2) % 12)) <= 1:
            print('months close')
            if day(date1) == day(date2):
                print('days same')
                if month(date1) == month(date2):
                    print('months same')
                    if year(date1) == year(date2):
                        print('years same')
                        return -1
                    else:
                        return 1
                return 0

            # "the jan 1st and feb 2nd problem"
            if month(date1) - month(date2) > 0 and day(date1) - day(date2) > 0:
                return 1
            elif month(date2) - month(date1) > 0 and day(date2) - day(date1) > 0:
                return 1
            else:
                return -1
    return 1

@_timedPrint.timed
def distance2(date1, date2):
    date1float = date1.day + date1.month/32 + date1.year/366
    date2float = date2.day + date2.month/32 + date2.year/366
    diff = date1float - date2float
    if diff == 0:
        return 0
    return 1 if diff > 30 else  -1

a = Date('01', '01', '1970')
b = Date('01', '30', '1970')
c = Date('02', '02', '1970')
d = Date('01', '01', '1969')
e = Date('01', '01', '1500')
f = Date('12', '01', '1969')

dates = (a,b,c,d,e)
data = permutations(dates, 2)

for elem in data:
    distance2(*elem)
