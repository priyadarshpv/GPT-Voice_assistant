from openai import OpenAI
import pyttsx3
import speech_recognition as sr
import time


client = OpenAI(api_key="your_api_key")


engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=3500,
            n=1,
            stop=None,
            temperature=0.5,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred with the OpenAI API: {e}")
        return "Sorry, I couldn't generate a response."


def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print("Say 'GPT' to start recording your question...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            recognizer.adjust_for_ambient_noise(source, duration=2)  
            try:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5) 
                print("Processing...")
                transcription = recognizer.recognize_google(audio)
                print(f"You said: {transcription}")
                print(f"Transcription (lowercase): {transcription.lower()}")  
                if "gpt" in transcription.lower():
                    filename = "input.wav"
                    print("Say your question...")
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source)
                        audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())

                    
                    text = transcribe_audio_to_text(filename)
                    if text:
                        print(f"You said: {text}")

                        response = generate_response(text)
                        print(f"GPT-3.5-turbo says: {response}")

                        speak_text(response)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand the audio. Please speak clearly and try again.")
            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

