from unittest import TestCase

from pyperiods.months import MonthPeriod
from pyperiods.period import InvalidPeriodError
from pyperiods.years import YearPeriod


def _serialize(period):
    from pyperiods.restframework.serializers import PeriodSerializer
    return PeriodSerializer().to_representation(period)


def _deserialize(obj):
    from pyperiods.restframework.serializers import PeriodSerializer
    return PeriodSerializer().to_internal_value(obj)


class TestPeriodSerializer(TestCase):

    @classmethod
    def setUpClass(cls):
        from django.conf import settings
        settings.configure()

    def test_deserialize_from_object(self):
        self.assertEqual(_deserialize({'year': 2012}), YearPeriod('2012'))
        self.assertEqual(_deserialize({'year': 2012, 'month': 2}), MonthPeriod('201202'))

    def test_deserialize_from_string(self):
        self.assertEqual(_deserialize('2013'), YearPeriod('2013'))
        self.assertEqual(_deserialize('201305'), MonthPeriod('201305'))

    def test_deserialize_from_empty_inputs(self):
        from rest_framework.exceptions import ValidationError

        self.assertRaises(ValidationError, _deserialize, {})

    def test_deserialize_from_invalid_input(self):
        self.assertRaises(InvalidPeriodError, _deserialize, 'abcdef')

    def test_serialize(self):
        self.assertEqual(_serialize(YearPeriod('2012')), {'year': 2012})
        self.assertEqual(_serialize(MonthPeriod('201202')), {'year': 2012, 'month': 2})

    def test_serialize_empty(self):
        self.assertEqual(_serialize(None), None)
        self.assertRaises(ValueError, _serialize, '')
        self.assertRaises(ValueError, _serialize, 201202)
