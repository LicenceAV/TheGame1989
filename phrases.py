import time as t

difficulté = "Avant de commencer, veuillez tout d'abord choisir la difficulté du jeu (Facile, Moyenne ou Difficile)"
welcome2 = """Veuillez choisir votre nouveau style de jeu : Chanceux intrépide, Attaquant chevronné, ou Défenseur en bêton (ou GODMODE)."""
cuisine = "Vous avez de la chance, le test de produits dopants est cassé ; votre vie est de nouveau à 100 et votre fatigue à 0"
separator = "------------------------------------------------------------"


training = ["\nTout d'aborrrrd, nous going to expliquer comment fonfonctionne le SystEme dE comBat via un fight d'entrainement, tu seras en mode GODMODE pour les prochains rounds ERROR... (appuie sur entrer pour papasser à la suite)",
            "Ton personnage ERROR à plusieurs caracteristicas qui dépendent de la cLaSSe que tu as choisiE: la chance, la valeur d'attaque, la valeur de défense, ta vie ainsi que votRe fatigue.",
            "Tù ES le premier à attaquer, tu as CINQ choix: l'attaque faible, moyenne, FuerTE, la défense, et la fuite. Si ERROR tu attaqueS, la fatigue de ton personnage augMenteras, si elle atTEint 100, tu ne PouRras plus attaquer, cependant tu perds 15 pts de fatigue à chaque round (il est donc bon de noter que tu ne pourras jamais être trop fatiguer en utilisant l'attaque 1). Choisir la défense ne te feras pas attaquer (donc pas de fatigue supplémentaire) mais tu perderas moins de vie. La fuite est un joker qui te feras reprendre tous tes PV, mais attention, tu ne peux l'utiliser qu'une seule foix.",
            "Entre chaque combat tu as une certaine chance d'avoir des avantages (comme - d'ennemis, ou ta vie remise à 100) ou des inconcénients. CeEci ERROR dépendras de ta chance, et par conséquence de la classe que TU AS choisiE",    
            "Après chaque ComBAt tu auras égaleMent l'occasion de faire un entrainement qui te permettras d'améliorer tes attaques ou tes défenses, mais ces entrainements te fatiguerons, tu pourras donc ERROR choisir de ne pas en faire et ainsi te reposer.",    
            "Voici un combat d'exEMPLE, tu es dans la classe que tu as choisis juste avant, mais avec une vie ILLIMITED"
            ]
    

dessine = ("""  ________                                                
 /  _____/ _____     _____    ____                        
/   \  ___ \__  \   /     \ _/ __ \                       
\    \_\  \ / __ \_|  Y Y  \\  ___/                       
 \______  /(____  /|__|_|  / \___  >                      
        \/      \/       \/      \/                       
 __      __         .__                                   
/  \    /  \  ____  |  |    ____   ____    _____    ____  
\   \/\/   /_/ __ \ |  |  _/ ___\ /  _ \  /     \ _/ __ \ 
 \        / \  ___/ |  |__\  \___(  <_> )|  Y Y  \\  ___/ 
  \__/\  /   \___  >|____/ \___  >\____/ |__|_|  / \___  >
       \/        \/            \/              \/      \/ 
  __              __   .__                                
_/  |_  ____    _/  |_ |  |__    ____                     
\   __\/  _ \   \   __\|  |  \ _/ __ \                    
 |  | (  <_> )   |  |  |   Y  \\  ___/                    
 |__|  \____/    |__|  |___|  / \___  >                   
                            \/      \/                    """)
"""
le thème de notre jeu est "un jeu qui bug" nous avons décider de changer de langues pour certains textes redondants, la phrase en français est mise plusieurs fois pour avoir une plus haute probabilité d'être tirée (75% de français)
"""
action = ["C'est à toi d'attaquer, quelle action veux tu faire ? (1) pour l'attaque faible, (2) pour l'attaque moyenne, (3) pour l'attaque puissante, (4) pour la défense et (5) pour la fuite \nVotre choix : ",
          "C'est à toi d'attaquer, quelle action veux tu faire ? (1) pour l'attaque faible, (2) pour l'attaque moyenne, (3) pour l'attaque puissante, (4) pour la défense et (5) pour la fuite \nVotre choix : ",
          "C'est à toi d'attaquer, quelle action veux tu faire ? (1) pour l'attaque faible, (2) pour l'attaque moyenne, (3) pour l'attaque puissante, (4) pour la défense et (5) pour la fuite \nVotre choix : ",
          "C'est à toi d'attaquer, quelle action veux tu faire ? (1) pour l'attaque faible, (2) pour l'attaque moyenne, (3) pour l'attaque puissante, (4) pour la défense et (5) pour la fuite \nVotre choix : ",
          "C'est à toi d'attaquer, quelle action veux tu faire ? (1) pour l'attaque faible, (2) pour l'attaque moyenne, (3) pour l'attaque puissante, (4) pour la défense et (5) pour la fuite \nVotre choix : ",
          "C'est à toi d'attaquer, quelle action veux tu faire ? (1) pour l'attaque faible, (2) pour l'attaque moyenne, (3) pour l'attaque puissante, (4) pour la défense et (5) pour la fuite \nVotre choix : ",
          "Depende de usted atacar, ¿qué acción quiere tomar? (1) para ataques débiles, (2) para ataques medianos, (3) para ataques poderosos, (4) para defensa y (5) para la fuga\nSu elección : ",
          "Es liegt an Ihnen anzugreifen, welche Aktion möchten Sie ausführen? (1) für schwache Angriffe, (2) für mittlere Angriffe, (3) für mächtige Angriffe, (4) für Verteidigung und (5) für das Leck \nIhre Wahl : "]

