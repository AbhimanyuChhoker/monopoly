class City:
    def __init__(self, name, price, base_rent, owner, rent_multiplier, color_group, house_cost,
                 houses, mortgage, mortgaged, type):
        self.name = name
        self.price = price
        self.base_rent = base_rent
        self.owner = owner
        self.rent_multiplier = rent_multiplier
        self.color_group = color_group
        self.house_cost = house_cost
        self.houses = houses
        self.mortgage = mortgage
        self.mortgaged = mortgaged
        self.type = type
        
    def buy(self, player):
        pass
    
    def sell(self, player):
        pass

    def mortgaged(self, player):
        pass

    def unmortgaged(self, player):
        pass

    def construct_house(self, player):
        pass

class Player:
    def __init__(self, name, money, cities, current_position, total_wealth):
        self.name = name
        self.money = money
        self.cities = cities
        self.current_position = current_position
        self.total_wealth = total_wealth
        
