import matplotlib.pyplot as pl
a=[-1,2,3,4]
b=[-2,4,6,8]
pl.xlabel("x axis")
pl.ylabel("y axis")
pl.plot(a,b,'rd',markeredgecolor='k',markersize=10,linewidth=2,linestyle='dotted')
pl.plot(a,[-2,2,3.4,8],'kv',markeredgecolor='k',markersize=10,linewidth=2,linestyle='dotted')
pl.show()