class AllergicAdopter(Adopter):
    """
    An AllergicAdopter is extremely allergic to a one or more species and cannot
    even be around it a little bit! If the adoption center contains one or more of
    these animals, they will not go there.
    Score should be 0 if the center contains any of the animals, or 1x number of desired animals if not
    """
    def __init__(self, name, desired_species, allergic_species):
        # superclass.__init__(need argument inside!)
        Adopter.__init__(self, name, desired_species)
        self.allergic_species = allergic_species
        
    def get_score(self, adoption_center):
        self.normal_score = float(adoption_center.get_number_of_species(self.desired_species))
        for sp in self.allergic_species:
            if adoption_center.get_number_of_species(sp) > 0:
                return 0.0
            else:
                continue
        return self.normal_score


class MedicatedAllergicAdopter(AllergicAdopter):
    """
    A MedicatedAllergicAdopter is extremely allergic to a particular species
    However! They have a medicine of varying effectiveness, which will be given in a dictionary
    To calculate the score for a specific adoption center, we want to find what is the most allergy-inducing species that the adoption center has for the particular MedicatedAllergicAdopter. 
    To do this, first examine what species the AdoptionCenter has that the MedicatedAllergicAdopter is allergic to, then compare them to the medicine_effectiveness dictionary. 
    Take the lowest medicine_effectiveness found for these species, and multiply that value by the Adopter's calculate score method.
    """
    def __init__(self, name, desired_species, allergic_species, medicine_effectiveness):
        # superclass.__init__(need argument inside!)
        AllergicAdopter.__init__(self, name, desired_species, allergic_species)
        self.medicine_effectiveness = medicine_effectiveness
        
    def get_score(self, adoption_center):
        self.normal_score = float(adoption_center.get_number_of_species(self.desired_species))
        self.min = None
        for sp in self.medicine_effectiveness.keys():
            if adoption_center.get_number_of_species(sp) > 0:
                value = self.medicine_effectiveness[sp]
                if self.min is None:
                    self.min = value
                elif value < self.min:
                    self.min = value
            else:
                continue
        if self.min == None:
            return self.normal_score
        else:
            self.med_score = self.min    
            return self.med_score * self.normal_score


