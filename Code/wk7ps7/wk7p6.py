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
        scoreDict[key] = center
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
        name = adopter.name()
        scoreDict[score] = name
    lst = scoreDict.keys()
    lst.sort(reverse=True)
    adopterList = []
    for key in lst:
        scoreDict[key] = adopters
        adopterList.append(adopters)
    for i in range(len(lst)):
        # two adopters who have the same score will be sorted alphabetically
        if lst[i]=lst[i+1] and adopterList[i] > adopterList[i]:
            adopterList[i] = adopterList[i+1]
            adopterList[i+1] = adopterList[i]
    if n >= len(list_of_adopters):
        return adopterList
    else:
        return adopterList[:n]

        