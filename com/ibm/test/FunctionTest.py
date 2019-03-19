#-*-coding:utf-8 -*-
'''
Created on Nov 7, 2018

@author: jyp
'''
import numpy as np
import math
import matplotlib.pyplot as pt
print('Sigmoid函数')

#print (np.arange(3))

def sig(a):
    '''sigmoid函数
    input:x(mat)feature*w
    output:sigmoid(x)(mat):sigmoid值
    '''
    #return 1/(1+math.exp(-x))
    return math.pow(a,2)

'''
x = np.arange(1,10)
print (x)
y = [sig(xi) for xi in x]
print(y)
'''
#pt.plot(x,y)
#pt.xlim(0,10)  
#pt.ylim(-1.2,1.2)   
#pt.show()
x = np.arange(0 , 360)  
print(x)
y = np.sin(x * np.pi / 180.0)  
print(y)
pt.plot(x,y)  
pt.xlim(0,360)  
pt.ylim(-1.2,1.2)  
pt.title("SIN function")  
pt.show()  