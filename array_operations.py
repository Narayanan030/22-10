#array operations

#sum
import numpy as np
np.sum([0.5, 1.5])

#mean
import numpy as np
a = np.array([[1, 2], [3, 4]])
np.mean(a)

#std
import numpy as np
a = np.array([[1, 2], [3, 4]])
np.std(a)

#min
import numpy as np
a = np.array([[1, 2], [3, 4]])
np.min(a)

#max
import numpy as np
a = np.array([[1, 2], [3, 4]])
np.max(a)

#argmin
x = np.arange(24).reshape((2, 3, 4))
res = np.argmin(x, axis=2, keepdims=True)
res.shape

#argmax
b = np.arange(6)
b[2] = 5
np.argmax(b)  

#matmul
a = np.array([[1, 0],
              [0, 1]])
b = np.array([[4, 1],
              [2, 2]])
np.matmul(a, b)

#dot
import numpy as np
np.dot(3, 4)

#clip
import numpy as np
a = np.arange(10)
a
np.clip(a, 0, 5)


