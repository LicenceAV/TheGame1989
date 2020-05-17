import random
import numpy as np

class Character:   
    def __init__(self, classe = 'attaquant chevronné'):
        """
        initialisation de l'instance'

        Parameters
        ----------
        classe : str, optional
            classe choisie par le joueur. The default is 'attaquant chevronné'.

        Returns
        -------
        None.

        """

        self.classe = classe
        self.vie = 100
        self.argent = 20
        self.fatigue = 0
        self.xp = [0,0,0]        
        if classe == 'chanceux intrépide':            
            self.attack = [10,15,30]            
            self.chance = 3        
            self.defense = 20
        if classe == 'attaquant chevronné':
            self.chance = 1
            self.attack = [35,40,50]                        
            self.defense = 20            
        if classe == 'défenseur en béton':
            self.chance = 2
            self.attack = [10,20,30]            
            
            self.defense = 50
            
        if classe == 'godmode':
            self.attack = [10000,10000,10000]            
            self.vie = 99999
            self.defense = 10000
            self.chance = 2

           
    def make_attack(self, attaque):
        """
        Permet d'avoir la valeur de l'attaque du personnage
        
        Parameters
        ----------
        attaque : int
            attaque choisie par le joueur.

        Returns
        -------
        float
            valeur de l'attaque.

        """
        self.fatigue -= 15
        if self.fatigue <100:
            self.power_up(attaque)
            
            if self.fatigue <0:
                self.fatigue = 0
            if attaque == 1:   
                self.fatigue += 10
                return int(self.attack[0]) + random_attack(self.chance)
            
            if attaque == 2:
                self.fatigue += 20                
                return int(self.attack[1]) + random_attack(self.chance)
               
            if attaque == 3:    
                self.fatigue += 50
                return int(self.attack[2]) + random_attack(self.chance)
        if attaque == 4:
            self.vie += self.defense
            return 0
            
            
        

        print("vous êtes trop fatigués, vous ne pouvez donc pas attaquer. Attendez un tour")
        return 0
    
    def __str__(self):
        """
        permet d'afficher les caractéristique du personnage

        Returns
        -------
        str
            phrase à afficher.

        """
        try:
            vie=round(self.vie/10)
            barre_vie = ["." for i in range(10)]
            for i in range(vie):
                barre_vie[i] = "*"
            return "Votre vie: {} \nVotre fatigue: {:.1f} \n".format("".join(barre_vie),self.fatigue)    
        except IndexError:
            return "Votre vie est infinie \nvotre fatigue est de: {}".format(self.fatigue)
            
        
        
            
    def power_up(self,attaque):
        """
        Compte les attaques utilisées et les fait évoluer

        Parameters
        ----------
        attaque : int
            l'attaque choisie par le joueur.

        Returns
        -------
        None.

        """

        
        if attaque == 1:
            self.xp[0] += 1
        if attaque == 2:
            self.xp[1] += 1
        if attaque == 3:
            self.xp[2] += 1
            
        for (index,i) in enumerate(self.xp):
            if int(i) >= 5:
                self.attack[index] += 1
                print("attaque {} level up".format(index+1))
                self.xp[index] = 0
                
                
                
class ennemy:
    
    def __init__(self, nround):
        """
        Initialisation de l'instance ennemy

        Parameters
        ----------
        nround : int
            numéro du round.

        Returns
        -------
        None.

        """
        
        self.attack = 10 * (nround*1.05)
        self.vie = 30*np.log(10*nround+5)   #voir image dans A LIRE AVANT DE LANCER en bas de page
    def make_attack(self):
        """
        Methode pour avoir la valeur d'attaque

        Returns
        -------
        float: la valeur de l'attaque.

        """
        return self.attack    
    
    def __str__(self):
        """
        Methode permettant d'afficher la vie de l'ennemie

        Returns
        -------
        str: phrase + vie si vie>0.

        """
        if self.vie > 0:
            return "La vie de votre ennemie est {:.1f}".format(round(self.vie))        
        else:
            return "La vie de votre ennemie est égale à 0"   
        
        
def random_attack(chance):
    """
    

    Parameters
    ----------
    chance : float
        la valeur de chance du personnage.

    Returns
    -------
    float
        valeur d'attack random du personnage (qui s'ajoute à sa valeur d'attaque normale).

    """
    temp = 0
    for n in range(chance):
        temp += random.randint(1,10)
    return temp
    #TODO à décider
    """
    OU
    
    return temp(5,chance)
    
    """        

      
                
                