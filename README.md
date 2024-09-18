
# Gemini API Chatbot

This is a chatbot web application that uses the **Gemini API** provided by Google for natural language processing and communication. The project is built with **Python** and the **Flask** framework for the backend, and utilizes **HTML**, **CSS**, and **JavaScript** for the frontend.

## Features

- Interactive chatbot interface to engage in conversations.
- Uses the Gemini API for AI-based responses.
- Real-time message handling and display.
- Simple, clean design with responsive UI.
- Built-in support for multiple message formats, including text, links, and code snippets.

## Technologies Used

- **Backend**: Python, Flask framework
- **Frontend**: HTML, CSS, JavaScript
- **API**: Gemini API by Google for handling chat responses
- **Deployment**: Flask-based web server

## Project Structure

The project is organized as follows:

```

GenAI-Gemini/
├── static/
│   ├── css/
│   │   └── styles.css     # Custom styles for the chatbot
│   ├── js/
│   │   └── script.js      # Frontend JavaScript for sending/receiving messages
├── templates/
│   │   └── includes
│   │       ├── header.html # Header template
│   │       └── footer.html # Footer template
│   └── home.html           # Main HTML file for the chatbot UI
└── main.py                 # Flask application (Backend)
├── server.py               # Flask application (Backend)
├── README.md               # Project documentation
└── requirements.txt        # Required Python libraries (Flask, requests, etc.)
```

## Installation

To set up the chatbot locally, follow these steps:

### 1. Clone the Repository

```bash
git clone https://github.com/manojPragada/GenAI-Gemini.git
cd GenAI-Gemini
```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to manage dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a `.env` file in the root directory of the project and include your Gemini API credentials:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

### 5. Run the Flask App

After setting up the environment, run the Flask app:

```bash
flask run
```
The application will be available at `http://127.0.0.1:8080`.

## Usage

- Open the chatbot in your browser.
- Type your message in the input box and press Enter to chat.
- The Gemini API will process the input and generate a response, which will be displayed in real-time.

## Frontend (UI)

- The interface includes a text input box for users to enter their messages.
- Message bubbles appear in real-time, with clear differentiation between user messages and responses from the chatbot.
- Messages support basic formatting like lists, bold text, and links, powered by the Gemini API.

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or support, please reach out to:

- Your Name: [pragadasaimanoj@gmail.com](mailto:pragadasaimanoj@gmail.com)
- GitHub: [manojPragada](https://github.com/manojPragada)
