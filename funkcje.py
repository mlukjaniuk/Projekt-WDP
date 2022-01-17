import random, sys, time, climage
from termcolor import colored

def tlumacz_karty():
    while True:
        print('\nW talii znajdują się następujące karty: \'Eksplodujący Kotek\', \'Rozbrój\', \'Atakuj\', '
              '\'Nie, Nie, Nie\', \'Pomiń\', \'Przysługa\', \'Potasuj\', \'Co Kryje Przyszłość\'')
        name = str(input('Jeżeli potrzebujesz wyjaśnienia, co robi dana karta, wpisz teraz jej nazwę'
                         ' (wielkość liter ma znaczenie), w przeciwnym przypadku wpisz \'X\': '))
        if name == 'X':
            break

        if name == 'Eksplodujący Kotek':
            print(colored('\n\t\tO ile nie masz karty rozbrojenia, umierasz. Jeżeli rozbroisz tę kartę, wraca ona do '
                  'potasowanej talii.', 'cyan'))

        elif name == 'Rozbrój':
            print(colored('\n\t\tPo wylosowaniu Eksplodującego Kotka zagraj tę kartę, aby nie umrzeć.'
                  ' Zostanie ona wtedy odrzucona, a Twoja tura zakończona.', 'cyan'))

        elif name == 'Nie, Nie, Nie':
            print(colored('\n\t\tAnuluj działanie karty Przysługi lub Ataku.', 'cyan'))

        elif name == 'Pomiń':
            print(colored('\n\t\tNatychmiast zakończ swoją turę bez dobierania karty (zagrana w odpowiedzi na kartę'
                  ' Ataku kończy tylko 1 z 2 tur).', 'cyan'))

        elif name == 'Przysługa':
            print(colored('\n\t\tZmuś następnego gracza do oddania Ci ostatniej dobranej przez siebie karty z ręki.', 'cyan'))

        elif name == 'Potasuj':
            print(colored('\n\t\tPotasuj talię pozostałych kart.', 'cyan'))

        elif name == 'Co Kryje Przyszłość':
            print(colored('\n\t\tPodejrzyj 3 wierzchnie karty talii bez zmiany ich kolejności.', 'cyan'))

        elif name == 'Atakuj':
            print(colored('\n\t\tNatychmiast zakończ swoją turę, nie dobierając karty. Kolejny gracz musi dobrać '
                  'kartę w ramach Twojej tury. Gra toczy się dalej, począwszy od zaatakowanego gracza.', 'cyan'))
        else:
            print(colored('\n\t\tPodałeś błędną nazwę, spróbuj jeszcze raz.', 'cyan'))


def rozdaj_karty_2(taliakart, rece):
        reka1 = ['roz']
        x1 = 4
        while x1 > 0:
            reka1.append(taliakart.pop(0))
            x1 = x1 - 1
        rece.append(reka1)
        reka2 = ['roz']
        x2 = 4
        while x2 > 0:
            reka2.append(taliakart.pop(0))
            x2 = x2 - 1
        rece.append(reka2)


def rozdaj_karty_3(taliakart, rece):
    reka1 = ['roz']
    x1 = 4
    while x1 > 0:
        reka1.append(taliakart.pop(0))
        x1 = x1 - 1
    rece.append(reka1)
    reka2 = ['roz']
    x2 = 4
    while x2 > 0:
        reka2.append(taliakart.pop(0))
        x2 = x2 - 1
    rece.append(reka2)
    reka3 = ['roz']
    x3 = 4
    while x3 > 0:
        reka3.append(taliakart.pop(0))
        x3 = x3 - 1
    rece.append(reka3)


def rozdaj_karty_4(taliakart, rece):
    reka1 = ['roz']
    x1 = 4
    while x1 > 0:
        reka1.append(taliakart.pop(0))
        x1 = x1 - 1
    rece.append(reka1)
    reka2 = ['roz']
    x2 = 4
    while x2 > 0:
        reka2.append(taliakart.pop(0))
        x2 = x2 - 1
    rece.append(reka2)
    reka3 = ['roz']
    x3 = 4
    while x3 > 0:
        reka3.append(taliakart.pop(0))
        x3 = x3 - 1
    rece.append(reka3)
    reka4 = ['roz']
    x4 = 4
    while x4 > 0:
        reka4.append(taliakart.pop(0))
        x4 = x4 - 1
    rece.append(reka4)


