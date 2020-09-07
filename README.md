# Virtual Terminal Real-time AGI Test

**This is a learning experience project for me. Nothin in here should be taken seriously, lol**

This project is a personal experiment around the development and application of a natural learning, real time agent that lives entirely within a virtual terminal.

The goal of this project is to experiment with the application of an AGI through the process of abstracting most of the lower level processes out of the neural network to allow the agent to only focus on higher-level concepts. This should hopefully improve the training time as well as make it much easier to control. This process works by allowing the agent to exist inside a terminal where it has the option to execute commands and save variables. Commands can either preform actions or execute queries that the agent can use in any way it desires. Additional functionality can be given to the agent by simply creating more commands. By allowing lower level actions to be abstracted away by the use of commands, the agent is free to learn how to utilitize these commands to work with instead of needing to learn how to do everything itself.

By allowing actions such as database queries, in theory, the agent should be capable of learning how to utilitze reading/writing to a "long term memory" or so.

### Tech Notes

The AI is probably going to be implemented using a Spike Neural Network as it seems more practical for this task. Since the goal is ultimately real-time, (meaning the agent is constantly running, not just an input-output function) having a mental state which mimics this sounds useful.

It'll also be using reinforcement learning as well, but that's probably a given, noting that we're using an SNN.

Lastly, I was to try and look into using a continous reward input, if that's possible. Something close to "here's your current reward value" instead of a quick reward impulse.
