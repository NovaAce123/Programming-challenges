#Wind Chill

def TempCalc(air_temp, air_speed):
    return 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16

def final():
    print("---Wind Chill Temperature Index---")
    print(f"Temperature of 10 and speed of 15 gives windchill of: {TempCalc(10,15)}")
    print(f"Temperature of 0 and speed of 25 gives windchill of: {TempCalc(0,25)}")
    print(f"Temperature of -10 and speed of 35 gives windchill of: {TempCalc(-10,35)}")

    user_temp = float(input("Enter Temperature: "))
    user_speed = float(input("Enter Speed: "))

    user_windchill = TempCalc(user_temp, user_speed)
    print(f"Temperature of {user_temp} and speed of {user_speed} gives windchill of: {user_windchill}")

if __name__ == '__main__':
    final()