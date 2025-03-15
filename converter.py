import streamlit as st

# Set page title and configuration
st.title("Unit Converter")
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .stSelectbox {
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Create conversion categories
category = st.selectbox(
    "Select Conversion Category",
    ["Length", "Weight", "Temperature"]
)

# Create conversion logic
if category == "Length":
    input_unit = st.selectbox("From:", ["Meters", "Kilometers", "Miles", "Feet"])
    output_unit = st.selectbox("To:", ["Meters", "Kilometers", "Miles", "Feet"])
    
    value = st.number_input("Enter value:", value=0.0)
    
    # Conversion factors to meters
    length_factors = {
        "Meters": 1,
        "Kilometers": 1000,
        "Miles": 1609.34,
        "Feet": 0.3048
    }
    
    # Convert to meters first, then to target unit
    result = value * length_factors[input_unit] / length_factors[output_unit]
    
elif category == "Weight":
    input_unit = st.selectbox("From:", ["Kilograms", "Pounds", "Grams", "Ounces"])
    output_unit = st.selectbox("To:", ["Kilograms", "Pounds", "Grams", "Ounces"])
    
    value = st.number_input("Enter value:", value=0.0)
    
    # Conversion factors to kilograms
    weight_factors = {
        "Kilograms": 1,
        "Pounds": 0.453592,
        "Grams": 0.001,
        "Ounces": 0.0283495
    }
    
    # Convert to kilograms first, then to target unit
    result = value * weight_factors[input_unit] / weight_factors[output_unit]

else:  # Temperature
    input_unit = st.selectbox("From:", ["Celsius", "Fahrenheit", "Kelvin"])
    output_unit = st.selectbox("To:", ["Celsius", "Fahrenheit", "Kelvin"])
    
    value = st.number_input("Enter value:", value=0.0)
    
    # Temperature conversion functions
    def convert_temperature(value, from_unit, to_unit):
        # Convert to Celsius first
        if from_unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
        elif from_unit == "Kelvin":
            celsius = value - 273.15
        else:
            celsius = value
            
        # Convert from Celsius to target unit
        if to_unit == "Fahrenheit":
            return (celsius * 9/5) + 32
        elif to_unit == "Kelvin":
            return celsius + 273.15
        else:
            return celsius
            
    result = convert_temperature(value, input_unit, output_unit)

# Display result
st.write(f"Result: {result:.4f} {output_unit}")

st.markdown("<div style='text-align: center;'>Developed by  Rahib Siddiqui </div>", unsafe_allow_html=True)
