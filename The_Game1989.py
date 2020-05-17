import hasard
import phrases as ph
import random
import time as t
import characters as char
import matrix as booting
import listes as random_perso
import clear

nbr_tours = int
txt_used = [0]

fuite = False

#variables concernant les évenements aléatoires

cuisine_var = False




def cuisine():    
    """
    Fonction gérant le joker du joueur:
        remet les PV à 100 et la fatigue à 0

    Returns
    -------
    None.

    """
    print(ph.cuisine)
    personnage.vie = 100
    personnage.fatigue = 0
    if personnage.classe == "godmode":
        personnage.vie = 99999


def random_(n):
    """
    fonction de random

    Parameters
    ----------
    n : int
        valeur de la chance du personnage.

    Returns
    -------
    bool
        retourne True si l'un des n essaies est vrai.

    """
    for i in range(n):
        temp = random.randint(1,10)
        if temp == 4:
            return True
    
def combat(nround):
    """
    fonction gérant les combat du jeu

    Parameters
    ----------
    nround : int
        numéro du round.

    Returns
    -------
    None.

    Notes
    -------
    
    Basé sur une boucle while avec comme condition: la vie du personnage et de l'ennmie >0
        -Si le joueur a de la chance, il obtient un multi-hit
        -Le joueur choisis l'attaque qu'il veut faire
        -Si il a choisis la fuite, on vérifie s'il l'a déja utilisé ou non
        -Sinon on retire la valeur de l'attaque du joueur à la vie de l'énnemie 
            puis on affiche la vie de ce dernier
        -Puis l'ennemie attaque, on retire la valeur de son attaque à la vie 
            du joueur
        
        
        
        """
    e = char.ennemy(nround)
    print("La vie de votre ennemi est de:", round(e.vie))
    while personnage.vie > 0 and e.vie > 0:
        global fuite
        
        #multi hit
        nhit = 1
        if random_(personnage.chance):
            nhit = 3
            
        
        
        attaque = int(input(random.choice(ph.action)))
        
        if attaque == 5 and fuite == False:
            
            personnage.vie = 100
            personnage.fatigue = 0
            print(random.choice(ph.fuite))
            fuite = True
        
        elif attaque ==5 and fuite == True:
            print("Vous avez déja utilisez votre fuite, vous ne pouvez donc pas re-fuire !")
        
        else:
            if nhit == 3:
                print("MULTI-HIT !!!!")                
            e.vie -= nhit * personnage.make_attack(attaque)        
            print("\n",e)
            print(ph.separator)
        t.sleep(1)
        
        if e.vie > 0 and personnage.vie > 0:
            print("l'ennemie attaque ! \n")
            personnage.vie -= e.make_attack()
            print(personnage)
            t.sleep(1)



def choix(choix):
    """
    Fonction gérant le choix de la difficulté et de la classe du joueur
    Vérification si l'entrée du joueur correspond aux attentes
    Parameters
    ----------
    choix : str
        utilisé pour formaté la phrase du input, permet d'utilisé cette fonction 
        pour des choix différents.

    Returns
    ----------
    temp : str
        choix du personnage.

    """
    difficulties = ["facile","moyenne","difficile"]
    classes = ["chanceux intrépide","défenseur en béton","attaquant chevronné","godmode"]
    while True:
        temp = input("Quelle {} choisissez vous ? ".format(choix)).lower()
        if temp in difficulties or temp in classes:          
            return temp
            break
        else:
            print("Votre entrée n'est pas correcte, essayez de nouveau")   

