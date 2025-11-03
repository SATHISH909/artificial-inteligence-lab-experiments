import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset (XOR problem)
inputs = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Output labels
outputs = np.array([[0], [1], [1], [0]])

# Set random seed for reproducibility
np.random.seed(42)

# Initialize weights and biases
input_neurons = 2
hidden_neurons = 3
output_neurons = 1

# Random weights between -1 and 1
weights_input_hidden = 2 * np.random.random((input_neurons, hidden_neurons)) - 1
weights_hidden_output = 2 * np.random.random((hidden_neurons, output_neurons)) - 1

bias_hidden = np.zeros((1, hidden_neurons))
bias_output = np.zeros((1, output_neurons))

# Learning rate
lr = 0.5

# Training process
for epoch in range(10000):
    # Feedforward
    hidden_layer_input = np.dot(inputs, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)

    final_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    final_output = sigmoid(final_layer_input)

    # Backpropagation
    error = outputs - final_output
    d_output = error * sigmoid_derivative(final_output)

    error_hidden = d_output.dot(weights_hidden_output.T)
    d_hidden = error_hidden * sigmoid_derivative(hidden_layer_output)

    # Update weights and biases
    weights_hidden_output += hidden_layer_output.T.dot(d_output) * lr
    weights_input_hidden += inputs.T.dot(d_hidden) * lr

    bias_output += np.sum(d_output, axis=0, keepdims=True) * lr
    bias_hidden += np.sum(d_hidden, axis=0, keepdims=True) * lr

# Final output after training
print("🔹 Final Output after Training:")
print(final_output.round(3))
