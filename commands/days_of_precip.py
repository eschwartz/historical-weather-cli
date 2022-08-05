import csv
from datetime import datetime, timedelta
from utils import lookup_city, debug_dict, debug, DAYS_PER_YEAR


def days_of_precip(csv_file_path, city_shorthand):
    """
    days-of-precip <city>
    
        Calculate the average number of days per year 
        the given city had non-zero precipitation (either snow or rain) 
        based on the entire period of the dataset

        Arguments
            <city>              Which city to evaluate
                                eg. bos, jnu, mia

        Output (JSON)
            city                City being evaluated
            days_of_precip      Average days of precipitation per year
    """
    # Lookup the full city name
    city = lookup_city(city_shorthand)

    # open the CSV file
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file); 

        precip_days_count = 0  

        first_date = None

        for row in reader:
            # Grab the first date from the first row
            # Assuming that we want to calculate using 
            # the time span of the entire data set
            # (vs. the time span of data for this one city)
            if (first_date is None):
                first_date = parse_date(row['DATE'])
            
            has_precip = (
                (row['PRCP'] != '' and float(row['PRCP']))
                or
                (row['SNOW'] != '' and float(row['SNOW']))
            )
            is_city = row['NAME'] == city
            if (has_precip and is_city):
                precip_days_count += 1
        
    # Access the last date, from the last row
    # Add 1 day, because each record represent a full day
    # eg. "2022-01-01" - "2022-01-02" == 1 day; 
    # but it represents 2 days of data
    last_date = parse_date(row['DATE']) + timedelta(days=1)

    # Calculate time span, in years
    time_delta = last_date - first_date
    time_span_years = time_delta.days / DAYS_PER_YEAR

    # Calculate average days with precip, per year
    avg_days_of_precip_per_year = precip_days_count / time_span_years

    # debug logs, to help understand the calculation
    # (set LOG_LEVEL=debug to see these)
    debug_dict({
        'city': city,
        'first_date': first_date,
        'last_date': last_date,
        'time_span_days ': time_delta.days,
        'time_span_years': time_span_years,
        'precip_days_count': precip_days_count,
        'avg_days_of_precip_per_year': avg_days_of_precip_per_year
    })

    return {
        'city': city_shorthand,
        'days_of_precip': avg_days_of_precip_per_year
    }

def parse_date(date_str):
    # See format codes: 
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    return datetime.strptime(date_str, '%Y-%m-%d')