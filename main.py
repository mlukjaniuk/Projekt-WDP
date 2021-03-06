from funkcje import *


while True:
    img1 = climage.convert('start.png', is_unicode=True, width=60)
    img4 = climage.convert('end.jpg', is_unicode=True, width=40)
    liczba_graczy = int(input('Wpisz ilość graczy lub \'0\' aby zakończyć grę: '))
    gracze = []
    l_graczy(liczba_graczy, gracze)
    if liczba_graczy == 0:
        print('Wyszedłeś z gry.')
        break
    if liczba_graczy < 2:
        print('Liczba graczy jest za mała, spróbuj jeszcze raz.')
    elif liczba_graczy > 4:
        print('Liczba graczy jest zbyt duża, spróbuj jeszcze raz.')
    else:
        print(img1)
        playsound('dzwieki/start.mp3')
        print(colored('Witajcie w grze Eksplodujące Kotki!\nLiczba graczy to:', 'red'),
              liczba_graczy, colored('\nKażdy z Was otrzymuje numer od 1 do', 'red'), colored(liczba_graczy, 'red'))
        il_ek = liczba_graczy-1
        il_roz = 6-liczba_graczy
        taliakart = ['nnn', 'nnn', 'nnn', 'atak', 'atak', 'atak', 'atak', 'pom', 'pom', 'pom', 'pom', 'przys',
                     'przys', 'przys', 'przys', 'pot', 'pot', 'pot', 'pot', 'ckp', 'ckp', 'ckp', 'ckp', 'ckp',
                     'pom', 'pom', 'pom', 'pom']

        while il_roz > 0:
            taliakart.append('roz')
            il_roz = il_roz-1

        #spiskart = ['Eksplodujący Kotek', 'Rozbrój', 'Nie, Nie, Nie', 'Pomiń', 'Przysługa', 'Potasuj',
               #     'Co Kryje Przyszłość', 'Atakuj']

        tlumacz_karty()
        rece = []
        random.shuffle(taliakart)
        if liczba_graczy == 2:
            rozdaj_karty_2(taliakart, rece)
        elif liczba_graczy == 3:
            rozdaj_karty_3(taliakart, rece)
        elif liczba_graczy == 4:
            rozdaj_karty_4(taliakart, rece)
        for i in range(0, il_ek):
            taliakart.append('ek')
        random.shuffle(taliakart)

        print(colored('\n\nKażdy z Was otrzyma kartę Rozbrój oraz 4 losowe z talii.', 'red'))
        str = '...\n...\n..'
        for litera in str:
            playsound('dzwieki/tasowanie.mp3')
            sys.stdout.write(litera)
            time.sleep(.1)
        print(colored(litera))
        print(colored('Karty zostały rozdane, zacznijmy grę!', 'red'))
        nr_odp_gracza = 0
        for nr_gry in range(liczba_graczy-1):
            nr_odp_gracza = gra(rece, gracze, liczba_graczy, taliakart, nr_odp_gracza)
            rece.pop(nr_odp_gracza)
            gracze.pop(nr_odp_gracza)
            liczba_graczy -= 1
        print(img4)
        playsound('dzwieki/wygrana.mp3')
        print(colored('\nWygrywa gracz nr', 'red'), colored(gracze[0], 'red'), colored('!!!', 'red'))

        print(colored('\n\nTo już koniec gry, możesz teraz wyjść lub zagrać jeszcze raz :)\n', 'red'))
