import streamlit as st
import math
import statistics

st.set_page_config(page_title="StatCheck Pro", page_icon="📊")

st.title("📊 StatCheck Pro")
st.write("Enter your numbers separated by spaces to get instant statistics.")

user_input = st.text_input("Dataset:", placeholder="e.g., 2 4 4 4 5 5 7 9")

if st.button("Calculate"):
    try:
        data = [float(x) for x in user_input.split()]
        if len(data) < 3:
            st.error("Please enter at least 3 numbers.")
        else:
            # إعادة استخدام المنطق اللي في project.py
            mean_val = statistics.mean(data)
            st.metric("Mean", round(mean_val, 4))
            st.metric("Median", round(statistics.median(data), 4))
            st.metric("Std Deviation", round(statistics.stdev(data), 4))
            st.write("Skewness:", round((sum((x - mean_val) ** 3 for x in data) / len(data)) / (statistics.stdev(data) ** 3), 4))
            st.success("Calculations complete!")
    except:
        st.error("Invalid input. Please enter numbers only.")