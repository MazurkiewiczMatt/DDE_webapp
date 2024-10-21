import streamlit as st
from webapp import render_header, render_inputs, render_results
from model import solve_dde
from inputs import SimulationInputs

render_header()

inputs_values = render_inputs()
inputs = SimulationInputs(*inputs_values)

if st.button("Run Simulation"):
    solution = solve_dde(inputs, references=inputs.references)
    render_results(solution)
