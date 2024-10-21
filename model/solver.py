import numpy as np
from ddeint import ddeint
from model.model import system_dynamics, history, F_func, calculate_output_power

def solve_dde(inputs, references=None):
    tspan = np.linspace(0, 10, 1000)
    A_solution = ddeint(system_dynamics(inputs), history, tspan)
    input_power = np.array([F_func(t, inputs.omega_driving) for t in tspan])
    A_1 = np.abs(A_solution[:, 0]) ** 2
    A_2 = np.abs(A_solution[:, 1]) ** 2
    output_power = calculate_output_power(tspan, A_1, A_2, inputs)
    return (tspan, A_solution, input_power, output_power, references)
