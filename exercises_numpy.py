## Numpy

# 1. Import the NumPy library. 
import numpy as np

# 2. Create an array with the shape of 3x6x4 which has elements between 0 and 10. 
array = np.random.randint(0,10,size=(3,6,4))

# 3. Print the number of elements, dimension, shape, and data type of the array. 
array.shape
array.size
type(array)
array.ndim
array.dtype

# 4. Change the data type of the array to float64. 
array.astype("float64").dtype #np.float64(array)

# 5. Reshape the array to have 2 dimensions. 
array = np.random.randint(0,10,size=(2,6,4))

# 6. Create x and y array that have shape 2x3 and has elements between 0 and 50. 
x = np.random.randint(0,50,size=(2,3))
y = np.random.randint(0,50,size=(2,3))

# 7. Concatenate the two arrays by rows. 
h_xy = np.hstack((x,y))

# 8. Concatenate the two arrays by columns.
v_xy = np.vstack((x,y))
