import math

def get_leap_years(start, end):
    rez = []
    for i in range(start, end + 1):
        if i%4 == 0:
            rez.append(i)
    return rez

def test_get_leap_years():
    assert get_leap_years(2000, 2020)==[2000,2004,2008,2012,2016,2020]
    assert get_leap_years(2002,2003)== []
    assert get_leap_years(2000,2009)==[2000,2004,2008]


def get_perfect_squares(start, end):
    rez = []
    for i in range(start, end + 1):
        if i//math.sqrt(i)==math.sqrt(i):
            rez.append(i)
    return rez

def test_get_perfect_squares():
    assert get_perfect_squares(2,10)== [4,9]
    assert get_perfect_squares(5,6)==[]
    assert get_perfect_squares(10,25)==[16,25]


def main():
    test_get_perfect_squares()
    test_get_leap_years()
    while True:
        print ("1. Afișează toți anii bisecți între doi ani dați (inclusiv anii dați).")
        print ("2. Afișează toate pătratele perfecte dintr-un interval închis dat.")
        print("3. Iesire")
        comanda = int (input("Introduceti optiunea:"))
        if comanda == 1:
            start = int(input("Primul an:"))
            end = int(input("Al doilea an:"))
            print("Anii bisecti sunt ", get_leap_years(start, end))
        elif comanda ==2:
            start = int(input("Primul nr:"))
            end = int(input("Al doilea nr:"))
            print("Patratele perfecte sunt ", get_perfect_squares(start, end))
        elif comanda == 3:
            break






main()