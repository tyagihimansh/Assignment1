##QR decomposition

import numpy as np
A=np.array([[5,-2],[-2,8]])
q,r= np.linalg.qr(A)
print(q,r)

##for eigenvalue using QR decomposition
j=A

for k in range(50):
  i=j
  q,r=np.linalg.qr(i)
  j=np.dot(r,q)

print(j)


##Eigenvalues using numpy
z=np.linalg.eigh(A)
print("eigenvalues",z)
