# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-20 11:52:29
#  * @modify date 2022-10-20 11:52:29
#  * @desc [TP3 - Exercice 5]
#  */

# Objectif : altitudes maximales de Syracuse


from TP3_4 import vol  # Importation de la fonction vol() du fichier TP3_4.py


def altMaxi(p_uinit):  # Altitude maximale de Syracuse
    liste = vol(p_uinit)
    return max(liste)


def main():
    uinit = int(input("Entrez un entier initial strictement positif : "))
    if (uinit <= 0):
        print("=> Erreur : uinit doit être strictement positif")
        while (uinit <= 0):
            uinit = int(input(">>> Entrez un entier initial strictement positif : "))
    else:
        print("\n", vol(uinit))
        print("\nLa suite de Syracuse de", uinit, "a une altitude maximale de", altMaxi(uinit))


if __name__ == "__main__":
    main()
