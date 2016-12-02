import calendar
from datetime import date

from .period import Period, InvalidPeriodError, validate_year, validate_month


def not_empty(value):
    if value is None:
        return False
    if isinstance(value, str):
        return len(value) > 0
    return True


class MonthPeriod(Period):
    def __init__(self, yearmonth=None, year=None, month=None):
        try:
            if not_empty(yearmonth):
                if len(yearmonth) != 6:
                    raise ValueError()
                self.year = int(yearmonth[0:4])
                self.month = int(yearmonth[4:6])
            elif not_empty(year) and not_empty(month):
                self.year = int(year)
                self.month = int(month)
            else:
                today = date.today()
                self.year = today.year
                self.month = today.month
        except ValueError:
            raise InvalidPeriodError('Cannot create MonthPeriod from string "%s"' % yearmonth)

        validate_month(self.month)
        validate_year(self.year)

        last_day = calendar.monthrange(self.year, self.month)[1]
        self.start = date(self.year, self.month, day=1)
        self.end = date(self.year, self.month, day=last_day)

        super().__init__(self.format_period_from(self.year, self.month))

    def __lt__(self, other):
        if self.year == other.year:
            return self.month < other.month
        return self.year < other.year

    def __add__(self, other):
        """
        Adds a certain number of months to this period.
        """
        year_delta, month = divmod(self.month + other - 1, 12)
        return MonthPeriod(year=self.year + year_delta, month=month + 1)

    def __sub__(self, other):
        """
        Subtracts a certain number of months from this period.
        """
        return self + (-other)

    def range(self, start=0, stop=0):
        for delta in range(start, stop+1):
            yield self + delta

    def format_long(self):
        return date.strftime(self.start, '%B %Y')

    def format_month(self):
        return date.strftime(self.start, '%B')

    def first_day(self):
        return self.start

    def last_day(self):
        return self.end

    def as_date(self, day):
        return date(self.year, self.month, day)

    def next(self):
        return self + 1

    def previous(self):
        return self - 1

    @staticmethod
    def format_period_from(year, month):
        return '{year}{month:02d}'.format(year=year, month=month)

    @staticmethod
    def year_months(year):
        return [item for item in MonthPeriod(year=year, month=1).range(stop=11)]
