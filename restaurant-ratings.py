#!/usr/bin/python
from sys import argv
filename = argv[1]

#PSEUDOCODE

#Read file
#Create an empty dictionary
#Read each line and .rstrip
#Split line into list (delimiter :)
#For each list, convert into dictionary entry
#Use .iteritems() to create a list of tuples
#Use sorted on list of tuples
#Print with sentence


def get_restaurant_ratings(filename):
    """Takes a .txt file with restaurant names and ratings and prints name and rating"""

    raw_scores = open(filename)
    restaurant_ratings = {}

    for line in raw_scores:
        line = line.rstrip()
        restaurant_info = line.split(":")
        name, rating = restaurant_info
        restaurant_ratings[name] = rating
    
    restaurants = sorted(restaurant_ratings.items())

    for restaurant_name, restaurant_rating in restaurants:
        print "{} is rated at {}.".format(restaurant_name, restaurant_rating)

get_restaurant_ratings(filename)