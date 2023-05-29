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
 


guwahati = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
guwahati.__dict__

bhubaneshwar = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
bhubaneshwar.__dict__

chennai_central_railway_station = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
chennai_central_railway_station.__dict__

panaji = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
panaji.__dict__

agra = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
agra.__dict__

vadodara = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
vadodara.__dict__

ludhiana = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
ludhiana.__dict__

electric_company = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
electric_company.__dict__

patna = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
patna.__dict__

bhopal = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
bhopal.__dict__

howrah_railway_station = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
howrah_railway_station.__dict__

indore = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
indore.__dict__

nagpur = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
nagpur.__dict__

kochi = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
kochi.__dict__

lucknow = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
lucknow.__dict__

chandigarh = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
chandigarh.__dict__

jaipur = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
jaipur.__dict__

new_delhi_railway_station = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
new_delhi_railway_station.__dict__

pune = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
pune.__dict__

hyderabad = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
hyderabad.__dict__

water_works = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
water_works.__dict__

ahmedabad = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
ahmedabad.__dict__

kolkata = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
kolkata.__dict__

chennai = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
chennai.__dict__

bengaluru = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
bengaluru.__dict__

chhatrapati_shivaji_terminus = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
chhatrapati_shivaji_terminus.__dict__

delhi = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
delhi.__dict__

mumbai = City(name = str(input("Name: ").lower()),
price = int(input("Price: ")),
base_rent = int(input("Base rent: ")),
owner = "bank",
rent_multiplier = int(input("Rent multiplier: ")),
color_group = str(input("Color group: ").lower()),
house_cost = int(input("House cost: ")),
houses = 0,
mortgage_amount = int(input("Mortgage amount: ")),
mortgaged = False)
mumbai.__dict__

example_dict = {"name":"panaji"}

with open('cities.json', 'w') as fp:
    json.dump(example_dict, fp)