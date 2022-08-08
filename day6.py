import numpy as np

print(np.array([1,2,3]))

# 1: Create x array with elements equal to 1.
x = np.ones((2,3))


# 2: Create y array with elements equal to 0.
y = np.zeros((2, 3))


# 3: Add x and y arrays.
r = np.add(x, y)
print(r)

# 4: Print x array characteristics (e.g: dimension, shape, size, t
print(x.shape)
print(x.size)
print(x.ndim)
print(x.dtype)

# 5: Create a 2D array "called w"
w = np.array([[11, 12, 13],
              [14, 15, 16]])
print(w)

# 6: Create z array contains the numbers from 1 to 3
z = np.arange(1, 4)
print(z)
# 7: Combine the arrays z and w in vertical way then save it in
newArray = np.vstack((z, w))
print(newArray)

# 8: Print all elements of "newArray" using the loop.
for i in newArray:
    print(i)

# 9: Reverse the columns and rows of "newArray".
print(newArray.transpose())

# 10: Decrement all elements of "newArray" with 1.
newArray += 1
print(newArray)

# 11: Find smallest and biggest values in "newArray".
print(newArray.min())
print(newArray.max())

# 12: Print the first row of "newArray" using indexing.
print(newArray[0])

# 13: Print the number equals 12 of "newArray" using indexing.
print(newArray[newArray == 12])


# 14: Print the numbers equal 0 and 13 of "newArray" using Slicing.
print(newArray[[0, 2], 0:1])

# 15: Change the shape of "newArray" to (9,1).
newArray.reshape(9,1)

# 16: Change the shape of "newArray" to (3,2).
newArray.reshape(3,2)







































