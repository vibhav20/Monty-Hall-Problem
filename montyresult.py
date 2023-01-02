from montyhall import game

result = game(True, 100)
print("Win switch %: ", result[1] / result[4])
print("Lose switch %: ", result[3] / result[4])
print("Win No switch %: ", result[0] / result[4])
print("Lose No switch %: ", result[2] / result[4])
