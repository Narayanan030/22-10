#Indexing and Slicing  

#where
import numpy as np
a = np.arange(10)
np.where(a < 5, a, 10*a)

#argwhere
import numpy as np
x = np.arange(6).reshape(2,3)
np.argwhere(x>1)

#sort
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

#argsort
ind = np.argsort(x, axis=0) 
ind
np.take_along_axis(x, ind, axis=0) 
