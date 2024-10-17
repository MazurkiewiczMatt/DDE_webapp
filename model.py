import numpy as np

def F_func(t, omega_driving):
    if t >= 0:
        return np.exp(1j * t * omega_driving)
    else:
        return 0.0 + 0.0j

def history(t):
    return np.zeros(2, dtype=np.complex128)

def dAdt(A_t, t, omega, kappa_x, kappa_w, t_delay):
    A_0 = A_t(t)
    A_1 = A_t(t - t_delay)
    A_2 = A_t(t - 2 * t_delay)
    F_0 = F_func(t, omega + 0.05 * kappa_w)
    F_1 = F_func(t - t_delay, omega + 0.05 * kappa_w)
    F_2 = F_func(t - 2 * t_delay, omega + 0.05 * kappa_w)

    dA1dt = (-1j * omega - kappa_x/2 - kappa_w) * A_0[0] + kappa_w * A_2[0] + kappa_w * A_1[1] + np.sqrt(kappa_w) * F_0 - np.sqrt(kappa_w) * F_2
    dA2dt = -1 * kappa_w * A_1[0] + (-1j * omega - kappa_x/2 - kappa_w/2) * A_0[1] + np.sqrt(kappa_w) * F_1

    return np.array([dA1dt, dA2dt], dtype=np.complex128)
