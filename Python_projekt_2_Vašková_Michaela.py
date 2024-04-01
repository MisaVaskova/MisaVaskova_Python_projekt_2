"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Michaela Vašková
email: vaskova.mich@seznam.cz
discord: misav19
"""
import random
oddelovac = "-" * 60

print("Hi there!")
print(oddelovac)
print("I've generated a random 4 digit number for you.",
      "\nLet's play a bulls and cows game.")
print(oddelovac)


def generuj_cislo_ke_hre() -> str:
    """
    Vygeneruje náhodné 4-místné číslo. Čislo nesmí začínat nulou. Čísla se ve 4-mistném čísle nesmí opakovat.
    """
    while True:
        cislo = ''.join(random.sample('123456789', 4))
        if cislo[0] != '0':
            return cislo


unikatni_cislo = generuj_cislo_ke_hre()
# print(unikatni_cislo)
# print pro kontrolu hádaného čísla

pokusy = 0


def kontrola_cisla_hrace(hadane_cislo):
    """
    Kontroluje správnost zadaného čísla uživatelem.
    """
    global pokusy
    print(oddelovac)
    pokusy += 1
    if len(hadane_cislo) != 4:
        return False, "Please enter a 4-digit number."
    if not hadane_cislo.isdigit():
        return False, "Please enter only numeric characters."
    if len(set(hadane_cislo)) != 4:
        return False, "The number must not contain duplicate numeric characters."
    if hadane_cislo[0] == '0':
        return False, "Number must not start with zero."
    return True, ""


def hodnot_odhad(hadane_cislo, tip):
    """
    Kontorluje tip uživatele a přičítá bulls a/nebo cows.
    """
    bulls = cows = 0
    for i in range(4):
        if tip[i] == hadane_cislo[i]:
            bulls += 1
        elif tip[i] in hadane_cislo:
            cows += 1
    return bulls, cows


while True:
    tip = input(f"Enter a number:\n{oddelovac}\n>>> ")

    validni, zprava = kontrola_cisla_hrace(tip)
    if not validni:
        print(zprava)
        continue

    bulls, cows = hodnot_odhad(unikatni_cislo, tip)
    if bulls == 4:
        print(f"Correct, you've guessed the right number in {pokusy} {'try' if pokusy == 1 else 'tries'}!")
        break
    else:
        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'}. Try again.")
