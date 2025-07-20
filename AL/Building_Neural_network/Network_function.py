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


def forward_propogation(network, input):
    for layer in network:
        output_of_this_layer = []
        for node in network[layer]:
            weighted_sum = compute_weighted_sum(input, network[layer][node]["weights"], network[layer][node]["bias"])
            activation = node_activation(weighted_sum)
            output_of_this_layer.append(activation)
        input = output_of_this_layer
    return input
final_output = forward_propogation(small_network,inputs)

print(final_output)





