import streamlit as st
import debugpy

#debugpy.listen(("localhost", 5679))  # Changed port to 5679
#print("Waiting for debugger attach...")
#debugpy.wait_for_client()

def main():
    st.title("Hello World!")
    
    # Top half with full width
    st.write("This is a Streamlit app!", key="top_half")
    
    # Bottom half with two columns
    col1, col2 = st.columns([0.35, 0.65])
    
    with col1:
        st.write("Bottom Left", key="bottom_left")
        
        # Dropdown
        options = ["Option 1", "Option 2", "Option 3"]
        selected_option = st.selectbox("Select an option", options)
        
        # Expandable placeholder
        with st.expander("Expandable Placeholder"):
            for i in range(1, 6):
                checkbox_col, input_col = st.columns([0.1,0.9])
                with checkbox_col:
                    st.checkbox("", key=f"checkbox_{i}")
                with input_col:
                    st.text_input(f"Input {i}", key=f"text_input_{i}")
    
    with col2:
        st.write("Bottom Right", key="bottom_right")

if __name__ == "__main__":
    main()