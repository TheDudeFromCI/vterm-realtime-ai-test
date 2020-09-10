from random import randrange
from typing import List, Tuple

class NeuralNetwork:
	def __init__(self, layers: List[int]):
		self.layers: List[List[Neuron]] = []

		for i in range(1, len(layers)):
			layer: List[Neuron] = []
			self.layers.append(layer)

			for x in range(layers[i]):
				layer.append(Neuron(layers[i - 1]))

	def forward_propagate(self, row: List[float]) -> List[float]:
		inputs = row
		for layer in self.layers:
			new_inputs = []
			for neuron in layer:
				neuron.activate(inputs)
				new_inputs.append(neuron.output)
			inputs = new_inputs

		return inputs

	def back_propagate(self, expected: List[float]):
		for i in reversed(range(len(self.layers))):
			layer = self.layers[i]
			errors = list()

			if i != len(self.layers) - 1:
				for j in range(len(layer)):
					error = 0.0
					for neuron in self.layers[i + 1]:
						error += (neuron.weights[j] * neuron.delta)
					errors.append(error)
			else:
				for j in range(len(layer)):
					neuron = layer[j]
					errors.append(expected[j] - neuron.output)

			for j in range(len(layer)):
				neuron = layer[j]

				if neuron.output >= 0:
					neuron.delta = errors[j]
				else:
					neuron.delta = 0.0

	def update_weights(self, row: List[float], learningRate: float):
		for i in range(len(self.layers)):
			inputs = row[:-1]
			if i != 0:
				inputs = [neuron.output for neuron in self.layers[i - 1]]

			for neuron in self.layers[i]:
				for j in range(len(inputs)):
					neuron.weights[j] += learningRate * neuron.delta * inputs[j]
				neuron.weights[-1] += learningRate * neuron.delta

	def train(self, train: List[Tuple[List[float], List[float]]], learningRate:float, epochs: int):
		for epoch in range(epochs):
			sum_error = 0
			for sample in train:
				outputs = self.forward_propagate(sample[0])
				expected = [sample[1][i] for i in range(len(sample[1]))]
				sum_error += sum([(expected[i] - outputs[i]) ** 2 for i in range(len(outputs))])
				self.back_propagate(expected)
				self.update_weights(sample[0], learningRate)
			print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, learningRate, sum_error))

class Neuron:
	def __init__(self, inputs: int):
		self.weights: List[float] = []
		self.output = 0.0
		self.delta = 0.0

		for i in range(inputs + 1):
			self.weights.append(randrange(-1.0, 1.0))

	def activate(self, inputs: List[float]):
		value: float = self.weights[-1]
		for x in range(len(inputs)):
			value += self.weights[x] * inputs[x]

		self.output = max(0.0, value)


dataset = [
	([0.2, 0.3], [0.5]),
	([0.1, 0.1], [0.2]),
	([0.6, 0.1], [0.7]),
	([0.25, 0.35], [0.6]),
	([0.5, 0.5], [1.0]),
]

network = NeuralNetwork([2, 1, 1, 2, 1])
network.train(dataset, 0.2, 20)
