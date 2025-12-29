import asyncio
import edge_tts
import os
import datetime
import webbrowser
import google.generativeai as genai
import time
import random
import threading
import speech_recognition as sr
import tkinter as tk
from tkinter import scrolledtext

# --- 1. GEMINI AI SETUP ---
# Model ko 'gemini-pro' rakha hai taaki 404 error na aaye
genai.configure(api_key="AIzaSyBneFle5s6nY9uzTJd21Fmp-ASwrrtHock")
model = genai.GenerativeModel('gemini-pro')

# --- 2. VOICE ENGINE (Madhur Voice) ---
async def speak_bhai(text):
    if not text: return
    voice = "hi-IN-MadhurNeural" 
    output_file = f"bhai_resp_{random.randint(1, 999)}.mp3"
    try:
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)
        # Windows Media Player background mein chalega
        os.system(f'start /min wmplayer "{os.path.abspath(output_file)}"')
        await asyncio.sleep(5) 
    except Exception as e:
        print(f"Voice Error: {e}")

# --- 3. LISTENING ENGINE (Siri Feature) ---
def listen_me():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sun raha hoon bhai...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        # Google recognize karega teri Hindi/English mix
        query = recognizer.recognize_google(audio, language='hi-IN')
        return query
    except:
        return ""

# --- 4. APP UI (Text + Voice Combined) ---
class BhaiApp:
    def __init__(self, root, loop):
        self.root = root
        self.loop = loop
        self.root.title("Mera Bhai AI - Siri Mode")
        self.root.geometry("450x600")
        self.root.configure(bg="#121212")

        # Chat Window (Jahan Text dikhega)
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#1e1e1e", fg="#00ff00", font=("Consolas", 11))
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.insert(tk.END, "Bhai: Bol jigar! Chahe bol ke bata ya likh ke, tera bhai hazir hai. 🚀\n\n")

        # Buttons Frame
        self.btn_frame = tk.Frame(root, bg="#121212")
        self.btn_frame.pack(pady=10)

        # Siri (Mic) Button
        self.mic_btn = tk.Button(self.btn_frame, text="🎤 Bol Kar Bata", command=self.voice_command, bg="#ff4b4b", fg="white", font=("Arial", 10, "bold"), width=15)
        self.mic_btn.pack(side=tk.LEFT, padx=5)

        # Input Box (Type karne ke liye)
        self.user_input = tk.Entry(root, bg="#2d2d2d", fg="white", font=("Arial", 12), insertbackground="white")
        self.user_input.pack(padx=10, pady=5, fill=tk.X)
        self.user_input.bind("<Return>", self.text_command)

    def update_chat(self, user_text, bhai_text):
        self.chat_area.insert(tk.END, f"Tu: {user_text}\n")
        self.chat_area.insert(tk.END, f"Bhai: {bhai_text}\n\n")
        self.chat_area.yview(tk.END)
        # Awaaz nikaalo
        asyncio.run_coroutine_threadsafe(speak_bhai(bhai_text), self.loop)

    def voice_command(self):
        def run():
            query = listen_me()
            if query:
                response = self.process_logic(query)
                self.update_chat(query, response)
        threading.Thread(target=run, daemon=True).start()

    def text_command(self, event=None):
        query = self.user_input.get()
        if query:
            self.user_input.delete(0, tk.END)
            response = self.process_logic(query)
            self.update_chat(query, response)

    def process_logic(self, query):
        query = query.lower()
        if "time" in query or "samay" in query:
            return f"Abhi {datetime.datetime.now().strftime('%I:%M %p')} ho rahe hain."
        elif "youtube" in query:
            webbrowser.open("https://youtube.com")
            return "YouTube khol diya bhai, maze kar!"
        else:
            try:
                # AI Response
                res = model.generate_content(f"Desi bhai style mein chota jawab do: {query}")
                return res.text
            except:
                return "Bhai, AI nakhre kar raha hai, ek baar net check kar!"

# --- EXECUTION ---
if __name__ == "__main__":
    root = tk.Tk()
    new_loop = asyncio.new_event_loop()
    def start_loop(loop):
        asyncio.set_event_loop(loop)
        loop.run_forever()
    
    threading.Thread(target=start_loop, args=(new_loop,), daemon=True).start()
    app = BhaiApp(root, new_loop)
    root.mainloop()