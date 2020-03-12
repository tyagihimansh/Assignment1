# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 14:09:39 2020

@author: Himanshu Tyagi
"""

import numpy as np
a= np.array([[1,0.67,0.33],[0.45,1,0.55],[0.67,0.33,1]])
b=np.array([2,2,2])
x= np.linalg.solve(a,b)
print (x)


#On comparing the result using code and doing manually, I got the same results.
