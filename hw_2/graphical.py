import matplotlib.pyplot as plt
import numpy as np

# set line ranges, [-1.,5.;-2.,8.]
x = np.arange(0. ,5. ,1.)
constraints = [ [ x, (24. - 6 * x) / 4., r"$6 x_1 + 4 x_2 = 24$" ],
                [ x, (6. - x) / 2.     , r"$  x_1 + 2 x_2 =  6$" ],
				[ x, 1. + x            , r"$- x_1 +   x_2 =  1$" ],
				[ x, 2. + x * 0.       , r"$          x_2 =  2$" ] ]

# get plot objs
fig = plt.figure()
mp = plt.subplot(111)

# plot constrains
for c in constraints :
  mp.plot(c[0], c[1], label = c[2])

# plot feasible area
y = constraints[0][1]
for i in range(0,len(constraints)) :
  y = np.minimum(y, constraints[i][1])
mp.fill_between(x, y, color="blue", alpha=0.5)

# plot corner points and objective lines
corner_points = [ [0., 0.], [0., 1.], [1., 2.], [2., 2.], [3., 3./2], [4., 0.] ]
for pt in corner_points :
  dx = np.arange(pt[0] - 0.5, pt[0] + 0.5, 0.05)
  dy = (5 * pt[0] + 4 * pt[1] - 5. * dx) / 4.
  mp.plot(dx, dy, 'k--')
  mp.text(pt[0] + 0.05, pt[1] + 0.05, r"$z = " + str(5 * pt[0] + 4 * pt[1]) + "$")

# plot axes and legend box
box = mp.get_position()
mp.set_position([box.x0, box.y0, box.width * 0.7, box.height])
mp.plot([0.,5.],[0.,0.],'k-',[0.,0.],[0.,6.],'k-')


mp.legend(loc=2, bbox_to_anchor=(1,1))
plt.show()
