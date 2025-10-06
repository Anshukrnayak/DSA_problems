import numpy as np

# One dimensional array 
arr=np.array([1,2,3,4,5])
print(arr)
print(type(arr))


# Two Dimensional array

arr2=np.array([[1,2,3],[4,5,6]])
print('Two dimensional array ')
print(arr2)

# Zeros array 

print('Zeros array')

arr3=np.zeros((3,4))
print(arr3)

print('Ones array ')

arr4=np.ones((3,2))
print(arr4)

# Identity matrix 

print('Identity matrix ')

arr5=np.identity((5))

print(arr5)

# a range 
print(' Arrange array ')
arr6=np.arange(4,10,2)
print(arr6)

# line space function 

arr7=np.linspace(10,20,10)
print(arr7)







