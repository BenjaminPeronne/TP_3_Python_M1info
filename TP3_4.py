# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-20 11:08:17
#  * @modify date 2022-10-20 11:08:17
#  * @desc [TP3 - Exercice 4]
#  */

# Objectif : Suite de Syracuse

def etapeSuivante(p_u): # Etape suivante de Syracuse
    if p_u % 2 == 0:
        return p_u // 2 # Si u est pair
    else:
        return 3 * p_u + 1 # Si u est impair


def vol(p_uinit): # Vol de Syracuse
    liste = []
    u = p_uinit

    while u != 1:
        liste.append(u)
        u = etapeSuivante(u)

    liste.append(u)
    return liste


def main():
    uinit = int(input("Entrez un entier initial strictement positif : "))
    if (uinit <= 0):
        print("=> Erreur : uinit doit être strictement positif")
        while (uinit <= 0):
            uinit = int(input(">>> Entrez un entier initial strictement positif : "))
    else:
        print(vol(uinit))


if __name__ == "__main__":
    main()
