#Kata name: Growth of a Population

#Kata link: https://www.codewars.com/kata/563b662a59afc2b5120000c6/solutions/python

#Kata description: In a small town the population is p0 = 1000 at the beginning of a year.
#The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town.
#How many years does the town need to see its population greater or equal to p = 1200 inhabitants?
#p0, percent, aug (inhabitants coming or leaving each year), p (population to surpass)



def nb_year(p0, percent, aug, p):
    years = 0
    while p0 < p:
         p0 += (p0 * (percent / 100) + aug)
         years += 1
    return years
