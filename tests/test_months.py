from unittest import TestCase
from datetime import date

from pyperiods.months import MonthPeriod
from pyperiods.period import InvalidPeriodError


class MonthPeriodTest(TestCase):

    def test_empty_constructor_uses_current_month(self):
        current_year = date.today().year
        current_month = date.today().month

        period = MonthPeriod()

        self.assertEqual(period.year, current_year)
        self.assertEqual(period.month, current_month)

    def test_month_year_extraction(self):
        period = MonthPeriod('201604')

        self.assertEqual(period.year, 2016)
        self.assertEqual(period.month, 4)

    def test_format_long(self):
        period = MonthPeriod('201612')

        self.assertEqual(period.format_long(), 'December 2016')

    def test_sort_natural(self):
        periods = [
            MonthPeriod('201607'),
            MonthPeriod('201601'),
            MonthPeriod('201501'),
            MonthPeriod('201507'),
        ]

        periods.sort()

        self.assertEqual([p.period for p in periods], ['201501', '201507', '201601', '201607'])

    def test_subtract(self):
        self.assertEqual(MonthPeriod('201602') - 1, MonthPeriod('201601'))
        self.assertEqual(MonthPeriod('201602') - 2, MonthPeriod('201512'))
        self.assertEqual(MonthPeriod('201602') - 14, MonthPeriod('201412'))

    def test_add(self):
        self.assertEqual(MonthPeriod('201611') + 1, MonthPeriod('201612'))
        self.assertEqual(MonthPeriod('201611') + 2, MonthPeriod('201701'))
        self.assertEqual(MonthPeriod('201602') + 14, MonthPeriod('201704'))

    def test_next(self):
        self.assertEqual(MonthPeriod('201611').next(), MonthPeriod('201612'))

    def test_previous(self):
        self.assertEqual(MonthPeriod('201611').previous(), MonthPeriod('201610'))

    def test_range(self):
        start = MonthPeriod('201510')
        generator = start.range(0, 3)

        self.assertEqual(next(generator), MonthPeriod('201510'))
        self.assertEqual(next(generator), MonthPeriod('201511'))
        self.assertEqual(next(generator), MonthPeriod('201512'))
        self.assertEqual(next(generator), MonthPeriod('201601'))
        self.assertRaises(StopIteration, next, generator)

    def test_range_negative(self):
        start = MonthPeriod('201512')
        generator = start.range(-2, 2)

        self.assertEqual(next(generator), MonthPeriod('201510'))
        self.assertEqual(next(generator), MonthPeriod('201511'))
        self.assertEqual(next(generator), MonthPeriod('201512'))
        self.assertEqual(next(generator), MonthPeriod('201601'))
        self.assertEqual(next(generator), MonthPeriod('201602'))
        self.assertRaises(StopIteration, next, generator)

    def test_create_from_strings(self):
        self.assertEqual(str(MonthPeriod(year='2012', month='02')), '201202')

    def test_create_from_empty_strings(self):
        self.assertEqual(str(MonthPeriod(yearmonth='')), MonthPeriod())
        self.assertEqual(str(MonthPeriod(year='', month='')), MonthPeriod())

    def test_invalid_month(self):
        self.assertRaises(InvalidPeriodError, MonthPeriod, year=2012, month=-1)
        self.assertRaises(InvalidPeriodError, MonthPeriod, year=2012, month=0)
        self.assertRaises(InvalidPeriodError, MonthPeriod, year=2012, month=14)
        self.assertRaises(InvalidPeriodError, MonthPeriod, year=2012, month='ab')

    def test_invalid_years(self):
        self.assertRaises(InvalidPeriodError, MonthPeriod, year=10000, month=1)
        self.assertRaises(InvalidPeriodError, MonthPeriod, year='ab', month=0)

    def test_invalid_yearmonths(self):
        self.assertRaises(InvalidPeriodError, MonthPeriod, yearmonth='0')
        self.assertRaises(InvalidPeriodError, MonthPeriod, yearmonth='912')
        self.assertRaises(InvalidPeriodError, MonthPeriod, yearmonth='9912')
        self.assertRaises(InvalidPeriodError, MonthPeriod, yearmonth='99912')
        self.assertRaises(InvalidPeriodError, MonthPeriod, yearmonth='abcd12')
        self.assertRaises(InvalidPeriodError, MonthPeriod, yearmonth='2012ab')
