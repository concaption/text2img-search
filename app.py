#!/usr/bin/env python
"""
Streamlit app for multimodal search
"""
# The Streamlit app for the multimodal search
# Importing necessary modules and the MultiModalSearch class
import streamlit as st
from  multimodal_search import MultiModalSearch

# Setting the page layout to "wide"
st.set_page_config(
    layout="wide"
)

# Main function to run the app
def main():
    """
    Main function to run the app
    """
    # Title of the app
    st.markdown("<h1 style='text-align: center; color: green;'>Fashion Cloth Search App</h1>", unsafe_allow_html=True)

    # Initialize the MultiModalSearch class
    multimodal_search = MultiModalSearch()

    # Text input for user query
    query = st.text_input("Enter your query:")
    # Search button
    if st.button("Search"):
        # Check if the query is not empty
        if len(query) > 0:
            # Perform the search
            results = multimodal_search.search(query)
            # Display the query
            st.warning("Your query was "+query)
            # Display the search results
            st.subheader("Search Results:")
            col1, col2, col3 = st.columns([1,1,1])
            # First result
            with col1:
                st.write(f"Score: {round(results[0].score*100, 2)}%")
                st.image(results[0].content, use_column_width=True)
            # Second result
            with col2:
                st.write(f"Score: {round(results[1].score*100, 2)}%")
                st.image(results[1].content, use_column_width=True)
            # Third result
            with col3:
                st.write(f"Score: {round(results[2].score*100, 2)}%")
                st.image(results[2].content, use_column_width=True)
        else:
            # Warning for empty query
            st.warning("Please enter a query.")

# Run the app
if __name__ == "__main__":
    main()
