import datetime
import psutil
import webbrowser
import google.generativeai as genai
import os

class BhaiBrain:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.instruction = (
            "Tu ek super-intelligent desi AI assistant hai jiska naam 'Bhai' hai. "
            "Tu user ka sabse pakka yaar hai. Teri baatein cool, swaggy aur Hinglish mein hoti hain. "
            "Hamesha chote aur mazedaar desi jawab dena. User ki pichli baatein yaad rakhna."
        )
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash", 
            system_instruction=self.instruction
        )
        self.chat_session = self.model.start_chat(history=[])

    def process_command(self, command):
        command = command.lower()
        if "time" in command or "samay" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            return f"Abhi baj rahe hain {now} yaar! Late ho raha kya? ⏰"
        
        elif "battery" in command:
            battery = psutil.sensors_battery()
            return f"Battery {battery.percent}% hai boss. 👍"
        
        elif "youtube" in command:
            webbrowser.open("https://youtube.com")
            return "YouTube ready hai bhai! Kya dekhega? 🎬"
        
        else:
            try:
                response = self.chat_session.send_message(command)
                return response.text
            except:
                return "Bhai, net ya API key nakhre kar rahi hai!"
