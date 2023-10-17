import tensorflow as tf

# Define a sample input with dimensions (batch_size, height, width, channels)
input_shape = (None, 28, 28, 3)  # None in batch_size means it can vary

# Create a Conv2D layer with 32 filters, a 3x3 kernel, and 'valid' padding
conv_layer = tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=input_shape[1:])

# Print layer summary
conv_layer.summary()
