from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..period import InvalidPeriodError
from ..months import MonthPeriod
from ..years import YearPeriod


class PeriodSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
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
        result = {'year': instance.year}
        if hasattr(instance, 'month'):
            result['month'] = instance.month
        return result
