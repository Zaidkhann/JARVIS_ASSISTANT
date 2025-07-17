import speech_recognition as sr
import webbrowser
import time
import pyautogui
import pyttsx3

# Initialize Windows TTS
engine = pyttsx3.init()
print("Initializing Jarvis...")
engine.say("Initializing Jarvis")
engine.runAndWait()
engine.say("JARVIS, your machine assistant")
engine.runAndWait()
engine.say("Designed by Zaid ")
engine.runAndWait()
time.sleep(1)
r = sr.Recognizer()
engine.say("Listening command")
engine.runAndWait()

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            command = r.recognize_google(audio).lower()
            print(command)

            if "exit" in command:
                engine.say("Okay, going to sleep.")
                engine.runAndWait()
                break

            if "jarvis" in command:
                print("Welcome home sir, How can I help you.")
                engine.say("Welcome home sir, How can I help you.")
                engine.runAndWait()

            if "open google" in command:
                webbrowser.open("https://www.google.com")
                engine.say("Opening Google.")
                engine.runAndWait()

            elif "open youtube" in command:
                webbrowser.open("https://www.youtube.com")
                engine.say("Opening YouTube.")
                engine.runAndWait()

            elif "play believer" in command:
                webbrowser.open("https://www.youtube.com/watch?v=W0DM5lcj6mw")
                engine.say("Playing Believer on YouTube.")
                engine.runAndWait()

            elif "open instagram" in command:
                webbrowser.open("https://www.instagram.com")
                engine.say("Opening Instagram.")
                engine.runAndWait()

            elif "open linkedin" in command:
                webbrowser.open("https://www.linkedin.com")
                engine.say("Opening LinkedIn.")
                engine.runAndWait()

            elif "take screenshot" in command or "screenshot" in command:
                screenshot = pyautogui.screenshot()
                screenshot.save("screenshot.png")
                engine.say("Screenshot taken and saved.")
                engine.runAndWait()

            elif "open chatgpt" in command or "chat gpt" in command:
                webbrowser.open("https://chatgpt.com/")
                engine.say("Opening ChatGPT.")
                engine.runAndWait()

            else:
                engine.say("Sorry, I didn't understand the command.")
                engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I couldn't understand the command.")
    except sr.RequestError:
        print("Network error.")
