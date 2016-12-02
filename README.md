# pyperiods

A Python library for representing and manipulating specific periods in time such as years and year/month.

## Some features

 - Both specific years (ex: 2012) and specific months (ex: January 2012) can be represented, manipulated and compared.
 - Simple add/subtract operations are supported (`month + 1` = next month)
 - Utilities for iterations (i.e.: iterate through all previous 12 months)
 - A Django ModelField is provided for storing months/years in Django models
 - A Django REST Framework serializer is provided for convenience as well
 - Compatible with **Python 3** only

## Concepts

The main concept of the library is a **Period**, an abstract base class which can represent either a specific year (ex: 2012), or a specific month and its year (ex: January 2012).

Specific years are represented by instances of the **`YearPeriod`** class while specific months are represented by instances of the **`MonthPeriod`** class.

Periods are comparable and can be sorted. All periods have a string representation which corresponds to either the year only as 4 digits (ex: `2012`) or the year and the month as 6 digits (ex: `201201`)


## Examples

The basics:

``` python
>>> from pyperiods.months import MonthPeriod
>>> start = MonthPeriod('201605')
>>> start.year
2016
>>> start.month
5
>>> next_month = start + 1
>>> str(next_month)
'201605'
>>> next_month.format_long
'May 2016'
>>> next_month.first_day()
datetime.date(2016, 5, 1)

>>> periods = [
        MonthPeriod('201607'),
        MonthPeriod('201601'),
        MonthPeriod('201501'),
        MonthPeriod('201507'),
    ]
>>> list(periods.sort())
[201501, 201507, 201601, 201607]

>>> list(MonthPeriod('201605').range(stop=6))
[201605, 201606, 201607, 201608, 201609, 201610, 201611]

>>> list(MonthPeriod('201605').range(start=6, stop=8))
[201611, 201612, 201701]

>>> from pyperiods.years import YearPeriod
>>> current_year = YearPeriod()
>>> str(current_year)
'2016'
>>> list(current_year.months)
[201601, 201602, 201603, 201604, 201605, 201606, 201607, 201608, 201609, 201610, 201611, 201612]

```


## APIs

See all unit tests in the `tests` folder for details on supported APIs.
