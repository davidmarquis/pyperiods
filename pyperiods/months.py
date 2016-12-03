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
            elif not_empty(year):
                self.year = int(year)
                self.month = int(month) if month is not None else 1
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

        super().__init__(MonthPeriod.format_as_identity(self.year, self.month))

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

    def range(self, start=0, stop=0):
        """
        Returns a generator that will yield consecutive months relatively from the current month.
        :param start: The delta to start from (negative starts with a past month)
        :param stop: The delta to end with
        :return:
        """
        for delta in range(start, stop+1):
            yield self + delta

    def format_long(self):
        return date.strftime(self.start, '%B %Y')

    def format_long_month_only(self):
        return date.strftime(self.start, '%B')

    def first_day(self):
        return self.start

    def last_day(self):
        return self.end

    def days(self, start=1):
        for day in range(start, self.end.day):
            yield date(self.year, self.month, day=day)

    def as_date(self, day):
        return date(self.year, self.month, day)

    @staticmethod
    def format_as_identity(year, month):
        return '{year}{month:02d}'.format(year=year, month=month)