def l_graczy(liczba_graczy, gracze):
    if liczba_graczy == 2:
        gracze.append(1)
        gracze.append(2)
    elif liczba_graczy == 3:
        gracze.append(1)
        gracze.append(2)
        gracze.append(3)
    else:
        gracze.append(1)
        gracze.append(2)
        gracze.append(3)
        gracze.append(4)


def dobierzkarte(taliakart, rece, nr_talii):
    dobranakarta = taliakart[0]
    if dobranakarta == 'ek':
        print(colored('Dobrana karta to Eksplodujący Kotek', 'magenta'))
        kotek_eksplodowal = eksplodujacykotek(nr_talii, rece, taliakart)
        if kotek_eksplodowal:
            return True
        else:
            return False
    elif dobranakarta == 'roz':
        print(colored('Dobrana karta to Rozbrój', 'magenta'))
        rece[nr_talii].append(taliakart.pop(0))
    elif dobranakarta == 'nnn':
        print(colored('Dobrana karta to Nie, Nie, Nie', 'magenta'))
        rece[nr_talii].append(taliakart.pop(0))
    elif dobranakarta == 'pom':
        print(colored('Dobrana karta to Pomiń', 'magenta'))
        rece[nr_talii].append(taliakart.pop(0))
    elif dobranakarta == 'przys':
        print(colored('Dobrana karta to Przysługa', 'magenta'))
        rece[nr_talii].append(taliakart.pop(0))
    elif dobranakarta == 'pot':
        print(colored('Dobrana karta to Potasuj', 'magenta'))
        rece[nr_talii].append(taliakart.pop(0))
    elif dobranakarta == 'ckp':
        print(colored('Dobrana karta to Co Kryje Przyszłość', 'magenta'))
        rece[nr_talii].append(taliakart.pop(0))
    else:
        print(colored('Dobrana karta to Atakuj', 'magenta'))
        rece[nr_talii].append(taliakart.pop(0))
    return False


def reka_karty(tura, liczba_graczy, rece):
    for karta in rece[tura % liczba_graczy]:
        if karta == 'roz':
            print('Rozbrój')
        elif karta == 'nnn':
            print('Nie, Nie, Nie')
        elif karta == 'pom':
            print('Pomiń')
        elif karta == 'przys':
            print('Przysługa')
        elif karta == 'pot':
            print('Potasuj')
        elif karta == 'ckp':
            print('Co Kryje Przyszłość')
        else:
            print('Atakuj')


def pelna_nazwa(skrot):
    if skrot == 'roz':
        print('Rozbrój')
    elif skrot == 'nnn':
        print('Nie, Nie, Nie')
    elif skrot == 'pom':
        print('Pomiń')
    elif skrot == 'przys':
        print('Przysługa')
    elif skrot == 'pot':
        print('Potasuj')
    elif skrot == 'ckp':
        print('Co Kryje Przyszłość')
    else:
        print('Atakuj')


def cokryjeprzyszlosc(taliakart):
    print('3 wierzchnie karty to: ')
    for i in range(0, 3):
        if taliakart[i] == 'ek':
            print('Eksplodujący Kotek')
        elif taliakart[i] == 'roz':
            print('Rozbrój')
        elif taliakart[i] == 'nnn':
            print('Nie, Nie, Nie')
        elif taliakart[i] == 'pom':
            print('Pomiń')
        elif taliakart[i] == 'przys':
            print('Przysługa')
        elif taliakart[i] == 'pot':
            print('Potasuj')
        elif taliakart[i] == 'ckp':
            print('Co Kryje Przyszłość')
        else:
            print('Atakuj')


