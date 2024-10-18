import streamlit as st

def render_inputs():

    with st.expander("Simulation settings", expanded=False):
        st.markdown("Waveguides:")
        t_delay = st.number_input("$t_{\\text{delay}}$ [s]", value=1.0)

        st.markdown("Cavities:")
        cavities = st.radio(
            " ",
            ["$\omega_1 = \omega_2$", "$\omega_1 \\neq \omega_2$"],
            label_visibility="hidden"
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

    return t_delay, omega_1, omega_2, kappa_w1_ratio, kappa_x1_ratio, kappa_w2_ratio, kappa_x2_ratio
