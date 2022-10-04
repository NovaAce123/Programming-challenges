# Challenge 12 Card Checksum

def length(card):
    x = 0
    while x == 0:
        if len(card) == 16:
            print("Valid card length")
            return 1
            x = 1
        elif len(card) > 16:
            print("Too long")
            return 0
        else:
            print("Too short")
            return 0


def letter_check(card):
    print(card.isalpha())
    if (card).isalpha() == False:
        print("Valid characters")
        return 1
    else:
        print("Card number must be just numbers")
        return 0

if __name__ == "__main__":
    card = str(input("Enter Card Number: "))
    length(card)
    letter_check(card)