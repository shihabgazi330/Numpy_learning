# Numpy Tutorial

import numpy as np

## Array

### Creating a one dimensional array

my_arr = np.array([3,4,5,6,7,8]) 

my_arr

my_arr[0]

### Creating a 2 dimensional array

two_d_array = np.array([[1,2,3,4,5,6,7,8,9,0]], np.int64)

two_d_array[0]

two_d_array[0,0]

two_d_array[0,1]

two_d_array.shape

s = two_d_array

s.dtype

s[0,1] = 45

s

two_d_array[0]

## Conversion from other Python Structures

list_array = np.array([[1,2,3,5],[123,4,3,24]])

list_array

list_array.dtype

list_array.size

np.array({1,2,3,5,6,8,3})

zeros = np.zeros((2,3))

zeros

print(zeros)

zeros.dtype

type(zeros)

range_ = np.arange(15)

range_

linspace_ = np.linspace(1,200,5)

linspace_

emp = np.empty((4,6))
emp

emp_like = np.empty_like(linspace_)

emp_like

ide = np.identity(45)
ide

ide.shape

arr = np.arange(99)

arr

arr.reshape(3, 33) # since total number of items is 99 and 3#33

# arr.reshape(3, 31) # throws an error as 99 items can't be devided in 3#31 i.e. 93 items

# arr has not changed yet

arr

# Changing arr

arr = arr.reshape(3,33)

arr

arr = arr.ravel()

arr

arr.shape

x = [[1,2,3,4],[1,2,0,3],[1,2,4,20]]

ar = np.array(x)

ar

ar.sum(axis = 0)

ar.sum(axis = 1)

y =  [[1,2,3,4],[1,2,0,3],[1,2,4,0]]

z =  [[1,2,3,4],[1,2,0,3],[1,2,4,0]]

three_dim = [x,y,z,x]

three_dim

ar.T

ar.flat

for item in ar.flat:
    item

for item in ar.flat:
    print(item)

print(item)

ar.ndim

ar.size

ar.nbytes

one = np.array([1,35,"",6,3,56,7])

one.argmax()

one.argmin()

one.argsort()

### functioning on ar

ar.argmax()

ar.argmin()

ar.argsort()

np.sort

ar

ar.argmax(axis = 0)

ar.argmax(axis = 1)

ar.argmin(axis = 0)

ar.argmin(axis = 1)

ar.ravel()

ar.reshape((6,2))

ar

ar2 = np.array([[1,.4,3,4],
               [3.,2,4,2],
               [2,7,4,166]])

ar+ar2

ar*ar2

np.sqrt(ar2)

ar2

np.where(ar2>5)

type(np.where(ar2>5))

np.count_nonzero(ar)

type(np.count_nonzero(ar))

ar

np.nonzero(ar)

ar[2,1] = 0

np.nonzero(ar)

import sys

py_ar = [0,3,4,5,2]

np_ar = np.array(py_ar)

sys.getsizeof(1)*len(py_ar)

np_ar.itemsize*np_ar.size

np_ar.tolist()
