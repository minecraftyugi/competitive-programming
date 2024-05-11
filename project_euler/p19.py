DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

class Date:
    def __init__(self, day, month, year, day_in_week=0):
        self.day = day
        self.month = month
        self.year = year
        self.day_in_week = day_in_week

    def increase_by_month(self):
        self.day_in_week += get_days_in_month(self.month, self.year)
        self.day_in_week %= 7
        
        self.month += 1
        if self.month == 12:
            self.month = 0
            self.year += 1

    def is_sunday(self):
        return self.day_in_week == 0

    def __lt__(self, other):
        if self.year > other.year:
            return False
        if self.year == other.year and self.month > other.month:
            return False
        if self.year == other.year and self.month == other.month and self.day > other.day:
            return False

        return True
        
def get_days_in_month(month, year):
    if month != 1:
        return DAYS_IN_MONTH[month]

    if year % 4 != 0:
        return DAYS_IN_MONTH[month]

    if year % 100 == 0 and year % 400 != 0:
        return DAYS_IN_MONTH[month]

    return 29

start = Date(0, 0, 1900, 1)
end = Date(0, 0, 2001)
for _ in range(12):
    start.increase_by_month()

count = 0
while start < end:
    if start.is_sunday():
        count += 1

    start.increase_by_month()

print(count)
