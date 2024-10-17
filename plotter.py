import matplotlib.pyplot as plt

def plot_results(tspan, A_solution, kappa_w):
    A_1 = np.abs(A_solution[:, 0])**2
    A_2 = np.abs(A_solution[:, 1])**2

    plt.figure(figsize=(12, 6))
    plt.plot(tspan * kappa_w, A_1, label='A_1 energy')
    plt.plot(tspan * kappa_w, A_2, label='A_2 energy')
    plt.xlabel('Time t')
    plt.ylabel('Energy')
    plt.legend(loc="right")
    plt.grid(True)
    plt.show()
