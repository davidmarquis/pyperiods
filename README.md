# pyperiods

A Python library for representing and manipulating specific periods in time such as years and year/month.

## How to Install?

`pyperiods` is available on [Pypi](https://pypi.python.org/pypi/pyperiods):

```
   pip install pyperiods
```

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
>>> start = MonthPeriod(year=2016, month=5)
>>> start.year
2016
>>> start.month
5
>>> next_month = start + 1
>>> str(next_month)
'201606'
>>> next_month.format_long()
'June 2016'
>>> next_month.first_day()
datetime.date(2016, 5, 1)
>>> next_month.last_day()
datetime.date(2016, 5, 30)

>>> from pyperiods.years import YearPeriod
>>> current_year = YearPeriod()
>>> str(current_year)
'2016'
>>> list(current_year.months)
[201601, 201602, 201603, 201604, 201605, 201606, 201607, 201608, 201609, 201610, 201611, 201612]

```

### Basic arithmetic

``` python
>>> MonthPeriod('201611') + 2
201701
>>> MonthPeriod('201611') - 12
201511
```

### Sorting & Comparison

``` python
>>> periods = [
        MonthPeriod('201607'),
        MonthPeriod('201601'),
        MonthPeriod('201501'),
        MonthPeriod('201507'),
    ]
>>> list(periods.sort())
[201501, 201507, 201601, 201607]
>>> MonthPeriod('201502') < MonthPeriod('201601')
True
>>> MonthPeriod('201502') == MonthPeriod('201503') - 1
True
```

### Iteration

``` python
>>> list(MonthPeriod('201605').range(stop=6))
[201605, 201606, 201607, 201608, 201609, 201610, 201611]
>>> list(MonthPeriod('201605').range(start=-2))
[201603, 201604, 201605]
>>> list(MonthPeriod('201605').range(start=-2, stop=2))
[201603, 201604, 201605, 201606, 201607]
```

### Creation

``` python
>>> MonthPeriod('201605')
201605
>>> MonthPeriod(year=2016)
201601
>>> MonthPeriod(year=2016, month=2)
201602
>>> YearPeriod(2016)
2016

>>> from pyperiods.factory import period_from_string
>>> type(period_from_string('2016'))
<class 'pyperiods.years.YearPeriod'>
>>> type(period_from_string('201612'))
<class 'pyperiods.months.MonthPeriod'>
```

## APIs

See all unit tests in the `tests` folder for details on supported APIs.
