import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
from Planet import Planet
import sys

num=int(input("inserisci il numero di pianeti: "))
T=int(input("inserisci il numero di giorni in cui studiare il moto: "))
dt=float(input("inserisci il timestep in giorni: "))
M=float(input("inserisci la massa della stella: "))
N=int(T/dt)
dt=dt*24*60*60
rx=np.zeros(num)
ry=np.zeros(num)
rz=np.zeros(num)
vx=np.zeros(num)
vy=np.zeros(num)
vz=np.zeros(num)
px=np.zeros(shape=(N,num))
py=np.zeros(shape=(N,num))
pz=np.zeros(shape=(N,num))
m=np.zeros(num)

for i in range(num):
	m[i]=float(input("inserisci la massa: "))
	rx[i]=1000*float(input("inserisci le coordinate x, y, z in km: "))
	ry[i]=1000*float(input())
	rz[i]=1000*float(input())
	vx[i]=1000*float(input("inserisci le velocità iniziali vx, vy, vz in km/s: "))
	vy[i]=1000*float(input())
	vz[i]=1000*float(input())

b=Planet(M,m,rx,ry,rz,vx,vy,vz,dt,num,N)

px=b.pos()[:,:,0]
py=b.pos()[:,:,1]
pz=b.pos()[:,:,2]


fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
if num==1:
	ax.set_xlim3d([min(px[:,0])-1000,max(px[:,0])+1000])
	ax.set_ylim3d([min(py[:,0])-1000,max(py[:,0])+1000])
	ax.set_zlim3d([min(pz[:,0])-1000,max(pz[:,0])+1000])
else:
	ax.set_xlim3d([min(np.transpose(px).min(1))-1000,max(np.transpose(px).max(1))+1000])
	ax.set_ylim3d([min(np.transpose(py).min(1))-1000,max(np.transpose(py).max(1))+1000])
	ax.set_zlim3d([min(np.transpose(pz).min(1))-1000,max(np.transpose(pz).max(1))+1000])
ax.set_title('Planets Orbits in {} days with {} timestep'.format(T,dt/(24*60*60)))
sun,=ax.plot([],[],[],'o',color='orange',markersize=5)
orbit=[]
planet=[]
for j in range(num):
	orbit.extend(ax.plot([],[],[],alpha=0.8,lw=2))
	planet.extend(ax.plot([],[],[],'o',color='blue',markersize=2))


def init():
	for j in range(num):
		orbit[j].set_data([],[])
		orbit[j].set_3d_properties([])
		planet[j].set_data([],[])
		planet[j].set_3d_properties([])
	sun.set_data([0],[0])
	sun.set_3d_properties([0])
	return orbit, planet, sun

def animate(i):
	for j in range(num):
		orbit[j].set_data(np.transpose(px)[j][:2*i],
							np.transpose(py)[j][:2*i])
		orbit[j].set_3d_properties(np.transpose(pz)[j][:2*i])
		planet[j].set_data(np.transpose(px)[j][2*i],
							np.transpose(py)[j][2*i])
		planet[j].set_3d_properties(np.transpose(pz)[j][2*i])
	return orbit, planet, sun


def loganim(i,n):
	if (i%100==0): print(f'Saving frame {i} of {n}')


anim = animation.FuncAnimation(fig, animate, init_func=init,
							frames=N//2, interval=2, blit=False)

anim.save('sistemastellare.mp4', writer='ffmpeg',fps=30, dpi=100,
			progress_callback=loganim)
sys.exit()