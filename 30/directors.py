import csv
from collections import defaultdict, namedtuple
import os
from urllib.request import urlretrieve
import string

BASE_URL = 'https://bites-data.s3.us-east-2.amazonaws.com/'
TMP = '/tmp'

fname = 'movie_metadata.csv'
remote = os.path.join(BASE_URL, fname)
local = os.path.join(TMP, fname)
urlretrieve(remote, local)

MOVIE_DATA = local
MIN_MOVIES = 4
MIN_YEAR = 1960

Movie = namedtuple('Movie', 'title year score')


def get_movies_by_director():
    """Extracts all movies from csv and stores them in a dict,
    where keys are directors, and values are a list of movies,
    use the defined Movie namedtuple"""

    director_dict = defaultdict(list)

    with open(local, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            try:
                year = int(row['title_year'])
            except:
                print("incorrect data format")

            director = row['director_name']
            title = row['movie_title'].strip(string.whitespace)
            score = float(row['imdb_score'])

            if year >= MIN_YEAR:
                movie_tuple = Movie(title, year, score)
                director_dict[director].append(movie_tuple)

    

    return director_dict


def calc_mean_score(movies):
    """Helper method to calculate mean of list of Movie namedtuples,
       round the mean to 1 decimal place"""
    
    mean_scores = sum(movie.score for movie in movies) / len(movies)

    return round(mean_scores, 1)


def get_average_scores(directors):
    """Iterate through the directors dict (returned by get_movies_by_director),
       return a list of tuples (director, average_score) ordered by highest
       score in descending order. Only take directors into account
       with >= MIN_MOVIES"""
    
    director_score = namedtuple('director', 'name score')

    average_scores = [director_score(director, calc_mean_score(movies)) 
                        for director, movies in directors.items() 
                        if len(movies) >= MIN_MOVIES]

    return sorted(average_scores, key=lambda director: director.score, reverse=True)
