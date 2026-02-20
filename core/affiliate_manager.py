import hashlib

class AffiliateManager:
    """إدارة العمولات والروابط التسويقية"""
    
    @staticmethod
    def generate_referral_code(user_id):
        # توليد كود فريد لكل شريك
        return hashlib.md5(str(user_id).encode()).hexdigest()[:8].upper()

    @staticmethod
    def calculate_commission(package_price, percentage=0.20):
        # حساب عمولة الشريك (20% كافتراضي)
        return package_price * percentage

# مثال للاستخدام في لوحة التحكم مستقبلاً
# code = AffiliateManager.generate_referral_code("influencer_1")
# print(f"Your Affiliate Code: {code}")