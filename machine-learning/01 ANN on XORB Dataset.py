import numpy as np


class NeuralNetwork:
    # specifies the input size, hidden layer size, and output size ( setting up network architecture )
    def __init__(self, input_size, hidden_size, output_size):
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size
        
        self.weights_input_hidden = np.random.rand(self.input_size, self.hidden_size)
        self.bias_hidden = np.zeros((1, self.hidden_size))
        
        self.weights_hidden_output = np.random.rand(self.hidden_size, self.output_size)
        self.bias_output = np.zeros((1, self.output_size))

    # sigmoid activation function  
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    
    # derivative of sigmoid activation function 
    def sigmoid_derivative(self, x):
        return x * (1 - x)

    # forward propagation
    def forward(self, x):
        self.hidden_input = np.dot(x, self.weights_input_hidden) + self.bias_hidden
        self.hidden_output = self.sigmoid(self.hidden_input)
        
        self.output = np.dot(self.hidden_output, self.weights_hidden_output) + self.bias_output
        return self.output
    
    # backward propagation
    def backward(self, x, y, learning_rate):
        error = y - self.output
        
        # calculate gradients
        delta_output = error
        delta_hidden = delta_output.dot(self.weights_hidden_output.T) * self.sigmoid_derivative(self.hidden_output)
        
        # update weights and biases
        self.weights_hidden_output += self.hidden_output.T.dot(delta_output) * learning_rate
        self.bias_output += np.sum(delta_output, axis=0, keepdims=True) * learning_rate
        self.weights_input_hidden += x.T.dot(delta_hidden) * learning_rate
        self.bias_hidden += np.sum(delta_hidden, axis=0, keepdims=True) * learning_rate

    # train the neural network    
    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            for i in range(len(X)):
                x = X[i]
                x = x.reshape(1, -1)
                target = y[i]
                
                # performing fwd / bwd pass
                output = self.forward(x)
                self.backward(x, target, learning_rate)
            
            if (epoch + 1) % 100 == 0:
                loss = np.mean(np.square(y - self.forward(X)))
                print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss:.4f}")
                
    def predict(self, X):
        # Make predictions on new data
        predictions = []
        for x in X:
            x = x.reshape(1, -1)
            prediction = self.forward(x)
            predictions.append(prediction)
        return np.array(predictions)

# Create a toy dataset (XOR problem)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

# creating and training the neural network
input_size = 2
hidden_size = 4
output_size = 1
learning_rate = 0.1
epochs = 1000

nn = NeuralNetwork(input_size, hidden_size, output_size)
nn.train(X, y, epochs, learning_rate)

predictions = nn.predict(X)
print("Predictions:")
print(predictions)
