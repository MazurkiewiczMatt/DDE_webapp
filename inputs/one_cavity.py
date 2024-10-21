from .data_structure import SimulationInputs

class OneCavityInputs(SimulationInputs):
    def __init__(self, omega_driving):
        t_delay = 3
        omega_1 = 10.0
        omega_2 = 10.0
        kappa_w1_ratio = 0.1
        kappa_x1_ratio = 0.0
        kappa_w2_ratio = 0
        kappa_x2_ratio = 0.0
        omega_driving = omega_driving

        super().__init__(self, t_delay, omega_driving, omega_1, omega_2, kappa_w1_ratio, kappa_x1_ratio, kappa_w2_ratio,
                     kappa_x2_ratio)
        self.references = None