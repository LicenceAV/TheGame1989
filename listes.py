import random

def nation():
    """
    permet de choisir au hasard un pays

    Returns
    -------
    str
        pays choisis au hasard.

    """
    nation_file = open("nations.txt", "r")
    liste_nations = []
    for line in nation_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        liste_nations.append(line_list)
    return random.choice(liste_nations)[0]

def firstname():  
    """
    permet de choisir au hasard un prénom

    Returns
    -------
    str
        prénom choisis au hasard.

    """
    firstnames_file = open("firstnames.txt", "r")
    liste_firstnames = []
    for line in firstnames_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        liste_firstnames.append(line_list)  
    return random.choice(liste_firstnames)[0]

def lastname(): 
    """
    permet de choisir au hasard un nom de famille

    Returns
    -------
    str
        nom de famille choisis au hasard.

    """
    lastnames_file = open("lastnames.txt", "r")
    liste_lastnames = []
    for line in lastnames_file:
        stripped_line = line.strip()
        line_list = stripped_line.split()
        liste_lastnames.append(line_list) 
    return random.choice(liste_lastnames)[0]

  