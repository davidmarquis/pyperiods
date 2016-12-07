from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from pyperiods.factory import period_from_string
from ..period import InvalidPeriodError, Period
from ..months import MonthPeriod
from ..years import YearPeriod


class PeriodSerializer(serializers.BaseSerializer):
    """
    Serializer for Django REST Framework. Can deserialize a period from a string or from an object
    with 'year' and optional 'month' attributes.
    """

    def to_internal_value(self, data):
        if isinstance(data, str):
            return period_from_string(data)

        year = data.get('year', None)
        month = data.get('month', None)

        if not year:
            raise ValidationError("Missing value for 'year' field: "
                                  "at least a year is required for creating a Period.")

        try:
            return YearPeriod(year) if month is None \
                else MonthPeriod(year=year, month=month)
        except InvalidPeriodError as e:
            raise ValidationError(str(e))

    def to_representation(self, instance):
        if instance is None:
            return None
        if not isinstance(instance, Period):
            raise ValueError('Cannot serialize value of type [%s]' % type(instance))

        result = {'year': instance.year}
        if hasattr(instance, 'month'):
            result['month'] = instance.month
        return result
