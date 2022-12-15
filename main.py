"""
Program pro převod číselných soustav.

@Authors Autors: Martin Beníček, Václav Tomeček
@version 1.2
"""

import time

reminders = []

try:
    number = int(input("Zadejte číslo které chcete převést: "))
    system = int(input("Zadejte číselnou soustavu (2, 8, 16): "))

    if number == 0:
        print(0)

# Slouží v případě generace pdoc dokumentu.
except EOFError as e:
    number = 5
    system = 2
    print(e)


def binOcta(number, system):
    """
    Funkce pro převod do dvojkové a osmičkové soustavy.

    Dokud je number větší než 0, vydělí system a zbytek přidá do reminders.
    number se vydělí system a beze zbytku se přepíše na vydělené číslo.
    Až je vydělené číslo == 0 cyklus končí.
    Reminders seřadí čísla od posledného k prvnímu a vypíše je.

    Příklad použití:
    >>> binOcta(5, 2)
    101

    >>> binOcta(14, 8)
    5
    """
    while number > 0:
        reminders.append(number % system)
        number = number // system
    reminders.reverse()
    for i in reminders:
        print(i, end="")
    # časové spoždění 5 sekund aby si uživatel mohl přečíst výsledek na konzoli
    time.sleep(5)
    return reminders


def sixteenth(number, system):
    """
    Funkce pro převod do šestnáctkové soustavy.

    Dokud je number větší než 0 vydělí system a zbytek přidá do reminders.
    Pokud je zbytek >=10 tak se přepisuje na příslušná písmena
    number se vydělí system a beze zbytku se přepíše na vydělené číslo.
    Až je vydělené číslo == 0 cyklus končí.
    Reminders seřadí čísla od posledného k prvnímu a vypíše je.
    """
    hexadecimal = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
    while number > 0:
        result = number % system
        if result >= 10:
            reminders.append(hexadecimal[result])
        else:
            reminders.append(result)
        number = number // system
    reminders.reverse()
    for i in reminders:
        print(i, end="")
    # časové spoždění 5 sekund aby si uživatel mohl přečíst výsledek na konzoli
    time.sleep(5)
    return reminders


if system == 2 or system == 8:
    binOcta(number, system)
elif system == 16:
    sixteenth(number, system)
