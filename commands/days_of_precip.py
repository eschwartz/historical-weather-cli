import csv
from datetime import datetime

help = """
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

def days_of_precip():
    with open('sample.csv', 'r') as csvFile:
        reader = csv.DictReader(csvFile); 

        precip_days_count = 0  

        first_date = None

        for row in reader:
            if (first_date is None and ):
                print(row['DATE'])
                first_date = parse_date(row['DATE'])
            
            if (row['PRCP'] != '0' or row['SNOW'] != '0'):
                precip_days_count += 1
        
        last_date = parse_date(row['DATE'])

        # todo
        # - limit to city
        # - calculate date range
        # - calculate avg
        # - test

        return {
            'first_date': first_date.isoformat(),
            'last_date': last_date.isoformat(),
            'precip_days_count': precip_days_count
        }

def parse_date(date_str):
    # See format codes: 
    # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    return datetime.strptime(date_str, '%Y-%m-%d')