from typing import List
from random import randrange, randint
import math

MIN_CONNECTIONS = 2
MAX_CONNECTIONS = 8
ALLOW_NEGATIVE_WEIGHTS = True
STIMULATION_FALLOFF = 0.9

class SpikedNeuralNetwork:
    def __init__(self, inputCount: int, hiddenCount: int, outputCount: int):

        def initNeurons(count: int) -> List[Neuron]:
            list = []
            for x in range(count): list.append(Neuron())
            return list

        def connectToRandom(n: Neuron, category: List[Neuron]):
            n.connectTo(category[randint(0, len(category) - 1)])

        self.inputs = initNeurons(inputCount)
        self.hidden = initNeurons(hiddenCount)
        self.outputs = initNeurons(outputCount)

        for n in self.inputs:
            for x in range(randint(MIN_CONNECTIONS, MAX_CONNECTIONS)):
                connectToRandom(n, self.hidden)

        for n in self.hidden:
            for x in range(randint(MIN_CONNECTIONS, MAX_CONNECTIONS)):
                connectToRandom(n, self.hidden)

        for n in self.outputs:
            for x in range(randint(MIN_CONNECTIONS, MAX_CONNECTIONS)):
                self.hidden[randint(0, hiddenCount - 1)].connectTo(n)
    
    def setInput(self, index: int, value: float):
        self.inputs[index].stimulation = value

    def getOutput(self, index: int) -> bool:
        return self.outputs[index].stimulation >= self.outputs[index].activation

    def step(self):
        toActivate: List[[Neuron, float]] = []

        for n in self.inputs + self.hidden:
            if n.needsActivation():
                toActivate.append([n, n.stimulation])
            else:
                n.drain()

        for n in toActivate:
            n[0].activate(n[1])

class Neuron:
    def __init__(self):
        self.stimulation = 0.0
        self.activation = randrange(0.5, 1.5)
        self.connections: List[Connection] = []

    def connectTo(self, target: Neuron):
        if target == self:
            return

        for con in self.connections:
            if con.target == target:
                return

        minValue = -1.0 if ALLOW_NEGATIVE_WEIGHTS else 0.0
        self.connections.append(Connection(target, randrange(minValue, 1.0)))

    def needsActivation(self) -> float:
        return self.stimulation >= self.activation and len(self.connections) > 0

    def activate(self, energy: float):
        self.stimulation -= energy
        energy = energy / len(self.connections)

        for c in self.connections:
            c.push(energy)

    def stimulate(self, value: float):
        self.stimulation = math.max(0.0, self.stimulation + value)

    def drain(self):
        self.stimulation *= STIMULATION_FALLOFF

class Connection:
    def __init__(self, target: Neuron, weight: float):
        self.target = target
        self.weight = weight

    def push(self, energy: float):
        self.target.stimulate(energy * self.weight)
