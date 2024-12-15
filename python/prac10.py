import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        self.weights = np.zeros(input_size + 1)  # +1 for bias
        self.learning_rate = learning_rate
        self.epochs = epochs

    def activation(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        z = np.dot(x, self.weights[1:]) + self.weights[0]
        return self.activation(z)

    def train(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                output = self.predict(xi)
                error = target - output
                self.weights[1:] += self.learning_rate * error * xi
                self.weights[0] += self.learning_rate * error

# Example usage
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([0, 0, 0, 1])  # AND Gate
model = Perceptron(input_size=2)
model.train(X, y)

print("Trained weights:", model.weights)
for xi in X:
    print(f"Input: {xi}, Prediction: {model.predict(xi)}")
