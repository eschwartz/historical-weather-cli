import argparse
import textwrap
from decimal import Decimal
from exceptions import CliUserError
from utils import parse_date, lookup_city, cities_by_shorthand, date_tostring

def max_temp_delta(
    records,
    city,
    year=None,
    month=None
):
    # Validate month/year options
    if month is not None and year is None:
        raise CliUserError('Must also provide a year, if a month is provided')

    # Lookup the full city name
    city_code = lookup_city(city)
    
    # track max temp change, and date
    max_delta = (0, None)

    for row in records:
        # Skip rows that aren't in the given city
        if row['NAME'] != city_code:
            continue
        
        # Skip records not in the provided year/month
        date = parse_date(row['DATE'])
        if (year is not None and date.year != year):
            continue
        if (month is not None and date.month != month):
            continue

        # Calculate temp delta, see if it's the new max
        #
        # Use decimal types to avoid floating point errors
        # https://docs.python.org/3/library/decimal.html#floating-point-notes
        temp_delta = Decimal(row['TMAX']) - Decimal(row['TMIN'])
        if temp_delta > max_delta[0]:
            max_delta = (temp_delta, date)

    return {
        'city': city,
        'date': date_tostring(max_delta[1]),
        'temp_change': float(max_delta[0])
    }

def register_argparser(subparsers):
    help  = textwrap.dedent("""
        Determine the greatest single day low to high temperature
        change for the designated city and time period (all time, 
        yearly, monthly).
    """)

    parser = subparsers.add_parser(
        'max-temp-delta',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=help,
        help=help,
        epilog=textwrap.dedent("""
            Output (JSON)
                city                City being evaluated
                date                Date with largest temp delta
                temp_change         Temperature delta
        """)
    )

    parser.add_argument(
        '--city',
        required=True,
        help="Which city to evaluate. eg. bos, jnu, mia",
        choices=cities_by_shorthand.keys()
    )

    parser.add_argument(
        '--year',
        help="""
            Restrict search to a single year. 
            Format: YYYY, eg. 2018
        """,
        type=int
    )

    parser.add_argument(
        '--month',
        help="""
            Restrict search to a particular month
            Requires --year
            Format: integer, 1-12
        """,
        type=int
    )

    parser.set_defaults(run_command=max_temp_delta)

    return parser