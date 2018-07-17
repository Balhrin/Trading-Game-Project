from random import randint
# définition des variables
wheat = 0
iron = 0
wool = 0
wheat_variation = 0
wool_variation = 0
iron_variation = 0

class city:
    def __init__(self, name, market, shop, wheat, wool, iron, wheat_variation, wool_variation, iron_variation):
        self.name = name #définition du nom
        self.market = True #présence d'un marché
        self.shop = True #présence d'un magasin
        self.wheat = wheat #prix initial du blé
        self.wool = wool #prix initial de la laine
        self.iron = iron #prix initial du fer

# variation des prix propres à chaque ville

        self.wheat_variation = wheat_variation
        self.wool_variation = wool_variation

        self.iron_variation = iron_variation
# fonction permettant de randomiser les prix par ville, de les sauvegarder puis de les afficher

    def price_update(self, wheat, iron, wool, wheat_variation, iron_variation, wool_variation):
        wheat = wheat + wheat_variation
        iron = iron + iron_variation
        wool = wool + wool_variation
        self.iron = iron
        self.wheat = wheat
        self.wool = wool
        print ("wool: " + str(wool))
        print("wheat: " + str(wheat))
        print("iron" + str(iron))

#définition de la ville de Rangin

Rangin = city("Rangin", True, True, 5, 15, 50, randint(-2,5), randint(-5,2), randint(-15,3))

#mise à jour des prix pour Rangin

Rangin.price_update(Rangin.wheat, Rangin.iron, Rangin.wool,Rangin.wheat_variation, Rangin.iron_variation, Rangin.wool_variation)
print(Rangin.wheat, Rangin.iron, Rangin.wool, Rangin.name, Rangin.shop, Rangin.market) #test du module
