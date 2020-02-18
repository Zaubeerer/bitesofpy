from collections import Counter

import requests

CAR_DATA = 'https://bites-data.s3.us-east-2.amazonaws.com/cars.json'

# pre-work: load JSON data into program

with requests.Session() as s:
    data = s.get(CAR_DATA).json()


# your turn:
def most_prolific_automaker(year):
    """Given year 'year' return the automaker that released
       the highest number of new car models"""

    releases_per_carmaker = Counter()

    for car_dict in data:
        if car_dict["year"] == year:
            releases_per_carmaker[car_dict["automaker"]] += 1

    return releases_per_carmaker.most_common(1)[0][0]

def get_models(automaker, year):
    """Filter cars 'data' by 'automaker' and 'year',
       return a set of models (a 'set' to avoid duplicate models)"""
    
    return set(car_dict["model"] for car_dict in data if car_dict["automaker"] == automaker and car_dict["year"] == year)
