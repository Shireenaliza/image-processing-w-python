import numpy as np
list1 =[1,2,3,'apple']
type(list1)

arr1 = np.array(list1)
arr1

np.arange(0,10)
np.arange(0,10,2)

#zeros(shape, dtype = float , order = 'c')
np.zeros(shape =(5,5))  #rows,col

#numpy by default produce floats

np.ones((2,4))

np.random.seed(101)
arr = np.random.randint(0,100,10)       #randint(low,high=none , size=none , dtype ='1')
arr2 = np.random.randint(0,100,10)

arr.max()   #min()
arr.argmax()  #argmin()
arr.mean()  #avg value

#reshape arrays
#arr.shape == (10,)

arr.reshape((2,5))  #move around EXISTING elements

matrix = np.arange(0,100).reshape(10,10)
matrix

#indexing, matrix[row,col]
#slicing, matrix[row no. , col, no]

matrix[:,1].reshape((10,1))

matrix[0:3,0:3]

mat2 = matrix.copy()
mat2[0:10,0:10] = 1
mat2
matrix
