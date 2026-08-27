#!/usr/bin/env python3
"""
Builds a neural network with Keras
"""
import tensorflow.keras as K


def build_model(nx, layers, activations, lambtha, keep_prob):
    """
    Builds a neural network with Keras library

    parameters:
        nx [int]: number of input features
        layers [list]: number of nodes in each layer
        activations [list]: activation function for each layer
        lambtha [float]: L2 regularization parameter
        keep_prob [float]: probability that a node will be kept for dropout

    returns:
        the compiled keras model
    """
    reg = K.regularizers.l2(lambtha)
    init = K.initializers.he_normal()
    inputs = K.Input(shape=(nx,))

    # First layer
    layer = K.layers.Dense(
        layers[0],
        activation=activations[0],
        kernel_initializer=init,
        kernel_regularizer=reg
    )(inputs)

    # Remaining layers
    for i in range(1, len(layers)):
        drop = K.layers.Dropout(rate=(1 - keep_prob))(layer)
        layer = K.layers.Dense(
            layers[i],
            activation=activations[i],
            kernel_initializer=init,
            kernel_regularizer=reg
        )(drop)

    return K.Model(inputs=inputs, outputs=layer)
