import customtkinter as ctk
import threading
from tkinter import END

# Settings
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class ChatBubble(ctk.CTkFrame):
    def __init__(self, master, message, is_user=True, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)
        
        # using if-else statment
        if is_user:
            # User Message (Right aligned, Blue-ish)
            self.msg_frame = ctk.CTkFrame(self, fg_color="#005c4b", corner_radius=15)
            self.msg_frame.pack(side="right", padx=10, pady=5, anchor="e")
            lbl = ctk.CTkLabel(self.msg_frame, text=message, font=("Segoe UI", 14), text_color="white", wraplength=350, justify="left")
            lbl.pack(padx=15, pady=10)
        else:
            # Bhai Message (Left aligned, Dark Grey)
            self.msg_frame = ctk.CTkFrame(self, fg_color="#202c33", corner_radius=15)
            self.msg_frame.pack(side="left", padx=10, pady=5, anchor="w")
            lbl = ctk.CTkLabel(self.msg_frame, text=message, font=("Segoe UI", 14), text_color="white", wraplength=350, justify="left")
            lbl.pack(padx=15, pady=10)

class BhaiGUI(ctk.CTk):
    def __init__(self, brain_instance, voice_callback):
        super().__init__()
        self.brain = brain_instance
        self.process_voice = voice_callback
        
        self.title("Mera Bhai Assistant 😎")
        self.geometry("450x700")
        
        # Header
        self.header = ctk.CTkFrame(self, height=60, corner_radius=0, fg_color="#202c33")
        self.header.pack(fill="x", side="top")
        
        self.status_lbl = ctk.CTkLabel(self.header, text="Mera Bhai ❤️", font=("Segoe UI", 20, "bold"))
        self.status_lbl.pack(pady=10, side="left", padx=20)

        # Chat Area
        self.chat_area = ctk.CTkScrollableFrame(self, fg_color="#0b141a")
        self.chat_area.pack(expand=True, fill="both")

        # Input Area
        self.input_frame = ctk.CTkFrame(self, height=60, fg_color="#202c33", corner_radius=0)
        self.input_frame.pack(fill="x", side="bottom")

        self.entry = ctk.CTkEntry(self.input_frame, placeholder_text="Bhai se kuch bol...", height=40)
        self.entry.pack(side="left", padx=10, pady=10, expand=True, fill="x")
        self.entry.bind("<Return>", self.send_text)

        self.mic_btn = ctk.CTkButton(self.input_frame, text="🎤", width=40, command=self.start_listening)
        self.mic_btn.pack(side="right", padx=10)

    def add_message(self, text, is_user):
        bubble = ChatBubble(self.chat_area, message=text, is_user=is_user)
        bubble.pack(fill="x", pady=2)

    def send_text(self, event=None):
        text = self.entry.get()
        if text:
            self.add_message(text, True)
            self.entry.delete(0, END)
            self.process_response(text)

    def start_listening(self):
        self.process_voice()

    def process_response(self, text):
        response = self.brain.process_command(text)
        self.after(500, lambda: self.add_message(response, False))
        self.speak_response(response)

    def speak_response(self, text):
        pass