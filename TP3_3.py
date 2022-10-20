# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-20 10:59:01
#  * @modify date 2022-10-20 10:59:01
#  * @desc [TP3 - Exercice 3]
#  */


# Ojectif : Calculer pi

import math


def monPi(p_n):
    ''' Sachant que l'ensemble de 1 / ** 2 = pi ** 2 / 6 '''
    somme = 0
    for i in range(1, p_n + 1):
        somme += 1 / i ** 2
    return math.sqrt(6 * somme)


def main():
    n = int(input("Entrez un entier n positif non nul : "))
    if (n <= 0):
        print("=> Erreur : n doit être positif non nul")
        while (n <= 0):
            n = int(input(">>> Entrez un entier n positif non nul : "))
    else:
        pi = monPi(n)
        print("Pi = ", pi)
        print("Erreur relative = ", abs(pi - math.pi) / math.pi * 100, "%")


if __name__ == "__main__":
    main()
