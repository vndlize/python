import tensorflow as tf

# Create a Sequential model
model = tf.keras.Sequential()

# Add a Conv2D layer (just for illustration)
model.add(tf.keras.layers.Conv2D(filters=32, kernel_size=(3, 3), padding='valid', activation='relu', input_shape=(28, 28, 3)))

# Add a Max Pooling Layer
model.add(tf.keras.layers.MaxPooling2D(pool_size=(2, 2)))

# Add an Average Pooling Layer
model.add(tf.keras.layers.AveragePooling2D(pool_size=(2, 2)))

# Print model summary to see the layers
model.summary()
