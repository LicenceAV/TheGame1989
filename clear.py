import os
import platform

def clear():
    """
    permet d'effacer la console du joueur

    Returns
    -------
    None.

    """
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')