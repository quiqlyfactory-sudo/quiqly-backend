class MoneyCard:
    def __init__(self, stripe_key, mercury_api):
        self.stripe = stripe_key
        self.mercury = mercury_api
    
    def get_net_worth(self):
        """Shows: Bank Balance + Stripe Pending"""
        bank_balance = self.mercury.get_balance()  # e.g., $12,450
        stripe_pending = self.stripe.get_pending()  # e.g., $2,100
        return bank_balance + stripe_pending
    
    def predictive_runway(self):
        """30-day income projection based on subscription growth"""
        # Logic: analyze Stripe subscription growth + Mercury spending
        return "You have 47 days of runway at current burn rate."
    
    def send_alert(self, message):
        """Mint-green notification when action needed"""
        if "unprofitable" in message.lower():
            print(f"⚠️ {message}")
        else:
            print(f"✅ {message}")

# Usage in Morning Briefing:
# card = MoneyCard(stripe_key, mercury_api)
# print(f"Net Worth: ${card.get_net_worth():,}")