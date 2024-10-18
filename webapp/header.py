import streamlit as st

def render_header():
    st.markdown("### Recirculating Photonic Integrated Circuits for Machine Learning  \n"
                "MSc Thesis, Mateusz Mazurkiewicz, 15-10-2024")

    st.image("assets/diagram_time_delay.png", caption="The circuit modelled using temporal coupled mode theory.")
