import math


def get_leap_years(start, end):
    """
    Afișează toți anii bisecți între doi ani dați (inclusiv anii dați).

    :param start: primul an introdus
    :param end: al doilea an introdus
    :return: anii bisecti dintre cei doi ani introdusi, inclusiv anii dati.
    """

    rez = []
    for i in range(start, end + 1):
        if i % 4 == 0:
            rez.append(i)
    return rez


def test_get_leap_years():
    """
    Testeaza daca functia get_leap_years functioneaza
    """
    assert get_leap_years(2000, 2020) == [2000, 2004, 2008, 2012, 2016, 2020]
    assert get_leap_years(2002, 2003) == []
    assert get_leap_years(2000, 2009) == [2000, 2004, 2008]


def get_perfect_squares(start, end):
    """
    Afișează toate pătratele perfecte dintr-un interval închis dat.

    :param start: primul capat al intervalului
    :param end: al doilea capat al inervalului
    :return: patratele perfecte dintre cele doua numere
    """
    rez = []
    for i in range(start, end + 1):
        if i // math.sqrt(i) == math.sqrt(i):
            rez.append(i)
    return rez


def test_get_perfect_squares():
    """
    Testeaza daca funtia get_perfect_squares functioneaza
    """
    assert get_perfect_squares(2, 10) == [4, 9]
    assert get_perfect_squares(5, 6) == []
    assert get_perfect_squares(10, 25) == [16, 25]


def get_n_choose_k(n: int, k: int):
    return math.comb(n, k)


def test_get_n_choose_k():
    """
    Testeaza daca functia get_n_choose_k functioneaza
    :return:
    """
    assert get_n_choose_k(3, 2) == 3
    assert get_n_choose_k(4, 2) == 6
    assert get_n_choose_k(2, 4) == 0


def main():
    test_get_perfect_squares()
    test_get_leap_years()
    test_get_n_choose_k()
    while True:
        print("1. Afișează toți anii bisecți între doi ani dați (inclusiv anii dați).")
        print("2. Afișează toate pătratele perfecte dintr-un interval închis dat.")
        print("3. Calculează combinări de n luate câte k (n și k date).")
        print("4. Iesire")
        comanda = int(input("Introduceti optiunea:"))
        if comanda == 1:
            start = int(input("Primul an:"))
            end = int(input("Al doilea an:"))
            print("Anii bisecti sunt ", get_leap_years(start, end))
        elif comanda == 2:
            start = int(input("Primul nr:"))
            end = int(input("Al doilea nr:"))
            print("Patratele perfecte sunt ", get_perfect_squares(start, end))
        elif comanda == 3:
            n = int(input("Introduceti primul nr: "))
            k = int(input("Introduceti al doilea nr: "))
            print("Valoarea combinarilor este de ", get_n_choose_k(n, k))
        elif comanda == 4:
            break



main()
