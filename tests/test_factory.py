from unittest import TestCase

from pyperiods.factory import period_from_string, period_factory
from pyperiods.months import MonthPeriod
from pyperiods.years import YearPeriod


class PeriodFactoryTest(TestCase):

    def test_from_string_month(self):
        self.assertEqual(period_from_string('2015'), YearPeriod(2015))
        self.assertEqual(period_from_string('201512'), MonthPeriod(year=2015, month=12))

    def test_period_factory(self):
        self.assertEqual(period_factory('year', '2015'), YearPeriod(2015))
        self.assertEqual(period_factory('month', '201512'), MonthPeriod(year=2015, month=12))
