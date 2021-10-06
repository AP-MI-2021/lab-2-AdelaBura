def get_perfect_squares(start: int, end: int):
    '''
    Afiseaza o lista cu toate patratele perfecte dintr-un interval inchis
    :param start: n nr intreg
    :param end: n nr intreg
    :return: lista de intregi cu toate patratele perfecte cuprinse in interval
    '''
    lista = []
    if start > end:
        aux = start
        start = end
        end = aux
    i = 1
    while i * i <= end:
        if i * i >= start:
            lista.append(i * i)
        i += 1
    return lista

def test_get_perfect_squares():
    assert get_perfect_squares(3, 47) == [4, 9, 16, 25, 36]
    assert get_perfect_squares(63, 100) == [64, 81, 100]
    assert get_perfect_squares(55, 57) == []

def get_leap_years(start: int, end: int):
    '''
    Afiseaza o lista cu anii bisecti intre doi ani dati, inclusiv anii dati
    :param start: n nr natural
    :param end: n nr natural
    :return: lista cu toate nr din intervalul [start, end]
    '''
    lista = []
    if start > end:
        aux = start
        start = end
        end = aux
    for an in range(start, end + 1):
        if an % 4 == 0 and an % 100 != 0:
            lista.append(an)
            if an % 400 == 0:
                lista.append(an)
    return lista

def test_get_leap_years():
    assert get_leap_years(1582, 1600) == [1584, 1588, 1592, 1596, 1600]
    assert get_leap_years(2001, 2020) == [2004, 2008, 2012, 2014, 2016, 2020]
    assert get_leap_years(2101, 2117) == [2104, 2108, 2112, 2116]

def main():
    test_get_perfect_squares()
    print ('''
    1. Afiseaza toate patratele perfecte dintr-un interval inchis
    2. Afiseaza anii bisecti intre doi ani dati, inclusiv anii dati
    x. Iesire
    ''')
    cmd = input("Comanda:")
    while cmd != 'x':
            if cmd == '1':
                interval = input('Introduceti marginile intervalului separate prin spatiu:').split(' ')
                lim_inf = int(interval[0])
                lim_sup = int(interval[1])
                lista_pp = get_perfect_squares(lim_inf, lim_sup)
                lista_pp_string = ''
                if len(lista_pp) > 0:
                    print(f'Patratele perfecte cuprinse intre {lim_inf} si {lim_sup} sunt:')
                    for pp in lista_pp:
                        lista_pp_string += str(pp) + ' '
                    print(lista_pp_string)
                else:
                    print (f'Nu exista patrate perfecte in intervalul [{lim_inf} ,{lim_sup}]')
            elif cmd == '2':
                ani = input('Introduceti anii separati prin spatiu:').split(' ')
                an_inceput = int(ani[0])
                an_final = int(ani[1])
                lista_ani = get_leap_years(an_inceput, an_final)
                lista_ani_string = ''
                if len(lista_ani) > 0:
                    print(f'Anii bisecti cuprinsi intre anii {an_inceput} si {an_final} sunt: ')
                    for an in lista_ani:
                        lista_ani_string += str(an) + ' '
                    print(lista_ani_string)
                else:
                    print(f'Nu exista ani bisecti intre anii {an_inceput} si {an_final}')
            cmd = input('Selectati o alta comanda:')

if __name__ == '__main__':
    main()
