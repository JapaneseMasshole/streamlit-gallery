import streamlit as st
import debugpy
import pandas as pd
import numpy as np

# debugpy.listen(("localhost", 5679))  # Changed port to 5679
# print("Waiting for debugger attach...")
# debugpy.wait_for_client()

# Set the page layout to wide and use the full screen
st.set_page_config(layout="wide", initial_sidebar_state="collapsed")

def main():
    st.title("Hello World!")
    
    # Use columns for the entire layout
    col1, col2 = st.columns([0.4, 0.6])
    
    with col1:
        st.header("This is a Streamlit app!")
        st.write("This is the left column content.", key="left_column")
        
        # Dropdown
        options = ["Option 1", "Option 2", "Option 3"]
        selected_option = st.selectbox("Select an option", options)
        
        # Create a dummy dataframe
        df = pd.DataFrame(
            np.random.randn(5, 3),
            columns=('Column 1', 'Column 2', 'Column 3')
        )

        # Display the dataframe
        

        # Expandable placeholder
        with st.expander("Expandable Placeholder"):
            # Add the existing input fields
            for i in range(1, 6):
                checkbox_col, label_col, input_col = st.columns([0.1, 0.2, 0.7])
                with checkbox_col:
                    st.checkbox("", key=f"checkbox_{i}")
                with label_col:
                    st.write(f"Input {i}")
                with input_col:
                    st.text_input("", key=f"text_input_{i}")
        
        st.dataframe(df)
    with col2:
        st.header("Another Header")
        st.write("This is the right column content.", key="right_column")
        # Add more content or widgets here

if __name__ == "__main__":
    main()