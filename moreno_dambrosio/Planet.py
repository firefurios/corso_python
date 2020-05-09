import numpy as np
class Planet:
	def __init__(self,M,m,rx,ry,rz,vx,vy,vz,dt,num,n):
		self.N=n
		self.Num=num
		self.ma=m
		self.Ma=M
		self.dT=dt
		self.R=np.zeros(shape=(self.N+1,self.Num,3))
		self.V=np.zeros(shape=(self.N+1,self.Num,3))
		self.A=np.zeros(shape=(self.N+1,self.Num,3))
		self.E=np.zeros(self.N)
		for i in range(self.Num):
			self.R[0][i]=[rx[i],ry[i],rz[i]]
			self.V[0][i]=[vx[i],vy[i],vz[i]]
		for ns in range(self.N):
			for i in range(self.Num):
				self.E[ns]+=0.5*self.ma[i]*(np.linalg.norm(self.V[ns][i]))**2-(
						6.67e-11*self.Ma*self.ma[i]/(np.linalg.norm(self.R[ns][i])))
				self.A[ns+1][i]=-(self.R[ns][i]/((np.linalg.norm(self.R[ns][i]))**3))*6.67e-11*self.Ma
				for j in range(self.Num):
					if j!=i:
						self.A[ns+1][i]-=6.67e-11*self.ma[j]*(
						(self.R[ns][i]-self.R[ns][j])/((np.linalg.norm(self.R[ns][i]-self.R[ns][j]))**3))
						self.E[ns]-=6.67e-11*self.ma[j]*self.ma[i]/(np.linalg.norm(self.R[ns][i]-self.R[ns][j]))
			self.V[ns+1]=self.V[ns]+0.5*self.A[ns]*self.dT
			self.R[ns+1]=self.R[ns]+self.V[ns+1]*self.dT
			self.V[ns+1]=self.V[ns+1]+0.5*self.A[ns+1]*self.dT
			print(self.E[ns]/self.E[0])


	def pos(self):
		return self.R

if __name__ == "__main__":
	p=Planet(1,3,1,2,1,0,10,20,0.1)
	print(p.R[1])
	a=p.pos()
	print(a[1])