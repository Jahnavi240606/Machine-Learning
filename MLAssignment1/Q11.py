import numpy as np
import matplotlib.pyplot as plt
V1 = np.random.rand(100)
V1_sorted = np.sort(V1)
plt.plot(V1_sorted, color='red')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Sorted Vector V1 in Increasing Order')
plt.show()

