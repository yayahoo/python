import matplotlib.pyplot as plt
from random_walk import RandomWalk


rw = RandomWalk()
rw.data()
steps = list(range(len(rw.x)))

# cur = plt.axes()
# cur.get_xaxis().set_visible(False)
# cur.get_yaxis().set_visible(False)
plt.scatter(rw.x,rw.y,c=steps,cmap=plt.cm.Blues ,edgecolor = 'none', s=5)
plt.scatter(0,0,c = 'green', s = 20)
plt.scatter(rw.x[-1],rw.y[-1],c = 'red', s=20)
plt.quiver([0,rw.x[-1]],[0,rw.y[-1]],color='black')
# plt.axis('off')
plt.show()

