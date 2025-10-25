# takes 5 inputs
# has three hidden layers
# has 3 nodes in the first layer, 2 nodes in the second layer, and 3 nodes in the third layer
# has 1 node in the output layer

import numpy as np
from random import seed


def initialize_network(input_no, number_layers, nodes, number_node_output):
    network = {}
    num_nodes_previous = input_no
    for layer in range(number_layers +1):
        if layer == number_layers:
            layer_name = "Output Layer"
            current_nodes = number_node_output
        else:
            layer_name = "Layer_{}".format(layer+1)
            current_nodes = nodes[layer]

        network[layer_name] = {}
        for node in range(current_nodes):
            node_name = "Node_{}".format(node+1)
            network[layer_name][node_name] = {
                'weights' : np.around(np.random.uniform(size=num_nodes_previous), decimals= 2),
                'bias' : np.around(np.random.uniform(size=1), decimals=2),
            }
        num_nodes_previous = current_nodes
    
    return network

# Start with the input layer as the input to the first hidden layer.
# Compute the weighted sum at the nodes of the current layer.
# Compute the output of the nodes of the current layer.
# Set the output of the current layer to be the input to the next layer.
# Move to the next layer in the network.
# Repeat steps 2 - 5 until we compute the output of the output layer.

def compute_weighted_sum(inputs, weights, bias):
    return np.sum(inputs * weights) + bias
def node_activation(weighted_sum):
    return 1.0 / (1.0 + np.exp(-1 * weighted_sum))
np.random.seed(12)
inputs = np.around(np.random.uniform(size=5), decimals=2)

small_network = initialize_network(5,3,[3,2,3],1)

weighted_sum_from_first_node = compute_weighted_sum(inputs, small_network["Layer_1"]["Node_1"]["weights"], small_network["Layer_1"]["Node_1"]["bias"]) 

activation_from_first_node = node_activation(weighted_sum_from_first_node)
print(weighted_sum_from_first_node)
print(activation_from_first_node)

def forward_propagate(network, inputs):
    
    layer_inputs = list(inputs) # start with the input layer as the input to the first hidden layer
    
    for layer in network:
        
        layer_data = network[layer]
        
        layer_outputs = [] 
        for layer_node in layer_data:
        
            node_data = layer_data[layer_node]
        
            # compute the weighted sum and the output of each node at the same time 
            node_output = node_activation(compute_weighted_sum(layer_inputs, node_data['weights'], node_data['bias']))
            layer_outputs.append(np.around(node_output, decimals=4))
            
        if layer != 'Output Layer':
            print('The outputs of the nodes in hidden layer number {} is {}'.format(layer.split('_')[1], layer_outputs))
    
        layer_inputs = layer_outputs # set the output of this layer to be the input to next layer

    network_predictions = layer_outputs
    return network_predictions

final_output = forward_propagate(small_network,inputs)

print(final_output)






