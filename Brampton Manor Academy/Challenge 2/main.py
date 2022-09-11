# PROJECT 2

def table():
    print("""
    Ritcher     Joules                  TNT
    1           1995262.3149688789      0.00047697913837688307
    5           1995262314968.8828      476.87913837688404
    9.1         2.818382931264449e+18   673609687.2046962
    9.2         3.981071705534953e+18   951498973.5982201
    9.5         1.1220184543019653E+19  2681688466.3048882""")

    value = float(input("Please enter a Richter scale value: "))
    print(f"Richter value: {value}")
    joules = 10**((1.5*value)+4.8)
    print(f"Equivalence in joules: {joules}")

    tnt(joules)



def joules():
    value = float(input("Please enter a Richter scale value: "))
    print(f"Richter value: {value}")
    joules = 10**((1.5*value)+4.8)
    print(f"Equivalence in joules: {joules}")

    tnt(joules)

def tnt(energy):
    tons = energy / 4.184*(10**9)
    print(f"Equivalence in tons of TNT: {tons}")

table()
