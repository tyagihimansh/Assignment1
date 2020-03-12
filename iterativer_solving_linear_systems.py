import numpy as np


##Using Jacobi Method

x1 = np.array([7.859713071,0.422926408,-0.073592239,-0.540643016,0.010626163])
A = np.array([[0.2,0.1,1,1,0],[0.1,4,-1,1,-1],[1,-1,60,0,-2],[1,1,0,8,4],[0,-1,-2,4,700]])
b = np.array([1,2,3,4,5])
n = 5
i = np.identity(n)
p = A*i
R = A-p
x2 = np.array([0.0,0.0,0.0,0.0,0.0])
pi = np.identity(n)

x=x2
for i in range(n):
    pi[i,i] = 1/p[i,i]


    
for i in range(500):
    x = np.dot(pi,(b-np.dot(R,x)))
    if np.amax(np.absolute(x-x1))<0.01:
        break
print(i+1)
print(x)

##Using Gauss Sidel Method

print("1",x2)
for i in range(500):
    for j in range(n):
        d = b[j]
        for k in range(n):
            if(j!=k):
                d = d-(A[j][k]*x[k])
        x[j] = (d/A[j][j])
    if np.amax(np.absolute(x-x1))<0.01:
        break
print(i+1)
print(x)

##Using Relaxation Method

x=np.array([0.0,0.0,0.0,0.0,0.0])
w=1.25
for i in range(500):
    for j in range(n):
        d=b[j]
        for k in range(n):
            if(j!=k):
                d=d-(A[j][k]*x[k])
        x[j]=(w*(d/A[j][j]))+(x[j]*(1-w))
    if np.amax(np.absolute(x-x1))<0.01:
        break
print(i+1)
print(x)


## Using Conjugate Gradient Method
x=np.array([0.0,0.0,0.0,0.0,0.0])
r=b-np.dot(A,x)
p=r
for i in range(500):
    al=(np.dot(r,r))/(np.dot(p,np.dot(A,p)))
    x=x+(al*p)
    r1=r-(al*np.dot(A,p))
    be=(np.dot(r1,r1))/(np.dot(r,r))
    p=r1+(be*p)
    r=r1
    if np.amax(np.absolute(x-x1))<0.01:
        break
print(i+1)
print(x)


