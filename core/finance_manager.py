import hashlib

class FinanceManager:
    def __init__(self, commission_rate=0.20):
        self.commission_rate = commission_rate

    def generate_affiliate_link(self, influencer_name):
        # توليد كود فريد للمؤثر
        short_hash = hashlib.md5(influencer_name.encode()).hexdigest()[:6].upper()
        return f"https://geoinvest.ai/ref/{short_hash}"

    def calculate_payout(self, total_sales):
        # حساب العمولة (مثلاً 20% من سعر التقرير)
        return total_sales * self.commission_rate

# تجربة سريعة
# fm = FinanceManager()
# print(fm.generate_affiliate_link("Zayed_Vlogger"))