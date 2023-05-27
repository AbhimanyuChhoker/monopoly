class City:
    def __init__(self, name, price, base_rent, owner, rent_multiplier, color_group, house_cost,
                 houses, mortgage_amount, mortgaged, type):
        self.name = name
        self.price = price
        self.base_rent = base_rent
        self.owner = owner
        self.rent_multiplier = rent_multiplier
        self.color_group = color_group
        self.house_cost = house_cost
        self.houses = houses
        self.mortgage_amount = mortgage_amount
        self.mortgaged = mortgaged
        self.type = type
        
    def buy(self, player):
        if player.money >= self.price:
            player.money -= self.price
            self.owner = player
        else:
            print("You don't have enough money to buy this city.")

    def trade(self, buyer, seller, selling_price):
        if seller.money >= selling_price:
            seller.money += selling_price
            self.owner = buyer
            buyer.money -= selling_price
        else:
            print("Buyer doesn't have enough money to buy this city.")

    def mortgage(self, player):
        self.mortgaged = True
        player.money += self.mortgage_amount

    def unmortgage(self, player):
        unmortgaging_amount = self.mortgage_amount + (1/10 * self.mortgage_amount)
        if unmortgaging_amount <= player.money:
            self.mortgaged = False
            player.money -= unmortgaging_amount
        else:
            print("You don't have enough money to unmortgage this city.")

    def construct_house(self, player):
        if self.house_cost <= player.money:
            player.money -= self.house_cost
            self.houses += 1
        else:
            print("You don't have enough money to construct house.")

class Player:
    def __init__(self, name, money, cities, current_position, total_wealth):
        self.name = name
        self.money = money
        self.cities = cities
        self.current_position = current_position
        self.total_wealth = total_wealth
        
