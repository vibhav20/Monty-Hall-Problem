from montyhall import game
import numpy
import matplotlib.pyplot as plt

tests = []
win_percentage = []
for i in range(1, 501):
    tests.append(i)
    y = game(True, i)
    win_percentage.append(y[1] / y[4])

plt.figure(figsize=(12, 6))
plt.plot(tests, win_percentage)
plt.title("Monty Hall Problem")
plt.xlabel("Number of Tests", fontsize=12)
plt.ylabel("Win Percentage", fontsize=12)
plt.show()
