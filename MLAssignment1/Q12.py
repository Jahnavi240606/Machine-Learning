import numpy as np
import matplotlib.pyplot as plt
V1 = np.random.rand(100)
V2 = V1 ** 2
plt.plot(V1, label='V1', color='blue')
plt.plot(V2, label='V2 (V1 squared)', color='green')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Plot of V1 and V2')
plt.legend()
plt.show()

