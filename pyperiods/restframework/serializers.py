from rest_framework import serializers

from ..months import MonthPeriod
from ..years import YearPeriod


class PeriodSerializer(serializers.BaseSerializer):
    def to_internal_value(self, data):
        year = data.get('year')
        month = data.get('month', None)

        if month is None:
            return YearPeriod(year)
        return MonthPeriod(year=year, month=month)

    def to_representation(self, instance):
        result = {'year': instance.year}
        if hasattr(instance, 'month'):
            result['month'] = instance.month
        return result
