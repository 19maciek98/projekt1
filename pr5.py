odp1 = False

while True:

    


    if odp1 == False:
        print('Witaj\nJakie zadanie chcesz rozwiązać?\n')
        print('-spadek swobodny [wpisz: "spadek"]\n-ruch postępowy [wpisz: "ruch"]\n-równia pochyła [wpisz: "rownia"]\n-rzut [wpisz: "rzut"]')
        odp1 = input()

    print('\n')
    if odp1 == 'spadek':
        spadek_swobodny()
    elif odp1 == 'ruch':
        ruch_postepowy()
    elif odp1 == 'rownia':
        rownia_pochyla()
    elif odp1 == 'rzut':
        rzut_ukosny()
    else:
        print('Nieprawidłowe polecenie')
        

    print('Czy chcesz liczyć ponownie?\ntak-"t"\ninne zadanie-"inne"')
    odp2 = input()


    if odp2 == 'inne':
        odp1 = False
    elif odp2 != 't':
        print('Zamykanie programu')
        break
