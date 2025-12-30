import customtkinter as ctk
import threading
import os
from tkinter import END

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class BhaiGUI(ctk.CTk):
    def __init__(self, brain_instance, voice_callback):
        super().__init__()
        self.brain = brain_instance
        self.process_voice = voice_callback
        self.title("Mera Bhai Assistant 😎")
        self.geometry("450x700")
        
        # UI Elements
        self.header = ctk.CTkFrame(self, height=60, fg_color="#202c33")
        self.header.pack(fill="x")
        self.status_lbl = ctk.CTkLabel(self.header, text="Mera Bhai ❤️", font=("Segoe UI", 20, "bold"))
        self.status_lbl.pack(pady=10)

        self.chat_area = ctk.CTkScrollableFrame(self, fg_color="#0b141a")
        self.chat_area.pack(expand=True, fill="both")

        self.input_frame = ctk.CTkFrame(self, height=60, fg_color="#202c33")
        self.input_frame.pack(fill="x", side="bottom")

        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text="Bhai se kuch bol...")
        self.entry.pack(side="left", padx=10, pady=10, expand=True, fill="x")
        self.entry.bind("<Return>", self.send_text)

        self.mic_btn = ctk.CTkButton(self.input_frame, text="🎤", width=40, command=self.start_listening)
        self.mic_btn.pack(side="right", padx=10)

    def add_message(self, text, is_user):
        color = "#005c4b" if is_user else "#202c33"
        align = "right" if is_user else "left"
        frame = ctk.CTkFrame(self.chat_area, fg_color=color, corner_radius=15)
        frame.pack(padx=10, pady=5, anchor="e" if is_user else "w")
        lbl = ctk.CTkLabel(frame, text=text, wraplength=300)
        lbl.pack(padx=15, pady=10)

    def send_text(self, event=None):
        text = self.entry.get()
        if text:
            self.add_message(text, True)
            self.entry.delete(0, END)
            threading.Thread(target=self.process_response, args=(text,), daemon=True).start()

    def start_listening(self):
        self.status_lbl.configure(text="Sun raha hoon... 👂", text_color="yellow")
        threading.Thread(target=self.process_voice, daemon=True).start()

    def process_response(self, text):
        response = self.brain.process_command(text)
        self.after(100, lambda: self.add_message(response, False))
        self.after(100, lambda: self.status_lbl.configure(text="Mera Bhai ❤️", text_color="white"))
        self.speak_response(response)

    def speak_response(self, text):
        def play():
            try:
                # Edge-TTS se awaaz banao aur Windows se play karo
                os.system(f'edge-tts --voice hi-IN-MadhurNeural --text "{text}" --write-media reply.mp3')
                os.system('start /min reply.mp3')
            except: pass
        threading.Thread(target=play, daemon=True).start()
