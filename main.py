import streamlit as st
import matplotlib.pyplot as plt

# Create six sliders and store their values
slider1 = st.slider('Slider 1', 0, 100, 50)
slider2 = st.slider('Slider 2', 0, 100, 50)
slider3 = st.slider('Slider 3', 0, 100, 50)
slider4 = st.slider('Slider 4', 0, 100, 50)
slider5 = st.slider('Slider 5', 0, 100, 50)
slider6 = st.slider('Slider 6', 0, 100, 50)

# Store the slider values in a list
slider_values = [slider1, slider2, slider3, slider4, slider5, slider6]

# Labels for the sliders
slider_labels = ['Slider 1', 'Slider 2', 'Slider 3', 'Slider 4', 'Slider 5', 'Slider 6']

# Create a bar chart using matplotlib
fig, ax = plt.subplots()
ax.bar(slider_labels, slider_values)

# Set the chart title and labels
ax.set_title('Slider Values')
ax.set_ylabel('Value')

# Display the chart in Streamlit
st.pyplot(fig)
