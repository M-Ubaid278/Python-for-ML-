import matplotlib.pyplot as plt

input=[1,2,3,4,5]
squares=[1,4,9,16,25]

plt.style.use('seaborn-v0_8')

ax = plt.subplot()
ax.plot(input,squares, linewidth=5)

ax.set_title("Square Numbers", fontsize=14)
ax.tick_params(labelsize=14)

ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("Square of value", fontsize=14)
plt.show()