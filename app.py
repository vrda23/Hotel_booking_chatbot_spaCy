# Import necessary libraries
import streamlit as st
import spacy
from datetime import datetime
import re
# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

# Function for extracting user name
def extract_name(text):
    """
    Extracts the first PERSON entity (name) from the given text.
    
    Args:
        text (str): The text to extract the name from.
    
    Returns:
        str: The extracted name, or None if no name is found.
    """
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

# Function for extracting start and end dates
#def extract_dates(text):
    """
    Extracts dates in YYYY-MM-DD format from the given text and sorts them.
    
    Args:
        text (str): The text to extract dates from.
    
    Returns:
        list: A list of two sorted datetime.datetime objects, or None if not found.
    """
    doc = nlp(text)
    dates = []
    for ent in doc.ents:
        if ent.label_ == "DATE":
            try:
                date = datetime.strptime(ent.text, "%Y-%m-%d")
                dates.append(date)
            except ValueError:
                pass
    if len(dates) == 2:
        return sorted(dates)
    return None

# Function for extracting start and end dates
def extract_dates(text):
    """
    Extracts dates in YYYY-MM-DD format from the given text and sorts them.
    
    Args:
        text (str): The text to extract dates from.
    
    Returns:
        list: A list of two sorted datetime.datetime objects, or None if not found.
    """
    # Regular expression pattern for YYYY-MM-DD dates
    pattern = r'\d{4}-\d{2}-\d{2}'
    
    # Find all matches in the input text
    matches = re.findall(pattern, text)
    
    dates = []
    for match in matches:
        try:
            date = datetime.strptime(match, "%Y-%m-%d")
            dates.append(date)
        except ValueError:
            pass
            
    if len(dates) == 2:
        return sorted(dates)
    return None






# Function for extracting the number of guests
def extract_number_of_guests(text):
    """
    Extracts the first numerical value from the given text.
    
    Args:
        text (str): The text to extract the number from.
    
    Returns:
        int: The extracted number, or None if no number is found.
    """
    doc = nlp(text)
    for token in doc:
        if token.pos_ == "NUM":
            return int(token.text)
    return None

# Define dictionary for booking info
booking_info = {}

# Streamlit app
def main():
    st.title("Hotel Booking Chatbot")
    
    name_input = st.text_input("What is your name?")
    name = extract_name(name_input)
    if name:
        st.success(f"Name: {name}")
        booking_info['name'] = name
    
    date_input = st.text_input("Please provide the check-in and check-out dates in YYYY-MM-DD format (e.g., 2023-04-20 and 2023-04-25):")
    dates = extract_dates(date_input)
    if dates:
        st.success(f"Dates: {dates[0].strftime('%Y-%m-%d')} to {dates[1].strftime('%Y-%m-%d')}")
        booking_info['dates'] = dates

    guests_input = st.text_input("How many guests will be staying?")
    guests = extract_number_of_guests(guests_input)
    if guests:
        st.success(f"Number of guests: {guests}")
        booking_info['guests'] = guests

    if st.button("Submit"):
        st.write("Booking information:")
        st.write(booking_info)

if __name__ == "__main__":
    main()
