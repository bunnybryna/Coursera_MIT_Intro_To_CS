import random as rand
import string

class AdoptionCenter:
    """
    The AdoptionCenter class stores the important information that a
    client would need to know about, such as the different numbers of
    species stored, the location, and the name. It also has a method to adopt a pet.
    """
    def __init__(self, name, species_types, location):
        self.name = name
        self.species_types = species_types
        self.location = (float(location[0]),float(location[1]))
    def get_number_of_species(self, animal):
        if self.species_types.get(animal)== None:
            return 0
        else:    
            return self.species_types[animal]           
    def get_location(self):
        return self.location
    def get_species_count(self):
    # returns a copy of the full list and count of the available species at the adoption center
        return self.species_types.copy() 
    def get_name(self):
        return self.name
    def adopt_pet(self, species):
        if not self.species_types.get(species)== None:
             self.species_types[species] -= 1
             # if the number drops to 0, delete the key
             if self.species_types[species] == 0:
                del self.species_types[species]




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
           

def get_ordered_adoption_center_list(adopter, list_of_adoption_centers):
    """
    The method returns a list of an organized adoption_center such that the scores for each AdoptionCenter to the Adopter will be ordered from highest score to lowest score.
    """
    scoreDict = {}
    for adoptionCenter in list_of_adoption_centers:
        score = adopter.get_score(adoptionCenter)
        scoreDict[score] = adoptionCenter
    lst = scoreDict.keys()
    lst.sort(reverse=True)
    centerList = []
    for key in lst:
        center = scoreDict[key]
        centerList.append(center)
    return centerList

def get_adopters_for_advertisement(adoption_center, list_of_adopters, n):
    """
    The function returns a list of the top n scoring Adopters from list_of_adopters (in numerical order of score)
    """
    # Your Code Here 
    scoreDict = {}
    for adopter in list_of_adopters:
        score = adopter.get_score(adoption_center)
        name = adopter[0]
        scoreDict[score] = adopter.get_name()
    lst = scoreDict.keys()
    lst.sort(reverse=True)
    adopterList = []
    for key in lst:
        adopters = scoreDict[key]
        adopterList.append(adopters)
    for i in range(len(lst)-1):
        # two adopters who have the same score will be sorted alphabetically
        if lst[i]==lst[i+1] and adopterList[i] > adopterList[i]:
            adopterList[i] = adopterList[i+1]
            adopterList[i+1] = adopterList[i]
    if n >= len(list_of_adopters):
        return adopterList
    else:
        return adopterList[:n]


