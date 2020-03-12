import numpy as np

A=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])

x=np.array([[1],[1],[1]])
r=x
for i in range(10):
  y=r
  r=np.dot(A,y)

e=np.linalg.norm(r)/np.linalg.norm(y)

print(e)
print(r/np.linalg.norm(r))

##using numpy
print(np.linalg.eigh(A))
