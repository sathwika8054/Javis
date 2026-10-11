import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import pyjokes
import datetime
import webbrowser
import os


# ---------------- TEXT TO SPEECH ----------------

engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# ---------------- VOICE INPUT ----------------

def take_command():
    listener = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("\nListening...")

            listener.adjust_for_ambient_noise(source, duration=1)

            audio = listener.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        print("Recognizing...")

        command = listener.recognize_google(audio)
        command = command.lower()

        print("You:", command)

        return command

    except sr.WaitTimeoutError:
        print("No speech detected")
        return ""

    except sr.UnknownValueError:
        print("Could not understand")
        return ""

    except Exception as e:
        print("Error:", e)
        return ""


# ---------------- WELCOME ----------------

speak("Hello. I am Jarvis.")
speak("How can I help you?")


# ---------------- MAIN LOOP ----------------

while True:

    command = take_command()

    if command == "":
        continue

    # Open Google
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # Open YouTube
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Open ChatGPT
    elif "open chatgpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com")

    # Open Instagram
    elif "open instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://www.instagram.com")

    # Time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak("Current time is " + current_time)

    # Date
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + current_date)

    # Play music
    elif "play" in command:
        song = command.replace("play", "").strip()

        if song:
            speak("Playing " + song)
            pywhatkit.playonyt(song)
        else:
            speak("Please tell the song name")

    # Wikipedia: Who is
    elif "who is" in command:
        person = command.replace("who is", "").strip()

        try:
            info = wikipedia.summary(person, sentences=2)
            print("\nWikipedia:", info)
            speak(info)

        except:
            speak("Sorry, I couldn't find information.")

    # Wikipedia: What is
    elif "what is" in command:
        thing = command.replace("what is", "").strip()

        try:
            info = wikipedia.summary(thing, sentences=2)
            print("\nWikipedia:", info)
            speak(info)

        except:
            speak("Sorry, I couldn't find information.")

    # Joke
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)

    # Greetings
    elif "hello" in command:
        speak("Hello. How are you?")

    elif "how are you" in command:
        speak("I am fine. Thank you for asking.")

    # Exit
    elif "exit" in command or "stop" in command or "bye" in command:
        speak("Goodbye")
        speak("Have a nice day")
        break

    # Unknown command
    else:
        speak("Sorry. I did not understand that command.")