def training():
    """
    Fonction gérant l'entrainement du joueur entre les combats
    Modifications des valeurs d'attaque et de défense de l'instance Personnage

    Returns
    -------
    None.

    """
    choix = int(input("\nVotre match désormais fini, vous avez maintenant le choix pour votre entrainement: Entraînement sac de frappe lourd (1), sac de frappe léger (2), sparring (3) ou vous reposer (4)\nVotre choix : "))
    if  choix == 1:
         personnage.attack[0] *= 1.25
         personnage.attack[1] *= 1.25
         personnage.attack[2] *= 1.50
         personnage.fatigue += 20
         print("\nVos attaques ont été améliorées, vous avez 20 pts de fatigue en plus.")
    elif choix == 2:
         personnage.attack[0] *= 1.50
         personnage.attack[1] *= 1.40
         personnage.attack[2] *= 1.10
         personnage.fatigue += 10
         print("\nVos attaques ont été améliorées, vous avez 10 pts de fatigue en plus.")
    elif choix == 3:
        personnage.fatigue += 10
        personnage.defense *= 1.2
        print("\nVotre défense a été améliorée, vous avez 10 pts de fatigue en plus.")
    elif choix == 4:
        personnage.fatigue = 0
        print("\nVous avez pu vous reposer, votre fatigue est désormais égale à 0")
        
def discover(classe):
    """
    Fonction gérant la découverte des combats avant de commencer le jeu

    Parameters
    ----------
    classe : str
        classe choisie par le joueur.

    Returns
    -------
    None.

    """
    global personnage #désolé pour ce global :( on avait pourtant réussi à ne pas en mettre jusque là
    for txt in ph.training:
        print(txt)
        input()
    personnage = char.Character(classe) 
    personnage.vie = 9999
    combat(5)
    
    print("Bravo, vous avez compris comment le système de combat fonctionne, l'histoire reprend:")
    t.sleep(3)
    


#####################_INIT_#############################
booting.booting() #Animation de démarrage


clear.clear()   
print(ph.dessine) #logo du jeu
print(ph.difficulté) #choix de la difficulté
difficulty = choix("difficulté")

clear.clear()

hasard.intro()
input()  
ph.debut()

print(ph.welcome2) # choix classe personnage princ.
classe = choix("classe").lower()

discover(classe) #présentation du système de combat

ph.debut2() #2e partie presentation

        
personnage = char.Character(classe)      #On créer notre objet personnage
 

if difficulty == "facile":  #entrée du nombre de tours suivant la difficulté choisie
    nbr_tours = 5
if difficulty == "moyenne":
    nbr_tours = 10
if difficulty == "difficile":
    nbr_tours = 15

######################_loop_############################

for nround in range(1,nbr_tours+1): #Boucle principale

    
    
    t.sleep(0.5)
    combat(nround)  #on appelle la fonction de combat
    
    if nround == nbr_tours: #Si on a fait le dernier combat, pas besoin de faire la suite: break de la boucle       
        break

        
    

    


    if personnage.vie <= 0: #Si le joueur n'a plus de vie, on imprime le texte de fin + break de la boucle
        for txt in ph.lose:
            print("Arbitre: ",txt)
            t.sleep(1)        
        break

    if not cuisine_var:     #Suivant la chance du personnage, il pourra avoir des petits bonus (vie au max et fatigue à 0)
        if random_(personnage.chance):
            cuisine()
            cuisine_var = True
    
  
    
    training()  #On appelle la fonction d'entrainement
        
    if nround == nbr_tours-1:   #lorsque le joueur est avant le dernier match, on print la suite de l'histoire
        for txt in hasard.fin:
            print(txt)
            t.sleep(1.5)
    elif nround < nbr_tours: #Pour le reste des temps inter-combats, on présente le prochain ennemie, toutes ses caractéristiques sont choisies grâce au hasard, sauf pour la vie et l'attaque qui dépende du round
        print("\n Now you are facing {} {} from {}.".format(random_perso.firstname(),random_perso.lastname(),random_perso.nation()))
    
    personnage.fatigue *= 0.7 #entre chaque combat, le joueur perd 30% de sa vie

clear.clear()    
if personnage.vie > 0:
    print(hasard.end)
    print(ph.boxeur)
else:
    print("Tu as perdu....")