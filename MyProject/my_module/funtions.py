"""A collection of functions to plan a crochet blanket."""

import requests
from bs4 import BeautifulSoup

def find_daily_temp(date_to_find):
    """
    Finds the daily average temperature in Farenheit in La Jolla, San Diego for a given date from Weather Underground.

    Parameters   
    ----------  
    date_to_find : str
        The date to find the temperature in the format 'YYYY-MM-DD'.

    Returns
    --------
    str or None
        The daily average temperature if found, None otherwise.
        
    Sources
    -------
    [1] Open AI: ChatGPT - Learned usage of Python Library, Beautiful Soup, to
    analyze given weather data from Weather Underground.
    [2] Weather Underground - Used this website to extract weather data for
    this project.
    """
    url = f'https://www.wunderground.com/history/daily/us/ca/la-jolla/KSAN/date/{date_to_find}'
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    temperature_element = soup.find('span', class_='wu-value wu-value-to')
    
    if temperature_element:
        temperature = temperature_element.get_text()
        return temperature
    
    else:
        return None
    

# example usage of finding average daily temperature for a specific day
date_to_find = '2024-03-19'
temperature = find_daily_temp(date_to_find)

# added print statements to organize Daily Average Temperature output 
if temperature is not None:
    print(f"Daily Average Temperature on {date_to_find}: {temperature}")   
    
else:
    print(f"Temperature data not found for {date_to_find}.")
    

def calculate_crochet_gauge(stitches, rows, measurement_unit):
    """
    Calculates the crochet gauge based on the number of stitches and rows.

    Parameters
    ----------
    stitches : int
        Number of stitches.
    rows : int
        Number of rows.
    measurement_unit : str
        Measurement unit, either 'inches' or other.

    Returns
    -------
    tuple or None
    Tuple containing the stitch gauge and row gauge if the measurement unit is    
    'inches', otherwise None.
    """
    if measurement_unit == 'inches':
        
        # gauge swatches typically made in 4 inches
        stitch_gauge = stitches / 4
        row_gauge = rows / 4
        return stitch_gauge, row_gauge
    
    else:
        return None
    

# example usage of finding stitch gauge and row gauge
stitch_gauge, row_gauge = calculate_crochet_gauge(15, 9, 'inches')

# added print statements to read how many stitches and rows are needed per inch
if stitch_gauge is not None and row_gauge is not None:
    print('Stitch gauge:', stitch_gauge, 'stitches for every 1 inch')
    print('Row gauge:', row_gauge, 'rows for every 1 inch')
    
else: 
    print('Wrong measurement unit, try inches or in')
    

def calculate_blanket_size(width, length, stitch_gauge, row_gauge):
    """
    Calculates the total number of stitches and rows needed to reached desired size of crochet blanket.

    Parameters
    ----------
    width : int
        Width of the blanket in inches.
    length : int
        Length of the blanket in inches.
    stitch_gauge : float
        Stitch gauge (stitches per inch).
    row_gauge : float
        Row gauge (rows per inch).

    Returns
    -------
    tuple
        Tuple containing the total number of stitches and rows needed.
    """
    total_stitches = width * stitch_gauge
    total_rows = length * row_gauge
    return total_stitches, total_rows


# example of calculating blanket size
width = 65
length = 90
stitch_gauge = 15
row_gauge = 9

# added print statements to read how many stitches and rows needed for desired size
total_stitches, total_rows = calculate_blanket_size(width, length, stitch_gauge, row_gauge)
print('Total stitches:', total_stitches)
print('Total rows:', total_rows)


def yarn_color(temperature):
    """
    Determines the color of yarn to use based on the temperature.

    Parameters
    ----------
    temperature : int
        Daily average temperature in Fahrenheit.

    Returns
    -------
    str
        Color of yarn to use.
    
    Sources
    -------
    [1] easycrochet.com - Used provided temperature blanket yarn color code.
    """
    if temperature < 30:
        use_yarn = 'white'
    elif temperature in range(30, 40):
        use_yarn = 'light blue'
    elif temperature in range(40, 50):
        use_yarn = 'dark blue'
    elif temperature in range(50, 60):
        use_yarn = 'green'
    elif temperature in range(60, 70):
        use_yarn = 'yellow'
    elif temperature in range(70, 80):
        use_yarn = 'orange'
    elif temperature >= 80:
        use_yarn = 'red'
    return use_yarn
