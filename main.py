import speech_recognition as sr
import cohere
from gTTS import gTTS
import os

# ==========================================
# 1. Configuration & Setup
# ==========================================
# Replace with your actual Cohere API key
COHERE_API_KEY = "YOUR_COHERE_API_KEY"

def step1_speech_to_text(audio_file_path):
    """
    Step 1: Convert spoken audio to text (Speech-to-Text)
    """
    print("\n[Step 1] 🎤 Converting Audio to Text...")
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)
            # You can change language to 'en-US' or 'ar-SA' depending on your audio input
            text = recognizer.recognize_google(audio_data, language="ar-SA")
            print(f"   💬 Transcribed Text: {text}")
            return text
    except Exception as e:
        print(f"   ❌ Error during Speech Recognition: {e}")
        return None

def step2_llm_generate_response(prompt):
    """
    Step 2: Process text using Cohere LLM to generate a response
    """
    print("\n[Step 2] 🧠 Processing Text with Cohere LLM...")
    try:
        co = cohere.Client(COHERE_API_KEY)
        response = co.chat(
            model='command-r-plus',
            message=prompt
        )
        reply = response.text
        print(f"   🤖 AI Assistant Response: {reply}")
        return reply
    except Exception as e:
        print(f"   ❌ Error with Cohere API: {e}")
        return None

def step3_text_to_speech(text):
    """
    Step 3: Convert text response into audio (Text-to-Speech)
    """
    print("\n[Step 3] 🔊 Converting Text Response to Speech...")
    try:
        tts = gTTS(text=text, lang='ar', slow=False)
        output_filename = "response.mp3"
        tts.save(output_filename)
        print(f"   ✅ Audio response saved successfully as: {output_filename}")
        
        # Play the generated audio file (macOS)
        os.system(f"afplay {output_filename}")
    except Exception as e:
        print(f"   ❌ Error during Text-to-Speech conversion: {e}")

# ==========================================
# Main Execution Pipeline
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("🤖 Voice-to-Voice AI Assistant Pipeline 🤖")
    print("============================================")
    
    # Provide the path to your input audio file (e.g., input.wav)
    audio_input_file = "input.wav" 
    
    # 1. Speech-to-Text
    user_text = step1_speech_to_text(audio_input_file)
    
    if user_text:
        # 2. LLM Processing
        ai_reply = step2_llm_generate_response(user_text)
        
        if ai_reply:
            # 3. Text-to-Speech
            step3_text_to_speech(ai_reply)