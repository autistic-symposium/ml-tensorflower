## Numpy Resources

### Arrays

* Grid of values, all of the same type.
* The number of dimensions is the rank of the array.
* The shape of an array is a tuple of integers giving the size of the array along each dimension.


```
a = np.array([1, 2, 3])  # Create a rank 1 array
print a.shape            # Prints "(3,)"
```

```
numpy.asarray([])
numpy.asarray([]).shape
```


* Many functions to create arrays:

```
a = np.zeros((2,2))  # Create an array of all zeros
b = np.ones((1,2))   # Create an array of all ones
c = np.full((2,2), 7) # Create a constant array
d = np.eye(2)        # Create a 2x2 identity matrix
e = np.random.random((2,2)) # Create an array filled with random values
```

* Products:


```
x = np.array([[1,2],[3,4]])

v = np.array([9,10])
w = np.array([11, 12])

# Inner product of vectors
print v.dot(w)
print np.dot(v, w)

# Matrix / vector product
print x.dot(v)
print np.dot(x, v)
```

* Sum:

```
print np.sum(x)  # Compute sum of all elements
print np.sum(x, axis=0)  # Compute sum of each column
print np.sum(x, axis=1)  # Compute sum of each row
```

* Broadcasting is a  mechanism that allows numpy to work with arrays of different shapes when performing arithmetic operations. Frequently we have a smaller array and a larger array, and we want to use the smaller array multiple times to perform some operation on the larger array.



