"""Core day counting logic and CLI."""

import argparse
import sys
from datetime import date, datetime


def parse_date(date_str: str) -> date:
    """Parse a date string in YYYY-MM-DD format."""
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(f"Invalid date '{date_str}'. Use YYYY-MM-DD format.")


def count_days(start: date, end: date, inclusive: bool = False) -> int:
    """
    Count calendar days between two dates.
    
    Args:
        start: The start date.
        end: The end date.
        inclusive: If True, include both start and end days in the count.
    
    Returns:
        Number of days between the dates.
    """
    if start > end:
        start, end = end, start  # Swap to always count forward
    
    delta = (end - start).days
    return delta + 1 if inclusive else delta


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Count calendar days between two dates."
    )
    parser.add_argument(
        "start",
        help="Start date in YYYY-MM-DD format"
    )
    parser.add_argument(
        "end",
        nargs="?",
        default=None,
        help="End date in YYYY-MM-DD format (default: today)"
    )
    parser.add_argument(
        "--inclusive", "-i",
        action="store_true",
        help="Include both start and end dates in the count"
    )
    
    args = parser.parse_args()
    
    try:
        start_date = parse_date(args.start)
        end_date = parse_date(args.end) if args.end else date.today()
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    
    days = count_days(start_date, end_date, inclusive=args.inclusive)
    
    inclusive_text = " (inclusive)" if args.inclusive else ""
    print(f"Days between {start_date} and {end_date}: {days}{inclusive_text}")


if __name__ == "__main__":
    main()