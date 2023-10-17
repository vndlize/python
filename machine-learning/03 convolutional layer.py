import tensorflow as tf

# Create a Sequential model and add the Conv2D layer to it
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=(28, 28, 3))
])

# Print the model summary
model.summary()
