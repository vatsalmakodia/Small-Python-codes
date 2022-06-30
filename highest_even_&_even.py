# finding the highest even number of the given list
def highest_even(list):
    evens = []
    for items in list:
        if items % 2 == 0:
            evens.append(items)
    return max(evens)

print(highest_even([1,2,3,4,5,6,7,8,8,10,29,26,50]))

# finding the highest odd number of the given list
def highest_odds(list):
    odds=[]
    for items in list:
        if items % 2 != 0:
            odds.append(items)
    return max(odds) 

print(highest_odds([1,2,3,4,5,6,7,8,9,11,12,13,1,45,67,8]))