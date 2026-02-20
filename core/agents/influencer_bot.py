from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class InfluencerBot:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def craft_pitch(self, influencer_name, top_location):
        """توليد رسالة تفاوض ذكية بناءً على بيانات الموقع"""
        prompt = f"""
        You are a Senior Partnership Manager at GeoInvest AI. 
        Write a short, high-end outreach message to the influencer '{influencer_name}'.
        Tell them we identified a massive investment opportunity in '{top_location}' using our AI.
        Offer them an exclusive partnership with 15% commission on referrals.
        Tone: Professional, elite, and data-driven.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Negotiation Logic Error: {e}"

# تجربة سريعة للوكيل
if __name__ == "__main__":
    bot = InfluencerBot()
    print(bot.craft_pitch("Marwan Tech", "Arkan Plaza, Sheikh Zayed"))