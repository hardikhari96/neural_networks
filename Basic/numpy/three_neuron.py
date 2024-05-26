import numpy as np

# Input values to the neural network
inputs = np.array([1, 2, 3, 2.5])

# Weights for the connections to the neurons
weights = np.array([
    [0.2, 0.8, -0.5, 1.0],  # Weights for the first neuron
    [0.5, -0.1, 0.4, 5.0],  # Weights for the second neuron
    [0.1, 0.2, -0.4, 9.0]   # Weights for the third neuron
])

# Biases for the neurons
biases = np.array([3, 5, 0.2])

# Calculate the output of the neurons
outputs = np.dot(weights, inputs) + biases

print(outputs)
