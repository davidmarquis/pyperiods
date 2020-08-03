from django.db import models

from ..factory import period_from_string
from ..period import Period
from ..months import MonthPeriod


class PeriodField(models.CharField):

    description = 'A field that provides a Period (year or month) as its value ' \
                  'and stores it as its string representation'

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 6
        super().__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"

    def to_python(self, value):
        if isinstance(value, Period) or value is None:
            return value
        if isinstance(value, str) and not value:
            return None
        return period_from_string(value)

    def from_db_value(self, value, *args):
        return self.to_python(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        return str(value)


class MonthField(PeriodField):

    description = 'A field that provides a MonthPeriod as its value and stores it as its string representation'

    def to_python(self, value):
        if isinstance(value, MonthPeriod) or value is None:
            return value
        if isinstance(value, str) and not value:
            return None
        return MonthPeriod(value)
