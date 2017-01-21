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