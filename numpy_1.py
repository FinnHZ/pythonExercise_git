import numpy as np



commands = np.ndarray((4,), dtype=np.uint16)
commands[:] = 0
commands[1] = 1

print(commands, type(commands))