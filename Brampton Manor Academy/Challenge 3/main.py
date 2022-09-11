# PROJECT 3

def player_one():
    x = False
    while x == False:
        answer = int(input("Select a number between 10 and 49: "))
        if (answer > 49) or (answer < 10):
            print("Out of range")
        else:
            x = True

    factor = 99 - answer
    return factor
    
def player_two(factor):
    x = False
    while x == False:
        num = int(input("Select a number between 50 and 99: "))
        if (num > 99) or (num < 50):
            print("Out of range")
        else:
            x = True

    ans = factor + num
    ans = ans - 100
    ans = ans + 1
    ans = num - ans
    print(ans)

player_two(player_one())