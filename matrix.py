import random
import time
import clear

def booting():
    """
    Fonction gérant le booting du jeu au démarrage:
        Génération et affichage de charactères au hasard

    Returns
    -------
    None.

    """
    symbols = ["0","1"," "," ","#","@","}","`"," ","&","*",">"]
    
    
    clear.clear()
    
    booting = ["booting","booting.","booting..","booting..."]
    for i in range(3):
        for txt in booting:
            clear.clear()
            print(txt)
            time.sleep(0.5)
    def booting(w):        
        line = ""
        counter = 0
        for i in range(w):
            for y in range(118):
                line += random.choice(symbols)
                counter +=1
            print(line)
            line = ""
            time.sleep(0.03)
    booting(100)    
    for i in range(20):
        print('\033[91m'+"ERROR: CANNOT LOAD JDR_GAME.exe FILE CORRUPTED PLS RETRY")
        time.sleep(0.1)
    time.sleep(1)
    print(">>THE SYSTEM DID NOT SUCCEED TO BOOT"+'\033[0m')
    time.sleep(1)    
    print("DO YOU WANT TO START IN SAFE MODE ? SOME SEVERE BUGS MAY APPEAR")
    input("yes or no : ")
    print("OK BOOTING THE SYSTEM IN SAFE MODE, PLS WAIT")
    time.sleep(2)
    booting(75)
    print("\n GAME BOOTED IN SAFE MODE, YOUR SAVE IS CORRUPTED, SOME BUGS OR SPELLING MISTAKES MAY APPEAR !!")
    time.sleep(5)

if __name__ == "__main__":
    booting()

