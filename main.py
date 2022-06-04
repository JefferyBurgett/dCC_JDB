#DayTripGenerator

#Lists

locations_list = ["Madison", "Green Bay", "Wisconsin Dells", "Chicago"]

#madison_restaurants_list = ["Sala Thai", "Sequoia", "Off Boradway", "Buck & Honey's"]

#green_bay_restaurants_list = ["Angelina", "Sushi Lover", "Our Place", "Al's Hamburger"]

#wisconsin_dells_restaurants_list = ["Paul Bunyan's", "Mexicali Rose", "Monk's", "Showboat Saloon"]

#chicago_restaurants_list = ["Portillo's", "Gibsons", "Gyu-Kaku", "Buona"]

transportation = ["Car","Train","Motorcycle","Bus"]

#madison_entertainment_list = ["Henry Vilas Zoo","Geology Museum","Olbrich Botanical Gardens","Capitol Tour"]

#green_bay_entertainment_list = ["Packers Hall of Fame","National Railroad Museum","Bay Beach Wildlife Sanctuary","Fox River Trail"]

#wisconsin_dells_entertainment_list = ["Noah's Ark","Ho-Chunk","Tommy Bartlett","Timber Falls Adventure Park"]

#chicago_entertainment_list = ["Grant Park","Art Institute","Willis Tower","Shedd Aquarium"]

#confirmed_trip_list = ["confirmed_location", "confirmed_transportation"]

restaurants = ["Wendy's","Culver's","Burger King","Chipotle"]
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
            print(f'You have choosen to keep {random_location} as your destination.')
            return random_location
        elif user_input == "n":
            return random_location_picker()
confirmed_location = random_location_picker()
print(confirmed_location)

def random_transportation_picker():
    random_transportation = random_item_picker(transportation)

    user_confirmed_one = False
    while user_confirmed_one == False:
        user_input = input(f'Would you like to keep {random_transportation} as your mode of transportation? y/n ')
        if user_input == "y":
            print(f'You have choosen to keep {random_transportation} as your mode of transportation.')
            return random_transportation
        elif user_input == "n":
            return random_transportation_picker()

confirmed_transportation = random_transportation_picker()
print(confirmed_transportation)

