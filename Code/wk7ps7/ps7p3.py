class Adopter:
    """ 
    Adopters represent people interested in adopting a species.
    They have a desired species type that they want, and their score is
    simply the number of species that the shelter has of that species.
    """
    def __init__(self, name, desired_species):
        self.name = name
        self.desired_species = desired_species
    def get_name(self):
    # returns the name of the adopter
        return self.name
    def get_desired_species(self):
    # returns the desired species of the adopter
        return self.desired_species
    def get_score(self, adoption_center):
    # need to be a float
        self.num_desired = adoption_center.get_number_of_species(self.desired_species)
        return float(1 * self.num_desired)
        
class FlexibleAdopter(Adopter):
    """
    A FlexibleAdopter still has one type of species that they desire,
    but they are also alright with considering other types of species.
    considered_species is a list containing the other species the adopter will consider
    Their score should be 1x their desired species + .3x all of their desired species
    """
    def __init__(self, name, desired_species, considered_species):
        # inherits from super class 
        Adopter.__init__(self,name, desired_species)
        self.considered_species = considered_species
        
    def get_score(self, adoption_center):
        self.adopter_score = adoption_center.get_number_of_species(self.desired_species)
        self.count = 0
        for sp in self.considered_species:
        # note here adoption_center.get_number_of_species() instead of AdoptionCenter.get_number_of_species
        # get_number_of_species is already a getting method, get_number_of_species(get,0) is wrong
            self.count += adoption_center.get_number_of_species(sp)
        self.num_other = self.count
        self.score = self.adopter_score + 0.3 * (self.num_other)
        return self.score
        


class FearfulAdopter(Adopter):
    """
    A FearfulAdopter is afraid of a particular species of animal.
    If the adoption center has one or more of those animals in it, they will
    be a bit more reluctant to go there due to the presence of the feared species.
    Their score should be 1x number of desired species - .3x the number of feared species
    """
    def __init__(self, name, desired_species,feared_species):
        # superclass.__init__(need argument inside!)
        Adopter.__init__(self, name, desired_species)
        self.feared_species = feared_species
        
    def get_score(self, adoption_center):
        self.adopter_score = adoption_center.get_number_of_species(self.desired_species)
        self.num_feared = adoption_center.get_number_of_species(self.feared_species)
        self.score = self.adopter_score - 0.3 * (self.num_feared) 
        # what if score is negative 
        if self.score < 0:
            return 0.0
        else:
            return self.score        