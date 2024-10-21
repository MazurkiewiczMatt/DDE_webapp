from email.policy import default

import streamlit as st

def render_inputs():

    with st.expander("Simulation settings", expanded=False):
        st.markdown("Waveguides:")
        t_delay = st.number_input("$t_{\\text{delay}}$ [s]", value=1.0)

        cavities = st.radio(
            "Cavities:",
            ["$\omega_1 = \omega_2$", "$\omega_1 \\neq \omega_2$"]
        )

        col2, col3 = st.columns([2, 2])

        with col2:
            st.markdown("Cavity A")
            omega_1 = st.number_input("$\omega_1$ [Hz]", value=1.0)
            kappa_w1_ratio = st.number_input("$\kappa_{w,1}/\omega_1$", value=0.1)
            kappa_x1_ratio = st.number_input("$\kappa_{x,1}/\omega_1$", value=0.0)

        with col3:
            st.markdown("Cavity B")
            omega_2 = st.number_input("$\omega_2$ [Hz]", value=1.0 if cavities == "$\omega_1 \\neq \omega_2$" else omega_1, disabled=(cavities != "$\omega_1 \\neq \omega_2$"))
            kappa_w2_ratio = st.number_input("$\kappa_{w,2}/\omega_2$", value=0.1)
            kappa_x2_ratio = st.number_input("$\kappa_{x,2}/\omega_2$", value=0.0)

        source_type = st.radio("Delievered power", ["Expressed as detuning", "Expressed in absolute terms"])
        if source_type == "Expressed as detuning":
            detuning = st.number_input("$(\\omega_{\\text{source}} - \omega_1) / \kappa_{w,1} $", value=0.0,
                                       help="Scaled detuning of the power delivered to the circuit relative to the first cavity.")
            omega_driving = detuning * kappa_w1_ratio + omega_1
        elif source_type == "Expressed in absolute terms":
            omega_driving = st.number_input("$\\omega_{\\text{source}}$ [Hz]", value=omega_1,
                                       help="Frequency of the power delivered to the circuit.")


    return t_delay, omega_driving, omega_1, omega_2, kappa_w1_ratio, kappa_x1_ratio, kappa_w2_ratio, kappa_x2_ratio
