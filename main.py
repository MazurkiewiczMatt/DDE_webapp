import streamlit as st
from inputs import render_inputs
from solver import solve_dde
from plotter import plot_results

st.title("Photonic Circuit Simulation with Temporal Coupled Mode Theory")

# Render inputs and get parameters
t_delay, omega_1, omega_2, kappa_w1_ratio, kappa_x1_ratio, kappa_w2_ratio, kappa_x2_ratio = render_inputs()

# Perform the DDE solution when inputs are submitted
if st.button("Run Simulation"):
    tspan, A_solution = solve_dde(omega_1, kappa_w1_ratio * omega_1, kappa_x1_ratio * omega_1, t_delay)

    # Display the results
    st.pyplot(plot_results(tspan, A_solution, kappa_w1_ratio * omega_1))
