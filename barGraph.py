import numpy as np
import matplotlib.pyplot as plt
import random


# prepare data
x_data = [f"20{i}" for i in range(16, 21)]
y_data = [random.randint(100, 300) for i in range(6)]


# right chinese and negative symbol
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

#graph plt.bar() is the key
for i in range(len(x_data)):
    plt.bar(x_data[i], y_data[i])

plt.title("TTTTTTTTTT")
plt.xlabel("Year")
plt.ylabel("ttt")

plt.show()
