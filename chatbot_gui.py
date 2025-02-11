import os
import google.generativeai as genai
import datetime
import tkinter as tk
from tkinter import scrolledtext

# Set up Google Gemini API Key
genai.configure(api_key="YOUR_GOOGLE_API_KEY")  # Replace with your actual API Key

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

# Function to handle sending messages
def send_message():
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    
    chat_window.insert(tk.END, f"You: {user_input}\n", "user")
    response = generate_response(user_input)
    chat_window.insert(tk.END, f"Bot: {response}\n\n", "bot")

    user_entry.delete(0, tk.END)  # Clear input field

# Creating the GUI window
root = tk.Tk()
root.title("Health Chatbot - AI Assistant")
root.geometry("500x600")
root.resizable(False, False)

# Chat history display
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=25)
chat_window.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
chat_window.tag_configure("user", foreground="blue", font=("Arial", 12, "bold"))
chat_window.tag_configure("bot", foreground="green", font=("Arial", 12))

# User input field
user_entry = tk.Entry(root, width=40, font=("Arial", 14))
user_entry.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Send button
send_button = tk.Button(root, text="Send", command=send_message, font=("Arial", 12), bg="blue", fg="white")
send_button.grid(row=1, column=1, padx=10, pady=10, sticky="e")

# Run the chatbot GUI
root.mainloop()
