from google import genai # Nayi library
import datetime
import psutil
import webbrowser

class BhaiBrain:
    def __init__(self, api_key):
        try:
            # Naya Client structure
            self.client = genai.Client(api_key=api_key)
            self.model_id = "gemini-1.5-flash" 
            
            self.instruction = (
                "Tu ek super-intelligent desi AI assistant hai jiska naam 'Bhai' hai. "
                "Teri baatein cool aur Hinglish mein hoti hain. "
                "C code hamesha Prototype -> Main -> Definition structure mein dena."
            )
            print("Bhai ka naya system ready hai! ✅")
        except Exception as e:
            print(f"Setup Error: {e}")

    def process_command(self, command):
        command = command.lower()
        
        if "time" in command:
            return f"Abhi {datetime.datetime.now().strftime('%I:%M %p')} ho rahe hain bhai."
        
        elif "battery" in command:
            return f"Battery {psutil.sensors_battery().percent}% hai."

        else:
            try:
                # Naya tarika message bhejne ka
                response = self.client.models.generate_content(
                    model=self.model_id,
                    contents=command,
                    config={'system_instruction': self.instruction}
                )
                return response.text
            except Exception as e:
                print(f"Asli Error Terminal mein dekho: {e}")
                return "Bhai, abhi bhi connection mein locha hai!"
