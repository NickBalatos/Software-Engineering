from st_pages import show_pages_from_config, add_page_title
import streamlit as st
import pandas as pd
import time
# Either this or add_indentation() MUST be called on each page in your
# app to add indendation in the sidebar
add_page_title()
show_pages_from_config()

#Loading data from the CSV or Excel file
def load_data(file_path):
    data = pd.read_csv(file_path)  
    data = pd.read_excel(file_path)
    return data

def main():
    st.session_state.data = None
    #Home Tab
    st.title("Αρχική Σελίδα")
    st.write("Καλώς ορίσατε στην Εφαρμογή Μηχανικής Μάθησης & 2D Visualization της ομάδας Brigade-01. Προσθέστε ένα αρχείο CSV ή Excel παρακάτω για να ξεκινήσετε την επεξεργασία του μέσω της εφαρμογής μας.")
    st.markdown("""---""")

    # File uploading module
    uploaded_file = st.file_uploader("Φόρτωση αρχείου CSV ή Excel", type=["csv", "xlsx"])
    
    if uploaded_file is not None:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            data = pd.read_excel(uploaded_file)
        else:
            st.error("Τύπος αρχείου μη υποστηριζόμενος.")
            return
        
        # Check if the uploaded file contains letters
        if data.select_dtypes(include=['object']).empty:
            success_message = st.success("Τα δεδομένα φορτώθηκαν με επιτυχία!")
            st.markdown("""---""")
            st.write("Τα φορτωμένα δεδομένα:")
            st.write(data)
        else:
            st.error("Το αρχείο δεδομένων περιέχει γράμματα. Φορτώστε ένα αρχείο που περιέχει μόνο αριθμητικές τιμές.")
            st.markdown("""---""")
            st.write("Τα φορτωμένα δεδομένα:")
            st.write(data)
        st.markdown("""---""")

        # Saving uploaded data for usage on the rest of the tabs
        st.session_state.data = data
if __name__ == "__main__":
    main()