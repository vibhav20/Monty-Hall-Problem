import random


def reveal(prize, choice, doors):
    i = 1
    while (i == prize or i == choice) and i <= len(doors):
        i = i + 1

    return i


def switch_door(door_shown, doors, choice):
    r = 1
    while (r == door_shown or r == choice) and r <= len(doors):
        r = r + 1
    return r


def game(switch, ntest):
    nwin_sw = 0
    nwin_nosw = 0
    nl_nosw = 0
    nl_sw = 0
    doors = [1, 2, 3]
    ndoors = len(doors)

    for i in range(0, ntest):
        choice = random.randint(1, ndoors)
        prize = random.randint(1, ndoors)
        door_revealed = reveal(prize, choice, doors)
        if switch == True:
            new_choice = switch_door(door_revealed, doors, choice)

        if choice == prize:
            nwin_nosw += 1

        if new_choice == prize:
            nwin_sw += 1

        if choice != prize:
            nl_nosw += 1

        if new_choice != prize:
            nl_sw += 1

    return nwin_nosw, nwin_sw, nl_nosw, nl_sw, ntest
