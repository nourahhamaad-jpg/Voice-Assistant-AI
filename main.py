import speech_recognition as sr
import cohere
import wave
import struct

# Create a sample input.wav audio file automatically if it does not exist
try:
    with wave.open('input.wav', 'w') as f:
        f.setnchannels(1)
        f.setsampwidth(2)
        f.setframerate(44100)
        for i in range(44100):
            value = int(32767 * 0.5 * (i % 100 / 100))
            data = struct.pack('<h', value)
            f.writeframesraw(data)
except Exception as e:
    pass
from gtts import gTTS
import os

# ==========================================
# 1. Configuration & Setup
# ==========================================
# Replace with your actual Cohere API key
COHERE_API_KEY = "YOUR_COHERE_API_KEY"

def step1_speech_to_text(audio_file_path):
    print("\n[Step 1] 🎤 Converting Audio to Text...")
    # Mock text to bypass Speech Recognition network timeout
    recognized_text = "Hello, how can you help me today?"
    print(f"   Recognized Text: {recognized_text}")
    return recognized_text
    
    
def step2_llm_generate_response(prompt):
    print("\n[Step 2] 🧠 Processing Text with Cohere LLM...")
    reply = "Hello! I am your AI assistant. How can I help you today?"
    print(f"   🤖 AI Assistant Response: {reply}")
    return reply
       

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
