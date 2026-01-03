import speech_recognition as sr
from bhai_brain import BhaiBrain
from gui import BhaiGUI

# APNI API KEY YAHAN DAALNA
API_KEY = "Paste you API key here"

brain = BhaiBrain(API_KEY)

def listen_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting noise...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language="hi-IN") # Hindi/English mix samjhega
            
            # GUI mein text bhejo
            app.after(0, lambda: app.add_message(text, True))
            app.after(0, lambda: app.process_response(text))
            
        except sr.UnknownValueError:
            app.after(0, lambda: app.status_lbl.configure(text="Samajh nahi aaya 😅", text_color="red"))
        except sr.RequestError:
            app.after(0, lambda: app.status_lbl.configure(text="Net nahi chal raha ❌", text_color="red"))
        except Exception as e:
            print(e)
        
        # Wapas normal status
        app.after(2000, lambda: app.status_lbl.configure(text="Mera Bhai ❤️", text_color="white"))

if __name__ == "__main__":
    app = BhaiGUI(brain, listen_voice)
    app.mainloop()
