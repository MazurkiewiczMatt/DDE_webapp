import streamlit as st

col1, col2, col3 = st.columns(3)

with col1:
    cavities = st.radio(
        "The cavities are:",
        ["Identical", "Different"]
    )

with col2:
    omega_1 = st.number_input("$\omega_1$ [Hz]", value=1.0)

with col3:
    if cavities == "Different":
        omega_2 = st.number_input("$\omega_2$ [Hz]", value=1.0)
    else:
        omega_2 = st.number_input("$\omega_2$ [Hz]", value=omega_1)


# Selector for units
unit_choice = st.radio(
    "Express values in:",
    ["Multiples of 1/omega_1", "Multiples of 1/omega_2", "Absolute values"]
)

# Function to apply conversion based on unit choice
def convert_value(value, omega_1, omega_2, unit_choice):
    if unit_choice == "Multiples of 1/omega_1":
        return value * omega_1
    elif unit_choice == "Multiples of 1/omega_2":
        return value * omega_2
    else:
        return value

# Input parameters
t_delay = st.number_input("t_delay (time)", value=1.0)
kappa_w1 = st.number_input("kappa_w1 (frequency)", value=1.0)
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
