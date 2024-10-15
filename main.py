import streamlit as st

st.markdown("### Recirculating Photonic Integrated Circuits for Machine Learning  \n"
            "MSc Thesis, Mateusz Mazurkiewicz, 15-10-2024")

st.image("diagram_time_delay.png", caption="The circuit modelled using temporal coupled mode theory.")


st.markdown("Cavities:")
with st.container(border=True):

    col1, col2, col3 = st.columns([1, 2, 2])

    with col1:
        cavities = st.radio(
            " ",
            ["$\omega_1 = \omega_2$", "$\omega_1 \\neq \omega_2$"],
            label_visibility="hidden"
        )

    with col2:
        with st.container(border=True):
            st.markdown("Cavity A")
            col21, col22 = st.columns(2)
            with col21:
                omega_1 = st.number_input("$\omega_1$ [Hz]", value=1.0, help="Natural frequency of the cavity.")
                kappa_w1_ratio = st.number_input("$\kappa_{w,1}/\omega_1$", value=0.1, help="$\kappa_{w}$ is coupling with waveguide.")
            with col22:
                kappa_x1_ratio = st.number_input("$\kappa_{x,1}/\omega_1$", value=0.0, help="$\kappa_{x}$ represents other cavity losses.")
                st.markdown("$\omega_{1} = " + f"{omega_1}" + "$ [Hz]  \n")
                st.markdown("$\kappa_{w,1} = " + f"{kappa_w1_ratio*omega_1}" + "$ [Hz]  \n")
                st.markdown("$\kappa_{x,1} = " + f"{kappa_x1_ratio * omega_1}" + "$ [Hz]")

    with col3:
        with st.container(border=True):
            st.markdown("Cavity B")
            col31, col32 = st.columns(2)
            with col31:
                if cavities == "$\omega_1 \\neq \omega_2$":
                    omega_2 = st.number_input("$\omega_2$ [Hz]", value=1.0, help="Natural frequency of the cavity.")
                else:
                    omega_2 = st.number_input("$\omega_2$ [Hz]", value=omega_1, disabled=True)
                kappa_w2_ratio = st.number_input("$\kappa_{w,2}/\omega_2$", value=0.1,
                                           help="$\kappa_{w}$ is coupling with waveguide.")
            with col32:
                kappa_x2_ratio = st.number_input("$\kappa_{x,2}/\omega_2$", value=0.0,
                                       help="$\kappa_{x}$ represents other cavity losses.")
                st.markdown("$\omega_{2} = " + f"{omega_2}" + "$ [Hz]  \n")
                st.markdown("$\kappa_{w,2} = " + f"{kappa_w1_ratio*omega_2}" + "$ [Hz]  \n")
                st.markdown("$\kappa_{x,2} = " + f"{kappa_x1_ratio * omega_2}" + "$ [Hz]")




# Input parameters
t_delay = st.number_input("t_delay (time)", value=1.0)

kappa_w2 = st.number_input("kappa_w2 (frequency)", value=1.0)
omega_driving = st.number_input("omega_driving (frequency)", value=1.0)
kappa_x_1 = st.number_input("kappa_x_1 (frequency)", value=1.0)
kappa_x_2 = st.number_input("kappa_x_2 (frequency)", value=1.0)

# Convert and display the parameters based on unit choice
t_delay = convert_value(t_delay, omega_1, omega_2, unit_choice)
kappa_w1 = convert_value(kappa_w1, omega_1, omega_2, unit_choice)
kappa_w2 = convert_value(kappa_w2, omega_1, omega_2, unit_choice)
omega_driving = convert_value(omega_driving, omega_1, omega_2, unit_choice)
kappa_x_1 = convert_value(kappa_x_1, omega_1, omega_2, unit_choice)
kappa_x_2 = convert_value(kappa_x_2, omega_1, omega_2, unit_choice)

# Display the results
st.write(f"t_delay: {t_delay}")
st.write(f"kappa_w1: {kappa_w1}")
st.write(f"kappa_w2: {kappa_w2}")
st.write(f"omega_driving: {omega_driving}")
st.write(f"kappa_x_1: {kappa_x_1}")
st.write(f"kappa_x_2: {kappa_x_2}")
