import os
import sys
import json
from exceptions import CliUserError

cities_by_shorthand = {
    'bos': 'BOSTON, MA US',
    'jnu': 'JUNEAU AIRPORT, AK US',
    'mia': 'MIAMI INTERNATIONAL AIRPORT, FL US'
}

# How many days in an average year?
#
# Leap years are every 4 years (avg 365.25),
# and also every 100, but not every 400 (avg 365.2425).
#
# But calendars are constructed approximations
# for actual astronomical events: the mean 
# tropical year is 365.24219
#
# You could also look at the number of days in each year
# of the given dataset, though that again gets complicated
# if you aren't dealing with full years' worth of data
#
# See
#   https://en.wikipedia.org/wiki/Year#Gregorian_calendar
#   https://astronomy.stackexchange.com/questions/27500/whats-a-good-model-for-the-vernal-equinox-year-can-it-increase-forever
DAYS_PER_YEAR = 365.24219

def lookup_city(shorthand):
    if shorthand not in cities_by_shorthand:
        raise CliUserError(
            f"{shorthand} is not a valid city name. Valid options are " +
            ','.join(cities_by_shorthand.keys())
        )
    
    return cities_by_shorthand[shorthand]

is_debug_mode = os.environ.get('LOG_LEVEL', 'error') == 'debug'

def debug(val):
    if (is_debug_mode):
        print(val, file=sys.stderr)

def debug_dict(dict):
    debug(json.dumps(dict, indent=2, default=str))