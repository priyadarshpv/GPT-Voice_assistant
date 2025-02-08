# **Voice Assistant using OpenAI & Google Speech Recognition**  

GPT Voice Assistant is a Python-based voice assistant that listens for a wake word ("GPT"), records the user's question, transcribes it to text using Google Speech Recognition, generates a response using OpenAI's GPT-3.5-turbo, and speaks the response aloud using pyttsx3.

## Features
- **Voice Activation**: Say "GPT" to activate the assistant.
- **Speech-to-Text**: Uses Google Speech Recognition to transcribe audio.
- **AI-Powered Responses**: Uses OpenAI's GPT-3.5-turbo to generate intelligent responses.
- **Text-to-Speech**: Uses pyttsx3 to speak the response.


## **Installation**

### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/voice-assistant.git
cd voice-assistant
```

### **2. Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4. Set Up OpenAI API Key**
- **Method 1: Environment Variable**  
  ```sh
  export OPENAI_API_KEY="your-api-key"  # macOS/Linux
  set OPENAI_API_KEY="your-api-key"  # Windows
  ```
- **Method 2: Directly in Code** (Not recommended for security reasons)  
  Replace `"your-api-key"` in `main.py`:
  ```python
  client = OpenAI(api_key="your-api-key")
  ```

---

## **Usage**
Run the script:
```sh
python main.py
```
1. Say **"GPT"** to activate the assistant.
2. Ask your question after the prompt.
3. The assistant will process and respond with speech.

---

## Future Enhancements
- **Improve Wake Word Detection**: Use advanced voice activity detection instead of Google Speech Recognition for better accuracy.
- **Google Speech API Integration**: Implement real-time streaming speech recognition.
- **GUI Interface**: Develop a simple UI using Tkinter or PyQt.
- **Multi-Language Support**: Expand transcription and text-to-speech to support multiple languages.
- **Context Awareness**: Allow conversations with memory for better interactions.

---


## **License**
This project is open-source under the **MIT License**.


```



