import streamlit as st

# Main page
st.title("Air Crash Severity Prediction App")

# Button to open Air Crash Details page
if st.button("Air Crash Details"):
    st.markdown("## Air Crash Details Page")
    st.write("This is the Air Crash Details page content.")
