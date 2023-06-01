# Importing libraries
import spacy
import re
from datetime import datetime

# loading a pre-trained statistical model for processing English text using the spaCy library
nlp = spacy.load("en_core_web_sm")

# NLP functions
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
def extract_dates(text):
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


def extract_number_of_guests(text):
    # Check if the input is a single number
    if text.isdigit():
        return int(text)
    doc = nlp(text)
    for token in doc:
        if token.pos_ == "NUM":
            return int(token.text)
    return None

# Chatbot questions
questions = [
    {
        "question": "What is your name?",
        "processor": extract_name,
        "key": "name"
    },
    {
        "question": "Please provide the check-in and check-out dates in YYYY-MM-DD format (e.g., 2023-04-20 and 2023-04-25):",
        "processor": extract_dates,
        "key": "dates"
    },
    {
        "question": "How many guests will be staying?",
        "processor": extract_number_of_guests,
        "key": "guests"
    },
]

# Booking information
booking_info = {}

# Main loop
for question_data in questions:
    while True:
        user_input = input(question_data["question"])
        answer = question_data["processor"](user_input)
        if answer:
            booking_info[question_data["key"]] = answer
            break
        else:
            print("Invalid input, please try again.")

# Save or display booking information
print(booking_info)

