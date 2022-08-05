from exceptions import CliUserError

cities_by_shorthand = {
    'bos': 'BOSTON, MA US',
    'jnu': 'JUNEAU AIRPORT, AK US',
    'mia': 'MIAMI INTERNATIONAL AIRPORT, FL US'
}

def lookup_city(shorthand):
    if shorthand not in cities_by_shorthand:
        raise CliUserError(
            f"{shorthand} is not a valid city name. Valid options are " +
            ','.join(cities_by_shorthand.keys())
        )
    
    return cities_by_shorthand[shorthand]