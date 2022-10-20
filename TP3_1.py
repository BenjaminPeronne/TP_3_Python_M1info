# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-20 10:17:23
#  * @modify date 2022-10-20 10:17:23
#  * @desc [TP3 - Exercice 1]
#  */

# Ojectif : Réorganisation de texte


def main():
    chaine = "Un texte que je veux retravailler"
    chaine = chaine.replace("je veux", "Joe veut")
    mots = chaine.split()
    print("+++".join(mots))


if __name__ == "__main__":
    main()
