import streamlit as st
import math_operations as dick

st.title("Simple Calculator")

x = st.number_input("Enter the first number:")
y = st.number_input("Enter the second number:")

operation = st.selectbox("Select an operation",
                         ("Add", "Subtract", "Multiply", "Divide"))

result = None

if st.button("Calculate"):
    if operation == "Add":
        result = dick.add(x, y)
    elif operation == "Subtract":
        result = dick.subtract(x, y)
    elif operation == "Multiply":
        result = dick.multiply(x, y)
    elif operation == "Divide":
        try:
            result = dick.divide(x, y)
        except ZeroDivisionError:
            st.error("Division by zero is not allowed.")

if result is not None:
    st.success(f"Result: {result}")