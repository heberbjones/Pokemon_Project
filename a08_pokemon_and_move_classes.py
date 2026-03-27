# Contributors: 
# Main file for the Pokemon Project for IS 303

import random

# Tyler - Move Classes

class Move :
    def __init__(self, sMove_name, sElemental_type, iLow_attack_points, iHigh_attack_points):
        self.move_name = sMove_name
        self.elemental_type = sElemental_type
        self.low_attack_points = iLow_attack_points
        self.high_attack_points = iHigh_attack_points
    
    def get_info (self) :
        return f"{self.move_name} (Type: {self.elemental_type}): {self.low_attack_points} to {self.high_attack_points} Attack Points"
    
    def generate_attack_value (self) :
        return random.randint(self.low_attack_points, self.high_attack_points)

# Heber - Pokemon Classes

class Pokemon :
    def __init__(self, sName, sElemental_type, iHit_points):
        self.Name = sName
        self.Elemental_type = sElemental_type
        self.Hit_points = iHit_points

    def get_info (self) :
        return f'Name: {self.Name} | Element Type: {self.Elemental_type} | Hit Points: {self.Hit_points}'   

    def heal (self) :
        self.Hit_points += 15
        print(f'Updated Hit Points: {self.Hit_points}')     


# Carl - Main program
# Create 9 Move objects
tackle = Move("Tackle", "Normal", 5, 20)
quick_attack = Move("Quick Attack", "Normal", 6, 25)
slash = Move("Slash", "Normal", 10, 30)
flamethrower = Move("Flamethrower", "Fire", 5, 30)
ember = Move("Ember", "Fire", 10, 20)
water_gun = Move("Water Gun", "Water", 5, 15)
hydro_pump = Move("Hydro Pump", "Water", 20, 25)
vine_whip = Move("Vine Whip", "Grass", 10, 25)
solar_beam = Move("Solar Beam", "Grass", 18, 27)

#List of moves 
# Put all 9 moves in a list
move_list = [tackle, quick_attack, slash, flamethrower, ember,
             water_gun, hydro_pump, vine_whip, solar_beam]

#create a loop that runs through 3 times
for i in range(3):
    #Choose a random move from the move list
    aSingleMove = random.choice(move_list)
    #Print info about the random move
    print(aSingleMove.get_info())
    #Print the generated attack value
    print(f"Generated attack value: {aSingleMove.generate_attack_value()}")
    #remove the move so it is not repeated
    move_list.remove(aSingleMove)

#add a pause
input("Press enter to continue...") 


#make 3 pokemon objects
oBulbasur = Pokemon("Bulbasaur", "Grass", 60)
oCharmander = Pokemon("Charmander", "Fire", 55)
oSquirtle = Pokemon("Squirtle", "Water", 65)

#print charmander info before healing
print(oCharmander.get_info())
#call heal function
oCharmander.heal()
#print charmander info after healing
print(oCharmander.get_info())

#create a list of the pokemon objects to loop through
pokemon_objects_list = [oBulbasur, oCharmander, oSquirtle]
#for pokemon objects in list of pokemon objects, print their info
for pokemon in pokemon_objects_list:
    print(pokemon.get_info())




