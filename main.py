import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.01, epochs=1000):
        self.weights = np.zeros(input_size + 1)  # +1 for the bias term
        self.learning_rate = learning_rate
        self.epochs = epochs

    def predict(self, x):
        x_with_bias = np.insert(x, 0, 1)  # Insert bias term at the beginning
        weighted_sum = np.dot(x_with_bias, self.weights)
        return 1 if weighted_sum >= 0 else 0

    def train(self, X, y):
        for epoch in range(self.epochs):
            for xi, target in zip(X, y):
                prediction = self.predict(xi)
                self.weights += self.learning_rate * (target - prediction) * np.insert(xi, 0, 1)

# Sample usage
if __name__ == "__main__":
    # Input data (XOR problem)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 0, 0, 1])  # AND logic

    # Initialize perceptron
    perceptron = Perceptron(input_size=2)

    # Train perceptron
    perceptron.train(X, y)

    # Test perceptron
    for xi in X:
        print(f"Input: {xi} -> Predicted: {perceptron.predict(xi)}")
