import speech_recognition as sr
import webbrowser
import time
import pyautogui
import win32com.client

# Initialize Windows TTS
speaker = win32com.client.Dispatch("SAPI.SpVoice")

print("Initializing Jarvis...")
speaker.Speak("Initializing Jarvis")
speaker.Speak("JARVIS, your machine assistant")
speaker.Speak("Designed by Zaid ")
time.sleep(1)
r = sr.Recognizer()
speaker.Speak("Listening command")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            command = r.recognize_google(audio).lower()
            print(command)

            if "exit" in command:
                speaker.Speak("Okay, going to sleep.")
                break

            if "jarvis" in command:
                print("Welcome home sir, How can I help you.")
                speaker.Speak("Welcome home sir, How can I help you.")

            if "open google" in command:
                webbrowser.open("https://www.google.com")
                speaker.Speak("Opening Google.")

            elif "open youtube" in command:
                webbrowser.open("https://www.youtube.com")
                speaker.Speak("Opening YouTube.")

            elif "play believer" in command:
                webbrowser.open("https://www.youtube.com/watch?v=W0DM5lcj6mw")
                speaker.Speak("Playing Believer on YouTube.")

            elif "open instagram" in command:
                webbrowser.open("https://www.instagram.com")
                speaker.Speak("Opening Instagram.")

            elif "open linkedin" in command:
                webbrowser.open("https://www.linkedin.com")
                speaker.Speak("Opening LinkedIn.")

            elif "take screenshot" in command or "screenshot" in command:
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot.png")
                speaker.Speak("Screenshot taken and saved.")

            elif "open chatgpt" in command or "chat gpt" in command:
                webbrowser.open("https://chatgpt.com/")
                speaker.Speak("Opening ChatGPT.")

            else:
                speaker.Speak("Sorry, I didn't understand the command.")

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the command.")
    except sr.RequestError:
        print("Network error.")