def eksplodujacykotek(nr_talii, rece, taliakart):
    if 'roz' in rece[nr_talii]:
        img2 = climage.convert('playing-kitten.png', is_unicode=True, width=40)
        print(img2)
        print(colored("Udało Ci się rozbroić Eksplodującego Kotka! Pozostajesz w grze, a karta wraca do talii.", 'red'))
        random.shuffle(taliakart)
        str = '...\n...\n...\n'
        for litera in str:
            sys.stdout.write(litera)
            time.sleep(.3)
        print("Talia została potasowana.")
        rece[nr_talii].remove('roz')
        return False
    else:
        img3 = climage.convert('exploding-kitten.png', is_unicode=True, width=40)
        print(img3)
        print(colored("Niestety Kotek eksplodował, więc odpadasz z gry.\n\n\n", 'red'))
        taliakart.remove('ek')
        return True


def gra(rece, gracze, liczba_graczy, taliakart, rozpoczynajacy_gracz):
    tura = rozpoczynajacy_gracz
    while True:
        print(colored('\n\n\n\n\n\n\n\n\n\nTura gracza nr ', 'yellow'),
              colored(gracze[tura % liczba_graczy], 'yellow'))
        while True:
            print(colored('Twoje karty to:', 'yellow'))
            reka_karty(tura, liczba_graczy, rece)
            print(colored('Jeżeli chcesz zagrać jakąś kartę, wpisz tutaj jej nazwę lub napisz '
                  '\'Dobierz\', aby dobrać kartę. ', 'yellow'))
            zagrana_karta = input()
            if zagrana_karta == 'Dobierz':
                kotek_eksplodowal = dobierzkarte(taliakart, rece, tura % liczba_graczy)
                if kotek_eksplodowal:
                    return tura % liczba_graczy
                break
            elif zagrana_karta == 'Potasuj' and 'pot' in rece[tura % liczba_graczy]:
                random.shuffle(taliakart)
                str = '...\n...\n...\n'
                for litera in str:
                    sys.stdout.write(litera)
                    time.sleep(.3)
                print('Talia została potasowana.')
                rece[tura % liczba_graczy].remove('pot')
            elif zagrana_karta == 'Co Kryje Przyszłość' and 'ckp' in rece[tura % liczba_graczy]:
                cokryjeprzyszlosc(taliakart)
                rece[tura % liczba_graczy].remove('ckp')
            elif zagrana_karta == 'Przysługa' and 'przys' in rece[tura % liczba_graczy]:
                if 'nnn' in rece[(tura + 1) % liczba_graczy]:
                    rece[(tura + 1) % liczba_graczy].remove('nnn')
                    print(colored('Następny gracz anulował działanie Twojej Przysługi kartą \'Nie, Nie, Nie\'.', 'red'))
                else:
                    if not rece[(tura + 1) % liczba_graczy]:
                        continue
                    else:
                        rece[tura % liczba_graczy].append(rece[(tura + 1) % liczba_graczy].pop())
                        rece[tura % liczba_graczy].remove('przys')
                        print('Dobrana karta to: ')
                        pelna_nazwa(rece[tura % liczba_graczy][-1])
            elif zagrana_karta == 'Atakuj' and 'atak' in rece[tura % liczba_graczy]:
                if 'nnn' in rece[(tura + 1) % liczba_graczy]:
                    rece[(tura + 1) % liczba_graczy].remove('nnn')
                    print(colored('Następny gracz anulował działanie Twojej Przysługi kartą \'Nie, Nie, Nie\'.', 'red'))
                    rece[tura % liczba_graczy].remove('atak')

                else:
                    kotek_eksplodowal = dobierzkarte(taliakart, rece, (tura + 1) % liczba_graczy)
                    if kotek_eksplodowal:
                        return tura + 1 % liczba_graczy
                    rece[tura % liczba_graczy].remove('atak')
                    break

            elif zagrana_karta == 'Pomiń' and 'pom' in rece[tura % liczba_graczy]:
                rece[tura % liczba_graczy].remove('pom')
                break

            else:
                print('Wprowadziłeś niepoprawną nazwę karty lub takiej nie posiadasz, spróbuj jeszcze raz.')

        tura += 1
