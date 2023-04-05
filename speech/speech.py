import speech_recognition as sr

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)

    try:
        print(f"I think you said \"{r.recognize_google(audio)}\"")
    except sr.RequestError as e:
        print("Error; {0}".format(e))

if __name__ == "__main__":
    main()