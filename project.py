import matplotlib.pyplot as plt

# input=[1,2,3,4,5]
# squares=[1,4,9,16,25]

# plt.style.use('seaborn-v0_8')

# ax = plt.subplot()

# ax.scatter(input,squares,s=200, color="orange")   #highlight the specific point in the graph by passing x and y points 
# ax.plot(input,squares, linewidth=5)

# ax.set_title("Square Numbers", fontsize=14)
# ax.tick_params(labelsize=14)  # set the size of the x and y labels 


# ax.set_xlabel("value", fontsize=14)
# ax.set_ylabel("Square of value", fontsize=14)
# plt.show()

# x_values=range(1,1001)
# y_values=[x**2 for x in x_values]

# plt.style.use('seaborn-v0_8')

# fig,ax = plt.subplots   ()

# ax.scatter(x_values,y_values, s=10,c=y_values,cmap=plt.cm.boneZ)

# ax.axis([0,1100,0,1_100_000]) 

# #  ------------------CUSTOMIZE THE GRAPH----------------------------------------

# ax.set_title("Square Numbers", fontsize=14)
# ax.tick_params(labelsize=14)  # set the size of the x and y labels 
# ax.ticklabel_format(style='plain')


# ax.set_xlabel("value", fontsize=14)
# ax.set_ylabel("Square of value", fontsize=14)

# plt.show()

#------------------------------------Practice question---------------------------------

fig, ax= plt.subplots(figsize=(10,6))

x_axis=range(1,5001)

y_axis=[ x** 3 for x in x_axis]

ax.axis([0,5000,0,125_000_000_000])

ax.ticklabel_format(style='plain')

ax.scatter(x_axis,y_axis,s=10, c=x_axis,cmap=plt.cm.Accent)



plt.savefig("FIG_2.pdf")

plt.show()
