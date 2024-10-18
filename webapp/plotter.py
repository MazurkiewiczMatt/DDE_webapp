import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def render_results(solution):
    A_1 = np.abs(solution[1][:, 0])**2
    A_2 = np.abs(solution[1][:, 1])**2

    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(solution[0], A_1, label='A_1 energy')
    ax.plot(solution[0], A_2, label='A_2 energy')
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Energy')
    ax.legend(loc="right")
    ax.grid(True)
    st.pyplot(fig)