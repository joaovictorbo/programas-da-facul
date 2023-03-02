import numpy as np

def distance(p1, p2):
      x1 = p1[0] - p2[0]
      x2 = p1[1] - p2[1]
      x1 = x1**2
      x2 = x2**2
      x3 = x1+x2
      x3 = np.sqrt(x3)
      return x3












print(distance(np.array([0,0]), np.array([1,1])))