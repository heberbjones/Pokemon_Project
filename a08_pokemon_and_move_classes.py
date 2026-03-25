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
#carl test