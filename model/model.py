import numpy as np

def F_func(t, omega_driving):
    if t >= 0:
        return np.exp(1j * t * omega_driving)
    else:
        return 0.0 + 0.0j

def history(t):
    return np.zeros(2, dtype=np.complex128)

def system_dynamics(inputs):
    def dAdt(A_t, t):
        A_0 = A_t(t)
        A_1 = A_t(t - inputs.t_delay)
        A_2 = A_t(t - 2 * inputs.t_delay)
        F_0 = F_func(t, inputs.omega_driving)
        F_1 = F_func(t - inputs.t_delay, inputs.omega_driving)
        F_2 = F_func(t - 2 * inputs.t_delay, inputs.omega_driving)

        dA1dt = (-1j * inputs.omega_1 - inputs.kappa_x1/2 - inputs.kappa_w1) * A_0[0] + np.sqrt(inputs.kappa_w1) * (F_0 - F_2 - np.sqrt(inputs.kappa_w1)*A_2[0] + np.sqrt(inputs.kappa_w2) * A_1[1])
        dA2dt = (-1j * inputs.omega_2 - inputs.kappa_x2/2 - inputs.kappa_w2/2) * A_0[1] + np.sqrt(inputs.kappa_w2)*(F_1 + np.sqrt(inputs.kappa_w1)*A_1[0])

        return np.array([dA1dt, dA2dt], dtype=np.complex128)
    return dAdt


def calculate_output_power(tspan, A_1, A_2, inputs):
    t_delay = inputs.t_delay
    sqrt_kappa_w1 = np.sqrt(inputs.kappa_w1)
    sqrt_kappa_w2 = np.sqrt(inputs.kappa_w2)

    def delayed(t, values, delay):
        delayed_time_idx = np.searchsorted(tspan, t - delay)
        if delayed_time_idx < 0:
            delayed_time_idx = 0
        return values[delayed_time_idx]

    output_power = np.array([
        -F_func(t - 2 * t_delay, inputs.omega_driving)
        + sqrt_kappa_w1 * delayed(t, A_1, 2 * t_delay)
        + sqrt_kappa_w2 * delayed(t, A_2, t_delay)
        - sqrt_kappa_w1 * A_1[idx]
        for idx, t in enumerate(tspan)
    ])

    return output_power
