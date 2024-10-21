import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


def render_results(solution):
    A_1 = np.abs(solution[1][:, 0]) ** 2
    A_2 = np.abs(solution[1][:, 1]) ** 2
    input_power = np.abs(solution[2]) ** 2
    output_power = np.abs(solution[3]) ** 2
    references = solution[4]

    fig, ax = plt.subplots(figsize=(12, 6))

    ax.plot(solution[0], A_1, label='A_1 energy', color='cyan', linewidth=2.5)
    ax.plot(solution[0], A_2, label='A_2 energy', color='magenta', linewidth=2.5)
    ax.plot(solution[0], input_power, label='Input power', color='lightblue', linewidth=2.5)
    ax.plot(solution[0], output_power, label='Output power', color='orange', linewidth=2.5)
    if references is not None:
        for ref in references:
            ax.plot(ref[0], ref[1], label='Reference', color='red', linewidth=6, linestyle=':')

    ax.set_xlabel('Time [s]', color='white', fontsize=16)
    ax.set_ylabel('Energy', color='white', fontsize=16)

    ax.tick_params(colors='white', labelsize=14)
    ax.legend(loc="right", facecolor='black', edgecolor='white', labelcolor='white', fontsize=14)
    ax.grid(True, color='white', linestyle='--', linewidth=0.7)

    fig.patch.set_alpha(0)
    ax.set_facecolor('none')
    ax.spines['top'].set_color('white')
    ax.spines['bottom'].set_color('white')
    ax.spines['left'].set_color('white')
    ax.spines['right'].set_color('white')
    ax.spines['top'].set_linewidth(1.5)
    ax.spines['bottom'].set_linewidth(1.5)
    ax.spines['left'].set_linewidth(1.5)
    ax.spines['right'].set_linewidth(1.5)

    st.pyplot(fig)
