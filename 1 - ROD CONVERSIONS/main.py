# PROJECT 1

rods=float(input("Input rods: "))

def convertmetres(rod):
    metres = rod * 5.0292
    return metres

def convertfurlong(rod):
    furlongs = rod/40
    return furlongs

def convertfeet(metres):
    feet = metres/0.3048
    return feet

def convertmiles(metres):
    miles = metres/1609.34
    return miles

def converttime(miles):
    time = (miles/(3.1/60))
    return time

def conversion(rods):
    print("Conversions: ")

    metres = convertmetres(rods)
    print("Meters:" + str(metres))

    furlongs = convertfurlong(rods)
    print("Furlongs:" + str(furlongs))

    feet = convertfeet(metres)
    print("Feet:" + str(feet))

    miles = convertmiles(metres)
    print("Miles:" + str(miles))

    time = converttime(miles)
    print("Minutes to walk " + str(rods) + " rods: " + str(time))


if __name__ == "__main__":
    conversion(rods)