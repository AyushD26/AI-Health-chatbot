import os
import google.generativeai as genai
import datetime

# Set up Google Gemini API Key
genai.configure(api_key="AIzaSyDYa0sPJajfq5XhcxOPJjpAQEryomXQ0OA")

# Function to log chat history
def log_conversation(user_input, bot_response):
    with open("chat_log.txt", "a", encoding="utf-8") as log_file:
        timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
        log_file.write(f"{timestamp} User: {user_input}\n")
        log_file.write(f"{timestamp} Bot: {bot_response}\n\n")

# Function to generate AI responses using Gemini
def generate_ai_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Function to handle medical symptoms
def generate_response(prompt):
    prompt_lower = prompt.lower()

    if "headache" in prompt_lower:
        response = "It seems like you have a headache. Try drinking water, resting, or using a cold compress."
    elif "fever" in prompt_lower:
        response = "If you have a fever, stay hydrated and take rest. If it's high, consider taking medicine like paracetamol."
    elif "stomach ache" in prompt_lower:
        response = "For a stomach ache, try drinking warm water, avoiding heavy foods, and resting. If pain persists, consult a doctor."
    elif "cough" in prompt_lower:
        response = "For a cough, drink warm liquids, use honey, and rest. If it's persistent, consult a doctor."
    elif "chest pain" in prompt_lower:
        response = "Chest pain can be serious. If it's severe or accompanied by dizziness or breathlessness, seek medical help immediately."
    elif "back pain" in prompt_lower:
        response = "For back pain, try stretching, applying heat/cold packs, and maintaining good posture."
    elif "dizziness" in prompt_lower:
        response = "Dizziness can be due to dehydration or low blood sugar. Sit down, drink water, and take deep breaths."
    elif "shortness of breath" in prompt_lower:
        response = "Shortness of breath can be serious. If severe, seek medical attention immediately."
    else:
        response = generate_ai_response(prompt)  # Call Gemini for AI-generated response

    log_conversation(prompt, response)  # Save chat to log
    return response

# Chatbot interaction loop
print("Chatbot is ready! Type 'exit' or 'quit' to stop.")

while True:
    user_input = input("How are you feeling today? ")

    if user_input.lower() in ["exit", "quit"]:
        print("Thanks for chatting! Have a great day! 😊")
        break

    response = generate_response(user_input)
    print("Bot:", response)

    print("Thanks for sharing!")
