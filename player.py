health = 3
money = 0
city = "Rangin"
place = "market"
weapon = "fist"
offhand = "fist"
armor = "leather armor"

class Player:
    def __init__(self, health, money, city, place, weapon, offhand, armor):
        self.health = health
        self.money = money
        self.city = city
        self.place = place
        self.weapon = weapon
        self.offhand = offhand
        self.armor = armor
Player = Player(health, money, city, place, weapon, offhand, armor)
print(Player.health, Player.money, Player.city, Player.place, Player.weapon, Player.offhand, Player.armor)
