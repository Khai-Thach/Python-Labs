while True:
    try:
        card = int(input('Card: '))
    except ValueError:
        continue
    if card > 0:
        break

        

    

def luhn_algorithm(card):
    def number_of(i):
        return [int(x) for x in str(i)]
    digits = number_of(card)
    odd = digits[-1::-2]
    even = digits[-2::-2]
    checksum = 0
    checksum += sum(odd)
    for x in even:
        checksum += sum(number_of(x*2))
    return checksum % 10


card_num = 0
visa = card
master = card
amex = card

card_num = len(str(card))


while visa >= 10:
    visa = int(visa/10)


while amex >= 10**13:
    amex = int(amex/10**13)


while master >= 10**14:
    master = int(master/10**14)


if luhn_algorithm(card) == 0:
    if visa == 4 and (card_num == 13 or card_num == 16):
        print('VISA')
    elif card_num == 15 and (amex == 34 or amex == 37):
        print('AMEX')
    elif card_num == 16 and (51 <= master <= 55):
        print('MASTERCARD')
else:
    print('INVALID')

    




