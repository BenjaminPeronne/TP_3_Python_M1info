# /**
#  * @author Benjamin Peronne
#  * @email contact@benjaminperonne.fr
#  * @create date 2022-10-20 13:33:42
#  * @modify date 2022-10-20 13:33:42
#  * @desc [TP3 - Exercice 6]
#  */

# Objectif : La suite de Fibonacci de manière récursive

def fibonacci(p_n):
    if (p_n == 0):
        return 0
    elif (p_n == 1):
        return 1
    else:
        return fibonacci(p_n - 1) + fibonacci(p_n - 2)


def main():
    n = int(input("Entrez un entier n positif non nul : "))
    for i in range(n + 1):
        print(fibonacci(i))


if __name__ == "__main__":
    main()
