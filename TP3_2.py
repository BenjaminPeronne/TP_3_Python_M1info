# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-20 10:53:35
#  * @modify date 2022-10-20 10:53:35
#  * @desc [TP3 - Exercice 2]
#  */

# Ojectif : Faire correspondre les jours de la semaine à des nombres


def main():
    semnum = {1: "lundi", 2: "mardi", 3: "mercredi", 4: "jeudi", 5: "vendredi", 6: "samedi", 7: "dimanche"}
    semjours = {}

    for key, value in semnum.items():
        semjours[value] = key

    jours = list(semjours.keys())
    jours.sort()

    for jour in jours:
        print(jour, semjours[jour])


if __name__ == "__main__":
    main()
