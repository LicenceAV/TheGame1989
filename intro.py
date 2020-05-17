import random as r

"""
définitions des listes contenant les evenements/lieux/personnages, utiles pour la suite
"""

lieu = ["au LAUM", "au Mans", "au Zimbawe", "au Machou Pichou", "au DAUM", "en France", "au Nord-pas-de-Calais", "a Paris", "a Warzazat", "à l'assemblée nationale",  ]
date = [" il y a fort longtemps", "lors des JO de Los Angeles", "lors de la coupe du monde 2018", "lors de la crucifixion de Jesus", "en 1995", "pendant le confinement", "pendant la troisième guerre mondiale", "pendant la révolution française"]
terriblechose = [" le communisme", "les résultats de fin de projet python", "la guerre", """la montée en puissance des gens qui disent 'comme même'""""", "l'élection de Jean Lasalle", "la dernière mutation du Covid-19", "la pénurie de papier toilette", "la cérémonie des oscars présentée par Weinstein", "que l'homme qui dit dans la pub 'je mange mon chapeau' à mangé son chapeau", "le clash booba-kaaris", "la fin des choux", "le ramadan", "la fête du jambon à Alger", "la canicule en décembre"]
personnageP = ["Zindim Zibdane", "Bill Portail", "Elonne Musque", "Jeffrey Baisos", "François Groland", "Bertrand Leheureux", "Pierre Olive", "Nicolat Hublot", "Emmanuel Macaron", "Philippe Edouard", "Jean-Luc Jesuisronchon", "Louis deFitness", "Quad Merad", "Narine Morano", "Baraque Obamot", "Michael Baie", "Vladimir Tabernac Poutine", "John lanone", "Nelson Mandala", "Tom Croisière", "Angelina Moche", "Donny Jepp", "Vin Sansplomb95", "Christophe Héro"]
metier = ["stripteaseur(e)", "comptable", "president de la republique du congo", "professeur(e)", "eleve en L1AV", "mécano", "agent secret", "marin d'eau douce", "bucheron"]
verbe = ["violenté", "emprisonné", "empoisonné", "tué", "assassiné", "mordu", "giflé", "tapoté avec le doigt", "fait un dab sur", "dit chocolatine à", "genré", "piétinné","""dit "bananée" lors du décompte de la nouvelle année en 1995 à"""  ]
appar = ["femme", "virginité", "maison", "arbre généalogique", "semestre", "chaise ogaming magnififque", "maman", "père", "agenda de la redoute", "calendrier avec des châtons des pompiers", "carte graphique RTX dernière génération 11go en GDDR6 cadencée à 1635 Mhz 2080ti", "comptable", "prépuce", "enceinte L-Acoustics X15 Hiq" ]


"""
Cette partie permet de choisir au hasard les personnages/évenements/lieux liés à l' histoire.
Chaque partie a donc une histoire complètement différente grâce à ce principe. 
Les .sample font une liste permettant de selectionner plusieurs fois au hasard.
"""
ou = r.choice(lieu) 
dat = r.choice(date)
ter = r.choice(terriblechose)
met = r.choice(metier)
ver = r.sample(verbe, 5)
ap = r.sample(appar,2)
P = r.sample(personnageP, 5)
    
    
fin = ["Après votre match un visiteur masqué vous attend dans le vestiaire...\n\nVisiteur masqué : Bravo, {}, je vois que vous vous êtes beaucoup entrainé".format(P[0]),
       "Vous : Qui êtes vous ?",
       "Visitante enmascarado: te he estado observando durante mucho tiempo, mi querido {}, especialmente desde {} en {} tu {} ... \ nTú: deja mi {} solamente !\nLoading...".format(P[0],P[1],ver[0],ap[0],ap[0]),
       "Visiteur masqué : Ne t'inquiète pas {}, après avoir {} votre {} je vais pouvoir {} votre {} une fois que je t'aurais battu\n\nVous avez enfin la chance de vous battre contre votre ennemi donnez tout !".format(P[0],ver[0],ap[0],ver[1],ap[1])
       ]

end = "{} : Ce n'est pas possible tu ne peux pas être aussi fort {}, tout ça à cause d'avoir {} ton/ta {} ?\nVous tuez votre pire ennemi.\nLe jeu de c'est la fin\nTHE HAND".format(P[1], P[0], ver[0], ap[0])

def intro():  
    
    print(f"{ou} {dat}, il est arrivé une terrible chose : {ter}. Vous incarnez {P[0]} qui était {met} avant que le monde bascule. Depuis, {ou}, c'est le règne de la violence et les gens rafolent du nouveau sport très violent, le Fight Until Comes Death (FUCD), où le principe consiste à taper l'adversaire jusque mort s'en suive... {ter} à rendu le monde fou et vous aussi. Vous participez maintenant à ces combats. Depuis que {P[1]}, boxeur de FUCD, à {ver[0]} votre {ap[0]} vous vous destinez à aller le tuer. Pour se faire vous avez recruté le meilleur coach {P[2]}. Assez parlé vous êtes actuellement à la finale régionale de FUCD allez vous battre !\n")
    print("Appuyez sur entrer lorsque vous avez fini de lire")


if __name__ == "__main__":
    intro()
    for txt in fin:
        print(txt)