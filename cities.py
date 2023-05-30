# Adds info about cities to json file by taking user info from user input

from classes import City
import json

cities_list = [
    "guwahati",
    "bhubaneshwar",
    "panaji",
    "agra",
    "vadodara",
    "ludhiana",
    "patna",
    "bhopal",
    "indore",
    "nagpur",
    "kochi",
    "lucknow",
    "chandigarh",
    "jaipur",
    "pune",
    "hyderabad",
    "ahmedabad",
    "kolkata",
    "chennai",
    "bengaluru",
    "delhi",
    "mumbai"
]

city_objects = []

for city_name in cities_list:
    city_dict = {"name": city_name}

    for attribute in ["price", "base_rent", "color_group", "house_cost", "mortgage_amount", "one_house_rent",
                      "two_house_rent", "three_house_rent", "four_house_rent", "five_house_rent"]:
        city_dict[attribute] = input(f"Enter the {attribute.replace('_', ' ')} for {city_name}: ")

    city_dict["owner"] = "bank"
    city_dict["houses"] = 0
    city_dict["mortgaged"] = False

    city = City(**city_dict)
    city_objects.append(city.__dict__)

with open('cities.json', 'w') as fp:
    json.dump(city_objects, fp)
