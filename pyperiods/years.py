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

        super().__init__(str(self.year))

    def __lt__(self, other):
        return self.year < other.year

    def __add__(self, other):
        if isinstance(other, YearPeriod):
            other = other.year
        return YearPeriod(self.year + other)

    def __sub__(self, other):
        if isinstance(other, YearPeriod):
            other = other.year
        return YearPeriod(self.year - other)

    def range(self, start=0, stop=0):
        if isinstance(start, self.__class__):
            start = start.year - self.year
        if isinstance(stop, self.__class__):
            stop = stop.year - self.year

        for delta in range(start, stop+1):
            yield self + delta

    def months(self):
        return MonthPeriod(year=self.year, month=1).range(0, 11)

    def format_long(self):
        return str(self.year)
