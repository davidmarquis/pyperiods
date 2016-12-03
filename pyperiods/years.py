from datetime import date

from .period import Period, InvalidPeriodError, validate_year
from .months import MonthPeriod


class YearPeriod(Period):
    def __init__(self, year=None):
        try:
            self.year = int(year) if year else date.today().year
        except ValueError:
            raise InvalidPeriodError("Cannot create YearPeriod from year [%s]" % year)

        validate_year(self.year)

        self.start = date(self.year, 1, 1)
        self.end = date(self.year, 12, 31)

        super().__init__(str(self.year))

    def __lt__(self, other):
        return self.year < other.year

    def __add__(self, other):
        if isinstance(other, YearPeriod):
            other = other.year
        return YearPeriod(self.year + other)

    def range(self, start=0, stop=0):
        if isinstance(start, type(self)):
            start = start.year - self.year
        if isinstance(stop, type(self)):
            stop = stop.year - self.year

        for delta in range(start, stop+1):
            yield self + delta

    def first_day(self):
        return self.start

    def last_day(self):
        return self.end

    @property
    def months(self):
        return MonthPeriod(year=self.year, month=1).range(0, 11)

    def format_long(self):
        return str(self.year)
