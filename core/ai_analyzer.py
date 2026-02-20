from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

class AIInvestmentAdvisor:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        # التحقق من وجود المفتاح وتنسيقه
        if self.api_key and self.api_key.startswith("sk-"):
            self.client = OpenAI(api_key=self.api_key)
        else:
            self.client = None

    def generate_analysis(self, summary_dict):
        if not self.client:
            return self._get_mock_analysis(summary_dict)
        
        try:
            prompt = f"Analyze this market data for Sheikh Zayed City: {summary_dict}. " \
                     f"Identify the biggest gap (underserved business) and give a ROI estimate."
            
            response = self.client.chat.completions.create(
                model="gpt-4o", # استخدام أحدث موديل
                messages=[
                    {"role": "system", "content": "You are a professional investment consultant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return self._get_mock_analysis(summary_dict)

    def _get_mock_analysis(self, summary_dict):
        # تحليل احتياطي في حالة تعطل الـ API
        return f"""
        📊 **Preliminary Market Analysis (Simulation Mode)**
        * **Current Density:** {summary_dict}
        * **Market Gap:** High saturation in 'Cafes'. Significant lack of 'Specialized Fitness Centers'.
        * **Recommendation:** Investing in a Boutique Gym or Health Clinic in the Central District shows a 25% projected annual ROI.
        * **Risk:** Low-Medium.
        """