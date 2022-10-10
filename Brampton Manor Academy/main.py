# Challenge 12 Card Checksum

def length(card):
    x = 0
    while x == 0:
        if len(str(card)) == 16:
            print("Valid card length")
            return 1
            x = 1
        elif len(str(card)) > 16:
            print("Too long")
            return 0
        else:
            print("Too short")
            return 0


def letter_check(card):
    boolean = False
    while boolean == False:
        if str(card).isnumeric() == True:
            print("Valid characters")
            return 1
        else:
            print("Card number must be just numbers")
            return 0

def l_check(card):
    card = str(card)
    card = unicode(card, 'utf-8')
    check = 1
    x = card.isnumeric()
    if x == check:
        print("Valid")
    else:
        print("Incorrect")


if __name__ == "__main__":
    card = input("Enter Card Number: ")
    #length(card)
    #letter_check(card)
    l_check(card)
