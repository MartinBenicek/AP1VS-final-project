"""
Program pro převod číselných soustav.

@Authors Autors: Martin Beníček, Václav Tomeček
@version 1.2
"""


reminders = []

number = int(input("Zadejte číslo které chcete převést: "))
system = int(input("Zadejte číselnou soustavu (2, 8, 16): "))

if number == 0:
    print(0)


def binOcta(number, system):
    """
    Funkce pro převod do dvojkové a osmičkové soustavy.

    Dokud je 5 větší než 0 vydělí dvojkou a zbytek přidá do reminders.
    5 se vydělí 2 a beze zbytku se přepíše na vydělené číslo.
    Až je vydělené číslo == 0 cyklus končí.
    Reminders seřadí čísla od posledného k prvnímu.

    Pro osmičkovou soutavu platí stejný postup.

    Příklad použití:
    >>> binOcta(5, 2)
    101
    """
    while number > 0:
        reminders.append(number % system)
        number = number // system
    reminders.reverse()
    for i in reminders:
        print(i, end="")


def sixteenth(number, system):
    """
    Funkce pro převod do šestnáctkové soustavy.

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


if system == 2 or system == 8:
    binOcta(number, system)
elif system == 16:
    sixteenth(number, system)
