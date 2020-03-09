#Kata name: Pete, the baker

#Kata link: https://www.codewars.com/kata/525c65e51bf619685c000059

#Kata description: Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object)
#and returns the maximum number of cakes Pete can bake (integer). For simplicity there are no units for the amounts
#(e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present in the objects, can be considered as 0.


def cakes(recipe, available):
    if len(recipe) > len(available):        
       return 0
    total = []
    for x in recipe:
        temp = int(available[x] / recipe[x])        #How much you can make from 1 ingredient 
        total.append(temp)
    total = sorted(total)
    return total[0]        
