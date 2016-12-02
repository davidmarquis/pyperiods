from functools import total_ordering


class InvalidPeriodError(Exception):
    pass


def validate_year(year):
    if year < 1970 or year > 9999:
        raise InvalidPeriodError("Year must be between 1970 and 9999")


def validate_month(month):
    if month < 1 or month > 12:
        raise InvalidPeriodError("Month must be between 1 and 12")


@total_ordering
class Period(object):
    def __init__(self, period):
        self.period = period

    def __repr__(self):
        return str(self.period)

    def __str__(self):
        return self.__repr__()

    def __unicode__(self):
        return self.__repr__()

    def __len__(self):
        return len(self.period)

    def __eq__(self, other):
        if isinstance(other, str):
            other = self.__class__(other) if other else None
        if other is None:
            return False
        if not isinstance(other, self.__class__):
            return False
        return self.period == other.period

    def __hash__(self):
        return self.period.__hash__()

    def __lt__(self, other):
        return self.period < other.period

    def is_current(self):
        current_period = type(self)()
        return current_period == self

    def is_future(self):
        current_period = type(self)()
        return int(current_period.period) < int(self.period)
