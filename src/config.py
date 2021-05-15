from os import getenv

LAMBDA = getenv('LAMBDA') or 2
MU = getenv('MU') or 1
NU = getenv('NU') or 0.5

CHANNELS = getenv('CHANNELS') or 5
STEPS = getenv('STEPS') or 10000
MAX_QUEUE_SIZE = getenv('MAX_QUEUE_SIZE') or 5
STEP_HEIGHT = 1/STEPS
