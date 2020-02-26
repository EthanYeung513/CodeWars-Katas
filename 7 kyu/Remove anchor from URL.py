#Kata name: Remove anchor from URL

#Kata link: https://www.codewars.com/kata/51f2b4448cadf20ed0000386

#Kata description: Complete the function/method so that it returns the url with anything after the anchor (#) removed.





def remove_url_anchor(url):
    newString = ""
    for x in url:         #Go through string and add every character UNTIL there's       
        if x == "#":      #a "#", then it returns the string
           return newString
        else:
           newString += x
    return newString
