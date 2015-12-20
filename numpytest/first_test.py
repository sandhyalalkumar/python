import numpy as np
a = np.arange(27).reshape(9,3)
print "nDim array"
print a
print "Shape"
print a.shape
print "Type"
print type(a)
print "An element"
print a[5][2]
print "nDim array dimension"
print a.ndim
print "Data type name"
print a.dtype.name
print "Total bytes of each items"
print a.itemsize
print "Total no items"
print a.size

