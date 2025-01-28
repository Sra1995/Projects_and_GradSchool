# Real-Time Anonymous Chat Application

## Project Description

Have you ever seen those anonymous chat applications in movies where characters communicate without revealing their identities? Inspired by that concept, I wanted to create my own anonymous chat application but with a unique twist: **a one-way chat experience**. In this application, users can send messages anonymously, but they cannot see their own messages once sent. However, they can see responses from other users in real time, creating a dynamic and mysterious communication environment.

This project is built using **Flask** and **Socket.IO** for real-time communication, along with HTML, JavaScript, and Tailwind CSS for the front end.

---

## Features

- **Anonymous Messaging**: No usernames or identities are required; simply join and chat.
- **One-Way Chat Experience**: Users can send messages but cannot see their own messages in the chat window, adding a unique layer of anonymity.
- **Real-Time Updates**: Messages are broadcast to all connected users in real time using Flask-SocketIO.
- **Responsive Design**: The front end is styled with Tailwind CSS for a modern, responsive look.

---

## How It Works

### 1. Backend
The backend is built using **Flask** and **Flask-SocketIO**. It handles:
- Receiving messages from users.
- Broadcasting messages to all connected clients.
- Managing WebSocket connections for real-time communication.

### 2. Frontend
The frontend:
- Allows users to type messages and send them.
- Displays messages from other users in real time.
- Ensures users cannot see their own sent messages.

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Node.js (optional, for live testing with npm packages)

### Installation

1. Clone the repository:

  
2. Install the required Python packages:

pip install flask flask-socketio


3.	Run the application:

python chat.py


4.	Open your browser and go to http://localhost:5000 to use the application.

How to Use
	1.	Open the chat application in your browser.
	2.	Start typing your messages in the input box and press Send.
	3.	Your message will not appear in your chat window, but other users’ messages will appear in real time.
	4.	Enjoy the anonymous and unique chat experience!

File Structure
```
project/
│
├── templates/
│   └── index.html        # Frontend HTML template
├── static/
│   └── styles.css        # Tailwind CSS file (optional)
├── chat.py               # Flask backend with Socket.IO
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```
Future Improvements
	•	User Avatars: Add random avatars for users to identify message sources.
	•	Custom Rooms: Allow users to create and join separate chat rooms.
	•	Message Moderation: Add spam detection and profanity filters.
	•	Mobile-Friendly Design: Enhance responsiveness for mobile devices.
	•	Deploy Online: Host the app on platforms like Heroku or AWS for public use.

Inspiration

This project was inspired by the anonymous chat applications you see in movies, but I wanted to add my own twist. Instead of a traditional two-way chat, I wanted to create a one-way communication system where users can only see responses from others, making the experience more mysterious and unique as if they would use burner phone.

Technologies Used
	•	Flask: Backend framework for Python.
	•	Flask-SocketIO: Real-time WebSocket communication.
	•	HTML5 & JavaScript: Frontend for structure and interactivity.
	•	Tailwind CSS: Styling for a modern, responsive UI.

Acknowledgments

Special thanks to the open-source community for resources and tutorials that helped bring this project to life.

License

This project is open-source and available under the MIT License.
