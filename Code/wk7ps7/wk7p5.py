class SluggishAdopter(Adopter):
    """
    A SluggishAdopter really dislikes travelleng. The further away the
    AdoptionCenter is linearly, the less likely they will want to visit it.
    Since we are not sure the specific mood the SluggishAdopter will be in on a
    given day, we will asign their score with a random modifier depending on
    distance as a guess.
    Score should be
    If distance < 1 return 1 x number of desired species
    elif distance < 3 return random between (.7, .9) times number of desired species
    elif distance < 5. return random between (.5, .7 times number of desired species
    else return random between (.1, .5) times number of desired species
    """
    def __init__(self, name, desired_species, location):
        Adopter.__init__(self, name, desired_species)
        self.location = (float(location[0]),float(location[1]))
        
    def get_linear_distance(self, to_location):
        x1, y1 = self.location
        x2, y2 = to_location
        d = ((x1-x2)**2+(y1-y2)**2)**0.5
        return d
        
    def get_score(self, adoption_center):
        self.distance = self.get_linear_distance(adoption_center.get_location())
        self.num_desired = adoption_center.get_number_of_species(self.desired_species)
        if self.distance < 1:
            return float(self.num_desired)
        elif 1 <= self.distance < 3:
            return random.uniform(0.7, 0.9)*self.num_desired
        elif 3 <= self.distance < 5:
            return random.uniform(0.5, 0.7)*self.num_desired 
        elif self.distance >= 5:
            return random.uniform(0.1, 0.5)*self.num_desired     
           