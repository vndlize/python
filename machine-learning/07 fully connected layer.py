# import tensorflow as tf

# # Define the input shape
# input_shape = (None, 64)  # Input shape (batch_size, input_size)

# # Create a tensor for input data with initial zeros
# input_data = tf.Variable(initial_value=tf.zeros(input_shape), dtype=tf.float32)

# # Define the weight matrix and bias
# weights = tf.Variable(initial_value=tf.random.normal([64, 128]), dtype=tf.float32)  # Weight matrix (input_size, num_units)
# bias = tf.Variable(initial_value=tf.zeros([128]), dtype=tf.float32)  # Bias vector (num_units)

# # Perform matrix multiplication and add bias
# fully_connected_layer = tf.matmul(input_data, weights) + bias

# # Apply activation function (ReLU in this example)
# output = tf.nn.relu(fully_connected_layer)

# # Print the output
# print(output)

# code NOT WORKING ???
