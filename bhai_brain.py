import random
import datetime
import psutil
import webbrowser
import os
import pywhatkit
# brai d=addressing/instruction
class BhaiBrain:
    def __init__(self):
        self.user_name = "Bhai"
    
    def get_time(self):
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"Abhi baj rahe hain {now} yaar! Late ho raha kya? ⏰"

    def get_battery(self):
        battery = psutil.sensors_battery()
        percent = battery.percent
        if percent > 70:
            return f"Battery full power hai bhai: {percent}%! 😎 Tension mat le."
        elif percent < 20:
            return f"Arre bhai battery {percent}% hai! Charger laga de warna main bhi so jaunga 😂"
        else:
            return f"Battery {percent}% hai, sab set hai boss. 👍"

    def process_command(self, command):
        command = command.lower()

        #SYSTEM COMMANDS
        if "time" in command or "samay" in command:
            return self.get_time()
        
        elif "battery" in command or "charge" in command:
            return self.get_battery()
        
        elif "chrome" in command or "google" in command:
            webbrowser.open("https://google.com")
            return "Chrome ready hai bhai! Kya search karega – knowledge ya entertainment? 😄"
        
        elif "whatsapp" in command:
            webbrowser.open("https://web.whatsapp.com")
            return "Haan bhai, WhatsApp khol diya! Kisse baat karega aaj? Koi special? 😏"
        
        # --- SMART YOUTUBE LOGIC (Dono features merge karr hai) ---
        elif "play" in command or "gaana" in command or "youtube" in command:
            # Gaane ka naam filter karo
            song = command.replace("play", "").replace("gaana", "").replace("bhai", "").replace("youtube", "").strip()
            
            if song == "":
                # Agar sirf "youtube" bola toh home page kholo
                webbrowser.open("https://youtube.com")
                return "YouTube set hai! Chal kuch mast video dekhte hain 🎬"
            else:
                # Agar gaane ka naam hai toh direct search results kholo (accurate tareeka)
                url = f"https://www.youtube.com/results?search_query={song}"
                webbrowser.open(url)
                return f"Theek hai bhai, YouTube pe '{song}' chala raha hoon. Enjoy kar! 🎶"

        # --- PERSONALITY & CHIT-CHAT ---
        elif "kya haal" in command or "kaise ho" in command:
            return "Arre bhai! Full mast mood mein hoon yaar 😎 Tu bata, aaj kya scene chal raha hai?"
        
        elif "thak gaya" in command or "tired" in command:
            return "Samajh gaya bhai... heavy day tha na? 😔 Chal thoda rest kar, main music on kar du? Ya chai bana du feel ke liye ☕"
        
        elif "boring" in command or "bore" in command:
            return "Arre yaar boring nahi chalega! 🔥 Chal ek joke sun: Ek baar ek bandar ne mirror dekha... chhod, tu hass de bas! 😂 Ab mood fresh hua?"
        
        elif "thanks" in command or "shukriya" in command:
            return "Arre anytime yaar! Tere liye toh main 24/7 ready hoon ❤️ Koi aur kaam bol!"
        
        elif "bye" in command or "good night" in command:
            return "Good night bhai! Sweet dreams de, kal subah fresh uthna aur world conquer karna 🚀 Love you yaar ❤️"
            
        elif "hello" in command or "hi" in command:
            return "Bol bhai! Main sun raha hoon. Aaj kya plan hai? 🚀"

        # FALLBACK
        else:
            return "Sahi baat hai bhai... Aur bata? (Samajh nahi aaya par main sun raha hoon! 😂)"

# Test
if __name__ == "__main__":
    brain = BhaiBrain()
    # Test your command here
    print(brain.process_command("bhai play Karan Aujla For A Reason"))