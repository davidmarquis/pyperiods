from unittest import TestCase
from datetime import date

from pyperiods.period import InvalidPeriodError
from pyperiods.years import YearPeriod


class YearPeriodTest(TestCase):

    def test_empty_constructor_uses_current_year(self):
        current_year = date.today().year

        period = YearPeriod()

        self.assertEqual(period.year, current_year)

    def test_constructor(self):
        self.assertEqual(YearPeriod('2016').year, 2016)
        self.assertEqual(YearPeriod(2016).year, 2016)

    def test_sort_natural(self):
        periods = [
            YearPeriod('2016'),
            YearPeriod('2017'),
            YearPeriod('2015'),
        ]

        periods.sort()

        self.assertEqual([p.year for p in periods], [2015, 2016, 2017, ])

    def test_subtract(self):
        self.assertEqual(YearPeriod(2016) - 1, YearPeriod(2015))

    def test_months(self):
        months_in_year = [str(m) for m in YearPeriod(2016).months]
        self.assertEqual(months_in_year, ['201601','201602','201603','201604','201605','201606',
                                          '201607','201608','201609','201610','201611','201612',])

    def test_add(self):
        self.assertEqual(YearPeriod(2016) + 1, YearPeriod(2017))

    def test_subtract(self):
        self.assertEqual(YearPeriod(2016) - 1, YearPeriod(2015))

    def test_range(self):
        generator = YearPeriod(2015).range(0, 3)

        self.assertEqual(next(generator), YearPeriod(2015))
        self.assertEqual(next(generator), YearPeriod(2016))
        self.assertEqual(next(generator), YearPeriod(2017))
        self.assertEqual(next(generator), YearPeriod(2018))
        self.assertRaises(StopIteration, next, generator)

    def test_range_with_period(self):
        generator = YearPeriod(2015).range(stop=YearPeriod(2018))

        self.assertEqual(next(generator), YearPeriod(2015))
        self.assertEqual(next(generator), YearPeriod(2016))
        self.assertEqual(next(generator), YearPeriod(2017))
        self.assertEqual(next(generator), YearPeriod(2018))
        self.assertRaises(StopIteration, next, generator)

    def test_range_negative(self):
        generator = YearPeriod(2015).range(-2, 2)

        self.assertEqual(next(generator), YearPeriod(2013))
        self.assertEqual(next(generator), YearPeriod(2014))
        self.assertEqual(next(generator), YearPeriod(2015))
        self.assertEqual(next(generator), YearPeriod(2016))
        self.assertEqual(next(generator), YearPeriod(2017))
        self.assertRaises(StopIteration, next, generator)

    def test_create_from_empty_strings(self):
        self.assertEqual(str(YearPeriod('')), YearPeriod())

    def test_current_past_future(self):
        month = YearPeriod()
        self.assertTrue(month.is_current())
        self.assertFalse(month.next().is_current())
        self.assertTrue(month.next().is_future())
        self.assertFalse(month.next().is_past())
        self.assertTrue(month.previous().is_past())
        self.assertFalse(month.next().is_past())

    def test_invalid_years(self):
        self.assertRaises(InvalidPeriodError, YearPeriod, 10000)
        self.assertRaises(InvalidPeriodError, YearPeriod, 1950)
        self.assertRaises(InvalidPeriodError, YearPeriod, 'ab')
