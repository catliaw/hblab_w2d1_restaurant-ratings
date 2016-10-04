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
        name, rating = line.rstrip().split(":")
        # line = line.rstrip()
        # restaurant_info = line.split(":")
        # name, rating = restaurant_info
        restaurant_ratings[name] = rating

    def print_sorted_restaurants(restaurant_ratings):
        """Prints an alphabetically sorted list of restaurants and ratings"""
        # restaurants = sorted(restaurant_ratings.items())
        # for restaurant_name, restaurant_rating in restaurants:
        for restaurant_name, restaurant_rating in sorted(restaurant_ratings.items()):
            print "{} is rated at {}.".format(restaurant_name, restaurant_rating)


    def get_user_ratings(restaurant_ratings):
        """Asks the user for new restaurant ratings"""
        new_restaurant = raw_input("Enter a restaurant to add to the rating's list: ")
        new_rating = int(raw_input("Enter a number 1 through 5 to rate the restaurant: "))
        restaurant_ratings[new_restaurant] = new_rating
        return restaurant_ratings

    #create user_input as empty string
    #while not 3, do these things
    # if 1, elif 2, elif not 3 error message

    # def get_user_input():
    #     user_input = raw_input("Would you like to (1) see all restaurant ratings in alphabetical order, (2) add any restaurant and rate it, or (3) quit. Please enter 1, 2 or 3. ")
    #     return user_input

    user_input = ""

    while user_input != "3":
        user_input = raw_input("Would you like to (1) see all restaurant ratings in alphabetical order, (2) add any restaurant and rate it, or (3) quit. Please enter 1, 2 or 3. ")
        if user_input == "1":
            print_sorted_restaurants(restaurant_ratings)
        elif user_input == "2":
            get_user_ratings(restaurant_ratings)
            print_sorted_restaurants(restaurant_ratings)
        elif user_input != "3":
            print "Please enter a valid option."


get_restaurant_ratings(filename)