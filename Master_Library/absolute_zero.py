class AbsoluteZero:
    def __init__(self):
        self.human_cost = 0
        self.subscription_cost = 0  # Use open-source models or one-time API keys
    
    def calculate_profit(self, revenue):
        """100% profit minus domain fees and taxes"""
        domain_fee = 12  # Annual .ai domain
        taxes = revenue * 0.20  # Rough estimate
        
        net_profit = revenue - domain_fee - taxes
        return f"Revenue: ${revenue:,} | Net Profit: ${net_profit:,} (≈{(net_profit/revenue)*100:.0f}%)"

# Example: 100 users × $2,499
# zero = AbsoluteZero()
# print(zero.calculate_profit(249900))
# Output: Revenue: $249,900 | Net Profit: $199,908 (≈80%)
