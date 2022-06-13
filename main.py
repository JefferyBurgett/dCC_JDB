#DayTripGenerator

#Lists

locations_list = ["Madison", "Green Bay", "Wisconsin Dells", "Chicago"]

transportations_list = ["Car","Train","Motorcycle","Bus"]

restaurants_list = ["Wendy's","Culver's","Burger King","Chipotle"]

entertainments_list = ["Hiking","Concert","Shopping","Cinema"]
import random

def random_item_picker(list):
    random_item = random.choice(list)
    return random_item


def random_location_picker():
    random_location = random_item_picker(locations_list)
    
    user_confirmed = False
    while user_confirmed == False:
        user_input = input(f'Would you like to keep {random_location} as your destination? y/n ')
        if user_input == "y":
            print(f'You have chose to keep {random_location} as your destination.')
            return random_location
        elif user_input == "n":
            return random_location_picker()
confirmed_location = random_location_picker()
print(confirmed_location)

def random_transportation_picker():
    random_transportation = random_item_picker(transportations_list)

    user_confirmed_one = False
    while user_confirmed_one == False:
        user_input = input(f'Would you like to keep {random_transportation} as your mode of transportation? y/n ')
        if user_input == "y":
            print(f'You have chose to keep {random_transportation} as your mode of transportation.')
            return random_transportation
        elif user_input == "n":
            return random_transportation_picker()

confirmed_transportation = random_transportation_picker()
print(confirmed_transportation)

def random_restaurant_picker():
    random_restaurant = random_item_picker(restaurants_list)

    user_confirmed = False
    while user_confirmed == False:
        user_input = input(f'Would you like to keep {random_restaurant} as your eating destination? y/n ')
        if user_input == "y":
            print(f'You have chose to keep {random_restaurant} as your mode of destination.')
            return random_restaurant
        elif user_input == "n":
            return random_restaurant_picker()

confirmed_restaurant = random_restaurant_picker()
print(confirmed_restaurant)

def random_entertainment_picker():
    random_entertainment = random_item_picker(entertainments_list)
    
    user_confirmed = False
    while user_confirmed == False:
        user_input = input(f'Would you like to keep {random_entertainment} as your entertainment choice? y/n ')
        if user_input == "y":
            print(f'You have chose to keep {random_entertainment} as your choice of entertainment')
            return random_entertainment
        elif user_input == "n":
            return random_entertainment_picker()

confirmed_entertainment = random_entertainment_picker()
print(confirmed_entertainment)

print(f"You have chosen {confirmed_location}, {confirmed_transportation}, {confirmed_restaurant} and {confirmed_entertainment} for your Day Trip")