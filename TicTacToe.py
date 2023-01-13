tableau = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}


def afftableau(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def game():
    Joueur = 'X'
    tour = 0

    for i in range(10):
        afftableau(tableau)
        print("A ton tour, chosis une case")

        choixcase = input()

        if tableau[choixcase] == ' ':
            tableau[choixcase] = Joueur
            tour += 1
        else:
            print("Cette case est déjà remplie.\nChoisis une autre case")
            continue

        if tour >= 5:
            if tableau['7'] == tableau['8'] == tableau['9'] != ' ':  # premiere ligne
                afftableau(tableau)
                print("\nGame Over.\n")
                print(" Joueur " + Joueur + " a gagné !.")
                break
            elif tableau['4'] == tableau['5'] == tableau['6'] != ' ':  # deuxieme ligne
                afftableau(tableau)
                print("\nGame Over.\n")
                print(" Joueur " + Joueur + " a gagné !.")
                break
            elif tableau['1'] == tableau['2'] == tableau['3'] != ' ':  # derniere ligne
                afftableau(tableau)
                print("\nGame Over.\n")
                print("Joueur" + Joueur + " a gagné !.")
                break
            elif tableau['1'] == tableau['4'] == tableau['7'] != ' ':  # premiere colonne
                afftableau(tableau)
                print("\nGame Over.\n")
                print("Joueur" + Joueur + " a gagné !.")
                break
            elif tableau['2'] == tableau['5'] == tableau['8'] != ' ':  # deuxieme colonne
                afftableau(tableau)
                print("\nGame Over.\n")
                print("Joueur" + Joueur + " a gagné !.")
                break
            elif tableau['3'] == tableau['6'] == tableau['9'] != ' ':  # derniere colonne
                afftableau(tableau)
                print("\nGame Over.\n")
                print("Joueur" + Joueur + " a gagné !.")
                break
            elif tableau['7'] == tableau['5'] == tableau['3'] != ' ':  # diagonal1
                afftableau(tableau)
                print("\nGame Over.\n")
                print("Joueur" + Joueur + " a gagné !.")
                break
            elif tableau['1'] == tableau['5'] == tableau['9'] != ' ':  # diagonal2
                afftableau(tableau)
                print("\nGame Over.\n")
                print("Joueur" + Joueur + " a gagné !.")
                break

                # S'il n'y a pas de victoire on affiche "Game over, ex aequo"
        if tour == 9:
            print("\nGame Over.\n")
            print("Ex aequo")

            # Changer de joueur à chaque tours
        if Joueur == 'X':
            Joueur = 'O'
        else:
            Joueur = 'X'


game()
