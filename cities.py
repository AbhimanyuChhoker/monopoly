from classes import City
import json

cities_list = [
    "guwahati",
    "bhubaneshwar",
    "chennai_central_railway_station",
    "panaji",
    "agra",
    "vadodara",
    "ludhiana",
    "electric_company",
    "patna",
    "bhopal",
    "howrah_railway_station",
    "indore",
    "nagpur",
    "kochi",
    "lucknow",
    "chandigarh",
    "jaipur",
    "new_delhi_railway_station",
    "pune",
    "hyderabad",
    "water_works",
    "ahmedabad",
    "kolkata",
    "chennai",
    "bengaluru",
    "chhatrapati_shivaji_terminus",
    "delhi",
    "mumbai"
]

city_objects = []

for city_name in cities_list:
    city_dict = {}
    city_dict["name"] = city_name

    for attribute in ["price", "base_rent", "rent_multiplier", "color_group", "house_cost", "mortgage_amount"]:
        city_dict[attribute] = int(input(f"Enter the {attribute.replace('_', ' ')} for {city_name}: "))

    city_dict["owner"] = "bank"
    city_dict["houses"] = 0
    city_dict["mortgaged"] = False

    city = City(**city_dict)
    city_objects.append(city.__dict__)

with open('cities.json', 'w') as fp:
    json.dump(city_objects, fp)
