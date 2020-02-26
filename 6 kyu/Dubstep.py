#Kata name: Dubstep

#Kata link: https://www.codewars.com/kata/551dc350bf4e526099000ae5

#Kata description: Return the words of the initial song that Polycarpus used to make a dubsteb remix. Separate the words with a space.


def song_decoder(song):
    replacing = song.replace("WUB", " ")     #Replace "wub with a space"
    replacing = replacing.replace("  ", " ")    
    replacing = replacing.replace("  ", " ")
    return replacing.strip()                 #Remove whitespace before and after
