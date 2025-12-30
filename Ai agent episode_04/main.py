import speech_recognition as sr
from bhai_brain import BhaiBrain
from gui import BhaiGUI

API_KEY = "YOUR GOOGLE STUDIO API KEY" # Aapki Key
brain = BhaiBrain(API_KEY)

def handle_voice():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio, language='hi-IN')
            app.after(0, lambda: app.add_message(query, True))
            app.process_response(query)
        except:
            app.after(0, lambda: app.status_lbl.configure(text="Nahi suna bhai!", text_color="red"))

if __name__ == "__main__":
    app = BhaiGUI(brain, handle_voice)
    app.mainloop()
