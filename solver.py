import numpy as np
from ddeint import ddeint
from model import dAdt, history

def solve_dde(omega, kappa_w, kappa_x, t_delay):
    # Time points where the solution is computed
    tspan = np.linspace(0, 100 / kappa_w, 1000)

    # Solve the DDE
    solution = ddeint(dAdt, history, tspan, fargs=(omega, kappa_x, kappa_w, t_delay))
    return tspan, solution
