from .years import YearPeriod
from .months import MonthPeriod


class PeriodError(Exception):
    pass


def period_factory(period_type, value):
    if period_type == 'month':
        return MonthPeriod(value)
    elif period_type == 'year':
        return YearPeriod(value)
    else:
        raise PeriodError("Unknown period type: %s" % period_type)


def period_from_string(period_str):
    if len(period_str) == 4:
        return YearPeriod(period_str)
    elif len(period_str) == 6:
        return MonthPeriod(yearmonth=period_str)
    raise PeriodError("Could not infer period from string [%s]" % period_str)
