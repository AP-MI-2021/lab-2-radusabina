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



def main():
    test_get_leap_years()
    start = int(input("Primul an:"))
    end = int(input("Al doilea an:"))
    print( "Anii bisecti sunt " ,get_leap_years(start, end))


main()