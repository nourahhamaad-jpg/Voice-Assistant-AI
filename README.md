# 🎙️ Voice-to-Voice AI Assistant

An intelligent voice-to-voice AI pipeline built using Python. The application receives an audio input, converts the speech to text, processes it using the Cohere Large Language Model (LLM), and finally converts the text response back into spoken audio.

---

## 🏗️ System Architecture & Workflow

The system operates in 3 core steps:

[Audio Input (.wav)] -> (1) Speech-to-Text -> [Text Prompt] -> (2) Cohere LLM -> [Text Response] -> (3) Text-to-Speech -> [Audio Output (.mp3)]

1. Speech-to-Text (STT): Converts the input audio file into raw text using Google Speech Recognition API (SpeechRecognition).
2. LLM Processing: Sends the converted text prompt to the Cohere Chat Model (cohere) to generate an intelligent response.
3. Text-to-Speech (TTS): Transforms the text response back to speech using Google Text-to-Speech (gTTS) and plays the generated .mp3 file.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed on your system.

### 1. Installation
Install all required dependencies using:
pip install -r requirements.txt

### 2. Configuration
Open main.py and set your Cohere API key:
COHERE_API_KEY = "YOUR_COHERE_API_KEY"

### 3. Running the Project
Place your target audio input file (e.g., input.wav) in the project directory, then execute:
python3 main.py

---

## 📁 Repository Structure

- main.py: Main executable python file containing the Voice-to-Voice pipeline logic.
- requirements.txt: List of Python packages required to run the project.
- README.md: Comprehensive documentation explaining the project setup and execution steps.
