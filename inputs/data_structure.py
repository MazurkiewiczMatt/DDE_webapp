class SimulationInputs:
    def __init__(self, t_delay, omega_driving, omega_1, omega_2, kappa_w1_ratio, kappa_x1_ratio, kappa_w2_ratio, kappa_x2_ratio):
        self.t_delay = t_delay
        self.omega_1 = omega_1
        self.omega_2 = omega_2
        self.kappa_w1_ratio = kappa_w1_ratio
        self.kappa_x1_ratio = kappa_x1_ratio
        self.kappa_w2_ratio = kappa_w2_ratio
        self.kappa_x2_ratio = kappa_x2_ratio
        self.kappa_w1 = self.omega_1 * self.kappa_w1_ratio
        self.kappa_w2 = self.omega_2 * self.kappa_w2_ratio
        self.kappa_x1 = self.omega_1 * self.kappa_x1_ratio
        self.kappa_x2 = self.omega_2 * self.kappa_x2_ratio
        self.omega_driving = omega_driving
        self.references = None
