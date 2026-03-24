# Contributors: 
# Main file for the Pokemon Project for IS 303

# Tyler - Move Classes


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