#Challenge 5

def calc(s,l,a,y,e,r):
    slayer = s+l+a+y+e+r
    updated_slayer = int(slayer)*3
    layers = l+a+y+e+r+s

    if updated_slayer == int(layers):
        print("Your guess is correct:")
        print(f"SLAYER + SLAYER + SLAYER = {updated_slayer}")
        print(f"LAYERS = {layers}")
        return False
    else:
        print("Your guess is incorrect:")
        print(f"SLAYER + SLAYER + SLAYER = {updated_slayer}")
        print(f"LAYERS = {layers}")
        return True

def iterate():
    while True:
        guess = str(input("Enter your guess for SLAYER: "))
        return_val = calc(guess[0], guess[1], guess[2], guess[3], guess[4], guess[5])
        if return_val == False:
            break

if __name__ == '__main__':
    iterate()