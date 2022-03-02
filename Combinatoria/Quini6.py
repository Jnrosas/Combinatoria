# A Python program to print all combinations of given length QUINI 6

from itertools import combinations
import random


def total_comb(comb):
    # Print the obtained combinations
    cont = 0
    for i in list(comb):
        cont = cont + 1
        print(i)
        if cont % 100 == 0:
            print("\nSiguientes", 9366819 - cont)
            input("\nPress ENTER for next 100")
            print()
    print('Fin')



def comb_aleat(comb):
    sec = []
    for i in list(comb):
        sec.append(i)
    choice = random.choice(sec)
    return(choice)



def main():
    print('\t-Menu de Opciones-\n\n'
        '1. Mostrar todas las combinaciones posibles de 100 en 100.\n'
        '2. Mostrar 1 combinacion aleatoria.\n'
        '0. Salir\n')

    opcion = -1
    while opcion != 0:
        comb = combinations(range(46), 6)
        opcion = int(input('\nElija numero de Opcion: '))
        print()
        if opcion == 1:
            print('\nLas combinaciones posibles son...\n')
            # Get all combinations from 0 to 45 and length 6
            total_comb(comb)

        elif opcion == 2:
            choice = comb_aleat(comb)
            print('Su combinacion aleatoria es: :', choice, '\n')

        elif opcion == 0:
            print('\n\t\tFin.\n\tHasta luego.')

        else:
            print('Numero de Opcion Invalido..\n')


if __name__ == '__main__':
    main()

