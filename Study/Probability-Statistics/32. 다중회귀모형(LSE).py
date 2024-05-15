import numpy as np
from numpy.linalg import inv

# 다중 회귀

y = [91, 72, 65, 69, 89, 85, 73, 93, 88, 80, 62, 86, 89, 81, 72, 78]
x1 = [9, 7, 8, 6, 11, 10, 8, 4, 8, 6, 5, 3, 12, 7, 6, 5]
x2 = [8, 5, 3, 4, 9, 6, 5, 12, 7, 4, 2, 10, 8, 9, 4, 8]
x0 = [1]*len(x1)

x = [x0, x1, x2]
X = np.array(x)
X = X.T
Y = np.array(y)
Y = Y.T

Beta = np.dot(np.dot(inv(np.dot(X.T,X)),X.T),Y)
print(Beta)
