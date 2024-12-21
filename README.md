Novida Chatbot
Project Description
Novida is an interactive chatbot built using Python's Tkinter for the graphical user interface (GUI) and pyttsx3 for text-to-speech (TTS) capabilities. The bot can respond to various user queries, including predefined responses and Wikipedia summaries. The project is intended for educational purposes and can serve as a base for more advanced chatbot development.

Features
Interactive Chatbot: Responds to various user queries like greetings, asking about its name, and more.
Text-to-Speech: The chatbot speaks its responses using pyttsx3.
Clear Button: Clears the chat history in the chatbox.
GUI: A simple and user-friendly graphical interface created with Tkinter.
Predefined Responses: Custom responses for various input patterns such as "hi", "how are you", "goodbye", etc.
Requirements
Before running this project, make sure to install the following Python libraries:

pyttsx3: For text-to-speech functionality.
wikipedia: To fetch information from Wikipedia (optional, if you want to add Wikipedia functionality).
Tkinter: Built-in with Python for GUI.
You can install the required libraries using the following commands:

bash
Copy code
pip install pyttsx3 wikipedia
Python version
This project is built with Python 3.x.

How to Run the Application
Clone the repository or download the code.
Make sure you have the required libraries installed (pyttsx3, wikipedia, and tkinter).
Run the novida_chatbot.py file.
bash
Copy code
python novida_chatbot.py
The application will open a window with the chatbot interface. Type your message in the input box and click the "Send" button. The chatbot will respond with a text-based reply and read it out loud using text-to-speech.
You can clear the chat history by pressing the "Clear" button.
Features Overview
Chatbot Response
The chatbot will provide responses based on predefined patterns.
For example, it can respond to "hi", "how are you", and "goodbye".
Text-to-Speech
The chatbot speaks its responses using the pyttsx3 library.
The speech will be played automatically after every response.
Clear Chat History
The "Clear" button clears the chat history from the chatbox.
Code Explanation
Tkinter GUI
The GUI is built using Tkinter, which creates a window with an input field and a chatbox for displaying messages. There are two buttons: Send and Clear.

Text-to-Speech (pyttsx3)
When the chatbot responds, it uses pyttsx3 to speak the reply out loud.

Wikipedia (Optional)
You can extend the chatbot to fetch Wikipedia summaries if you wish to add more knowledge-based functionality.

Project Structure
bash
Copy code
Novida_Chatbot/
├── novida_chatbot.py        # Main application file
├── Novida chatbot.PNG       # Icon for the application window (optional)
└── README.md                # Project documentation
Acknowledgements
pyttsx3: Text-to-speech library used for converting text to speech.
Tkinter: GUI toolkit for building the chat interface.
Wikipedia: Provides the ability to fetch summaries from Wikipedia (optional feature).

