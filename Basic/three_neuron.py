# 3 neurons  with 4 input --- output layer
# Input values to the neural network
inputs = [1, 2, 3, 2.5]

# Weights for the connections to the first neuron
weights = [0.2, 0.8, -0.5, 1.0]

# Weights for the connections to the second neuron
weights1 = [0.5, -0.1, 0.4, 5.0]

# Weights for the connections to the third neuron
weights2 = [0.1, 0.2, -0.4, 9.0]

# Bias for the first neuron
bias = 3

# Bias for the second neuron
bias2 = 5

# Bias for the third neuron
bias3 = 0.2

# Calculate the output of the first neuron
# The output is the sum of the input values each multiplied by their corresponding weight plus the bias
output1 = inputs[0] * weights[0] + inputs[1] * weights[1] + inputs[2] * weights[2] + inputs[3] * weights[3] + bias

# Calculate the output of the second neuron
output2 = inputs[0] * weights1[0] + inputs[1] * weights1[1] + inputs[2] * weights1[2] + inputs[3] * weights1[3] + bias2

# Calculate the output of the third neuron
output3 = inputs[0] * weights2[0] + inputs[1] * weights2[1] + inputs[2] * weights2[2] + inputs[3] * weights2[3] + bias3

# Combine the outputs of the three neurons into a single list
output = [output1, output2, output3]

# Print the output of the network
print(output)

