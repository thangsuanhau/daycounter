"""Unit tests for daycounter."""

from datetime import date
import pytest
from daycounter.counter import count_days, parse_date


def test_parse_date_valid():
    assert parse_date("2024-01-15") == date(2024, 1, 15)


def test_parse_date_invalid():
    with pytest.raises(ValueError):
        parse_date("15-01-2024")


def test_count_days_exclusive():
    start = date(2024, 1, 1)
    end = date(2024, 1, 10)
    assert count_days(start, end) == 9


def test_count_days_inclusive():
    start = date(2024, 1, 1)
    end = date(2024, 1, 10)
    assert count_days(start, end, inclusive=True) == 10


def test_count_days_swapped():
    """Should work even if start > end."""
    start = date(2024, 1, 10)
    end = date(2024, 1, 1)
    assert count_days(start, end) == 9


def test_count_same_day():
    start = date(2024, 1, 1)
    end = date(2024, 1, 1)
    assert count_days(start, end) == 0
    assert count_days(start, end, inclusive=True) == 1