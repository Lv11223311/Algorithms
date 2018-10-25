from primitive_calculator import optimal_sequence
import numpy as np

for i in range(100):
    n = np.random.randint(1, 2000)
    sequence = list(optimal_sequence(n))
    print(n ,len(sequence) -1)