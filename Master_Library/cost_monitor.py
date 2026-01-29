class CostMonitor:
    def __init__(self):
        self.monthly_costs = {
            "Stripe": "2.9% + 30¢ per transaction",
            "Mercury": "$0 (basic) or $20/mo (treasury)",
            "Google Cloud": "$70/mo (2× Vertex AI)",
            "Cloudflare Pro": "$25/mo",
            "MindSea/Venn": "$99/mo (compliance)",
            "ElevenLabs": "$22/mo (1M characters)",
            "Veo/Sora": "$60/mo (20min of 4K video)",
            "OpenPhone": "$43/mo (phone + transcription)"
        }
    
    def calculate_total(self):
        """Estimates fixed monthly costs"""
        # Simplified calculation
        fixed_costs = 70 + 25 + 99 + 22 + 60 + 43
        return f"Fixed: ${fixed_costs}/mo | Variable: Stripe fees + AI usage"

# monitor = CostMonitor()
# print(monitor.calculate_total())
