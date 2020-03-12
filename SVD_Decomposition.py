## for SVD decomposition A=U*S*V(transpose)
import time
import numpy as np
A=np.array([[0,1,1],[0,1,1],[1,1,0],[0,1,0],[1,0,1]])

t1=time.time()
B= np.transpose(A)

C=np.dot(A,B)
D=np.dot(B,A)
E=np.linalg.eigh(C)[1]
E[:,[0,1,2,3,4]]=E[:,[4,3,2,1,0]]
F=np.linalg.eigh(D)[1]
F[:,[0,1,2]]=F[:,[2,1,0]]


print("S",np.sqrt(np.linalg.eigh(D)[0]))

print("U",E)

print("V",F)
t2=time.time()
print('time=',t2-t1)


##using numpy function
t3=time.time()
l=np.linalg.svd(A)

print('svd',l)
t4=time.time()
print('time=',t4-t3)

