
matrice = [['.','.','.'],['.','.','.'],['.','.','.'],]
lung=len(matrice)
p1='X'
p2='0'

def afiseaza(a):
    print('Tabel curent:')
    for i in range(lung):
        for j in range(lung):
            print(matrice[i][j], end='')
        print()


def citeste_mutare(tabla, jucator):
    while True:
        try:
            print(f"Este randul jucatorului: {jucator}")
            lin = int(input('Selecteaza linia (1-3): ')) - 1
            col = int(input('Selecteaza coloana (1-3): ')) - 1

            if 0 <= lin <= 2 and 0 <= col <= 2:
                if tabla[lin][col] == '.':
                    return lin, col
                else:
                    print(f"Pozitia este ocupata de {tabla[lin][col]}. Alege alta.")
            else:
                print("Coordonate invalide! Alege numere intre 1 si 3.")

        except ValueError:
            print("Te rog introdu un numar valid!")

def stare_joc(tabla):
    lung = len(tabla)

    for i in range(lung):
        if tabla[i][0] == tabla[i][1] == tabla[i][2] and tabla[i][0] != '.':
            return tabla[i][0]

    for i in range(lung):
        if tabla[0][i] == tabla[1][i] == tabla[2][i] and tabla[0][i] != '.':
            return tabla[0][i]

    if tabla[0][0] == tabla[1][1] == tabla[2][2] and tabla[0][0] != '.':
        return tabla[0][0]

    if tabla[0][2] == tabla[1][1] == tabla[2][0] and tabla[0][2] != '.':
        return tabla[0][2]

    flag = True
    for i in range(lung):
        for j in range(lung):
            if matrice[i][j] == '.':
                flag = False
                break
    if flag:
        return 'EGAL'
    else:
        return 'CONTINUA'

print('Jucator 1 are semnul X. Jucator 2 are semnul 0.')
jucator_curent = p1
joc_activ = True

while joc_activ:
    afiseaza(matrice)

    linie, coloana = citeste_mutare(matrice, jucator_curent)

    matrice[linie][coloana] = jucator_curent

    rezultat = stare_joc(matrice)

    if rezultat != 'CONTINUA':
        afiseaza(matrice)
        if rezultat == 'EGAL':
            print("Jocul s-a terminat la EGALITATE!")
        else:
            print(f"FELICITARI! Jucatorul {rezultat} a castigat!")
        joc_activ = False
    else:
        if jucator_curent == p1:
            jucator_curent = p2
        else:
            jucator_curent = p1