fuite = ["Le moine en fuite n'échappe pas à son monastère","A ne rien espérer d'immortel te convie la fuite de l'année","Il n'y a qu'un remède à l'amour : la fuite.","Le soldat doit avoir assaut de lévrier, fuite de loup, défense de sanglier.", "Mourir en combattant sied mieux au soldat qu’être libre dans la fuite.", "Moi, je suis assez partisan de la fuite. Je trouve ça très beau"]
dessin = """            _______
    _-_-  _/\______\\__
 _-_-__  / ,-. -|-  ,-.`-.
    _-_- `( o )----( o )-'
           `-'      `-'"""
debut1 = ["*bruit de foule*",
          "coach : réveilles toi bon sang de bonsoir",
          "arbitre : 5...",
          "arbitre : 6...ERROR",
          "arbitre : 7...",
          "coach : Tu vas pas abandonner si prêt du but !",
          "*bruit de foule s'intensifie*",
          "\narbitre : 10 ! Victoire par KO.",
          "     Dans le vestiaire...\n",
          "coach : Tu te rends compte que tu viens de perdre le\ntitre de champion du monde des titres poids lourds?",
          "coach : Je t'écoute même pas il n'y a pas d'excuses possible...les défaites ça ne peut plus durer\ncoach : Aller je te raccompagne chez toi",
          dessin,
          "     Chez vous....\n",
          "Cela ne peut plus durer ... j'échoue chaque année... Il me faut une nouvelle stratégie\n"]

debut_2 = ["L'intersaison est passée et vous vous sentez prêt comme jamais",
           "\nVous recevez un message de votre coach qui vous invite pour un nouveau match\nVous aller le rejoindre",
           dessin,
           "coach : J'ai une bonne nouvelle, les matchs reprennent",
           "voilà ton premier adversaire",
           "Jean Baguette - 1m76 - 86 kls - Français",
           "Points forts : Des bras longs comme des baguettes, rapide sur les appuis",
           "Points faibles : Se rend facilement si il se prends un gros coup",
           "coach : Le match à lieu demain. Soit prêt",
           separator,
           "     Le lendemain JOUR DE MATCH....",
           "coach : Aller oublies pas ses points forts et faibles ! il t'aideront à gagner",
           "arbitre : Messieurs j'attends de vous des coups bas et uppercuts derrière la tête. Bon match et mourrez vite",
           " *cling cling* ROUND 1 "]

lose = ["5","6","7","8","9","10 !  Le joueur a perdu !"]

boxeur = ("""
               /////'                 
              '  # o
              C   - |
 ___          '  =__'        ___
(` _ \_       |   |        _/  ')
 \  (__\  ,---- _ |----.  /__)- |
  \__  ( (           /  ) )  __/
    |_X_\/ \.   #  _.|  \/_X_|
      |  \ /(   /    /\ /  |
       \ /  (  ,    /  \ _/
            /______/
           [:::::::]
          /*%*%*%*%*\              
          >%*%#%*%*%|               
         /%*%*#*%*%*\               
        ######^######              
                                    """)


def debut():
    """
    1ere partie du dialogue de début

    Returns
    -------
    None.

    """
    for i in range(6):
        print(debut1[i])
        t.sleep(1.5)
    
    choose=str(input("Que voulez vous faire :\n A-Vous relever\n B-Abandonner le combat\nVotre choix : "))
    if choose=="A":
        print("Vous titubez mais votre énergie est trop basse et tombez devant la foule en délire...")
        t.sleep(1.5)
         
    for i in range(7,10):
        print(debut1[i])
        t.sleep(1.5)
    
    str(input("Votre réponse : "))
    
    for i in range(10,14):
        print(debut1[i])
        t.sleep(1.5)
        
def debut2():
    """
    2ere partie du dialogue de début

    Returns
    -------
    None.

    """
    for i in debut_2:
        print(i)
        t.sleep(1.5)
        
if __name__ == "__main__":
    # debut()
    # print(separator)
    # debut2()
    pass