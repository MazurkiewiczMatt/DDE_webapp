import numpy as np
from ddeint import ddeint
from model.model import system_dynamics, history

def solve_dde(inputs):
    tspan = np.linspace(0, 10, 1000)
    solution = ddeint(system_dynamics(inputs), history, tspan)
    return (tspan, solution)
