from math import exp

def activate(weights, inputs):
    activation = weights[-1]  # Bias term
    for i in range(len(weights) - 1):
        activation += weights[i] * inputs[i]
    print('Activation value : ', activation)
    return activation

# Transfer neuron activation to output
def transfer(activation):
    return 1.0 / (1.0 + exp(-activation))

# Forward propagate input to a network output
def forward_propagate(network, row):
    inputs = row
    for layer in network:
        new_inputs = []
    for neuron in layer:
        activation = activate(neuron['weights'], inputs)
        neuron['output'] = transfer(activation)
        new_inputs.append(neuron['output'])
    inputs = new_inputs
    return inputs

# Test forward propagation
network = [
    [{'weights': [0.13, 0.84]}],  # Adding bias term to weights
    [{'weights': [0.25, 0.49]}],  # Adding bias term to weights
    [{'weights': [0.44, 0.65]}]   # Adding bias term to weights
]
row = [1, 0, None]  # Including bias input of 1 in the input row
output = forward_propagate(network, row)
print('Output : ', output)
