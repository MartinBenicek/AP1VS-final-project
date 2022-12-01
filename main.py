reminders = []

number = int(input("Zadejte číslo které chcete převést: "))
system = int(input("Zadejte do ktéré soustavy chcete číslo převést (2, 8, 16): "))

if number == 0:
    print(0)

def binOcta(number, system):
    while number > 0:
        reminders.append(number % system)
        number = number // system
    reminders.reverse()
    for i in reminders:
        print(i, end="")


def sixteenth(number, system):
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
