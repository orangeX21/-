import random

import numpy as np
import pandas as pd

# A1 = nq.random.randint(60,100,size = 20)
# B1 = nq.random.randint(60,100,size = 20)
# idx=["name" + str(i) for i in range(20) ]
# s1 = pd.series(A,)
A = np.random.randint(60, 100, size=20)
d = pd.Series(A, name="score", copy=False)
A[0] = -20
d.head(2)
