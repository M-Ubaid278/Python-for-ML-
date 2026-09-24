import numpy as np
import matplotlib.pyplot as plt

# x_axis=np.arange(1,9,1)
# y_axis=np.arange(3,27,3)


# x_axis_p=[1,2,3,4,5,6,7,8]
# y_axis_p=[3,6,9,12,15,18,21,24]

# x_axis1=[-1,-2,-3,-4,-5]
# y_axis1=[1,4,9,16,25]


# plt.title("Hello-My graph")

# plt.xlabel("X-AXIS")
# plt.ylabel("Y_AXIS")



# plt.bar(x_axis,y_axis)
# plt.polar(x_axis_p, y_axis_p)


# plt.plot(x_axis1,y_axis1)

# plt.figure(figsize=(10,5),dpi=100)
# # plt.plot(x_axis,y_axis)

#  ------------------CREATE THE SUBPLOTS-----------------------------------

# plt.subplot(2,2,1)
# plt.plot(x_axis,y_axis,"red")

# plt.subplot(2,2,2)
# plt.plot(x_axis,y_axis,"blue")

# plt.subplot(2,2,3)
# plt.plot(x_axis,y_axis,"black")

# plt.subplot(2,2,4)
# plt.plot(x_axis,y_axis,"yellow")

# fig=plt.figure()

# axes=fig.add_axes([0.25,0.25,0.5,0.5])

# figure = plt.figure()

# axes = figure.add_axes([0.25, 0.25, 0.5, 0.5])

# axes.plot(x_axis,y_axis)

# axes.set_xlabel("X_Axis")
# axes.set_ylabel("Y_Axis")

# axes.set_title("Graph")



# plt.show()

# --------------------------------------FIGURE CUSTOMIZATION-----------------------------------------------


# figure, axes=plt.subplots(nrows=2,ncols=1)

# plt.tight_layout()

# axes.plot(x_axis,y_axis)

# print(type(axes))
# print(axes[0])
# print(axes[1])


# for i in axes:
#     print(i.plot(x_axis,y_axis))

# axes[0].plot(x_axis,y_axis,color="red")
# axes[1].plot(x_axis,y_axis **2)


# plt.show()


# --------------------------------------PLOT CUSTOMIZATION-----------------------------------------------

fig=plt.figure()

axes=fig.add_axes([0.25,0.25,0.5,0.5])

x_axis=np.arange(1,9,1)
y_axis=x_axis **2

# plt.plot(x_axis,y_axis)

axes.plot(x_axis,y_axis,color="orange",linewidth="5", marker="D", markersize=10, markerfacecolor="blue" , markeredgecolor="red")

plt.savefig("my graph.png")
plt.show()



