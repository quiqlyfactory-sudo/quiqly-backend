import stripe
import os
from typing import Dict

# Initialize Stripe with free tier (2.9% + $0.30)
stripe.api_key = os.getenv("STRIPE_API_KEY")

class QuiqlyPaymentProcessor:
    """Stripe-only payment processing for Quiqly free tier
    
    Cost: $0 upfront, 2.9% + $0.30 per transaction
    No monthly fees, no hidden costs
    """
    
    def __init__(self):
        self.fee_percentage = 0.029  # 2.9%
        self.fee_fixed = 0.30        # $0.30
    
    def create_payment_link(self, product_name: str, price_cents: int, metadata: Dict = None) -> str:
        """Create a payment link (Quiqly default: $2,499 lifetime)"""
        
        try:
            link = stripe.PaymentLink.create(
                line_items=[
                    {
                        "price_data": {
                            "currency": "usd",
                            "product_data": {
                                "name": product_name,
                                "description": "Lifetime access"
                            },
                            "unit_amount": price_cents
                        },
                        "quantity": 1
                    }
                ],
                metadata=metadata or {}
            )
            return link.url
        except stripe.error.StripeError as e:
            return f"❌ Error creating payment link: {str(e)}"
    
    def calculate_fees(self, amount_cents: int) -> Dict:
        """Calculate Stripe fees (2.9% + $0.30)"""
        fee_amount = int(amount_cents * self.fee_percentage) + int(self.fee_fixed * 100)
        net_amount = amount_cents - fee_amount
        
        return {
            "gross": amount_cents / 100,
            "fee": fee_amount / 100,
            "fee_percent": f"{self.fee_percentage * 100}%",
            "fee_fixed": f"${self.fee_fixed}",
            "net": net_amount / 100
        }
    
    def create_product(self, name: str, description: str, price_cents: int) -> str:
        """Create a Stripe product with price"""
        
        try:
            product = stripe.Product.create(
                name=name,
                description=description,
                metadata={"quiqly": "true"}
            )
            
            price = stripe.Price.create(
                product=product.id,
                unit_amount=price_cents,
                currency="usd"
            )
            
            return f"✅ Product created: {product.id} | Price: ${price_cents/100}"
        except stripe.error.StripeError as e:
            return f"❌ Error: {str(e)}"
    
    def process_webhook(self, event: Dict) -> Dict:
        """Process Stripe webhooks (payment success, etc.)"""
        
        event_type = event['type']
        
        if event_type == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            return {
                "status": "✅ Payment succeeded",
                "amount": payment_intent['amount'] / 100,
                "customer": payment_intent.get('customer', 'unknown'),
                "metadata": payment_intent.get('metadata', {})
            }
        
        elif event_type == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']
            return {
                "status": "❌ Payment failed",
                "error": payment_intent['last_payment_error']['message']
            }
        
        elif event_type == 'charge.refunded':
            charge = event['data']['object']
            return {
                "status": "↩️ Refund processed",
                "amount": charge['amount_refunded'] / 100
            }
        
        return {"status": "⏳ Event logged"}
    
    def create_checkout_session(self, line_items: list, customer_email: str = None) -> str:
        """Create checkout session for cart"""
        
        try:
            session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=line_items,
                mode='payment',
                success_url='https://example.com/success',
                cancel_url='https://example.com/cancel',
                customer_email=customer_email
            )
            return session.url
        except stripe.error.StripeError as e:
            return f"❌ Error: {str(e)}"
    
    def get_dashboard_metrics(self) -> Dict:
        """Get sales metrics from Stripe"""
        
        try:
            # Get recent charges
            charges = stripe.Charge.list(limit=10)
            
            total_revenue = sum(c.amount for c in charges.data) / 100
            total_fees = sum(c.amount * self.fee_percentage for c in charges.data) / 100 + len(charges.data) * self.fee_fixed
            net_revenue = total_revenue - total_fees
            
            return {
                "total_charges": len(charges.data),
                "total_revenue": f"${total_revenue:.2f}",
                "total_fees": f"${total_fees:.2f}",
                "net_revenue": f"${net_revenue:.2f}",
                "success_rate": f"{(len([c for c in charges.data if c.paid]) / len(charges.data) * 100):.1f}%"
            }
        except stripe.error.StripeError as e:
            return {"error": str(e)}

# Example Usage:
if __name__ == "__main__":
    processor = QuiqlyPaymentProcessor()
    
    # Create payment link for $2,499 WISeRly lifetime license
    link = processor.create_payment_link(
        "WISeRly Lifetime License",
        249900,  # $2,499.00 in cents
        {"product": "wiserly", "tier": "lifetime"}
    )
    print(f"💳 Payment Link: {link}")
    
    # Calculate fees
    fees = processor.calculate_fees(249900)
    print(f"\n💰 Fee Breakdown for $2,499 sale:")
    print(f"  Gross: ${fees['gross']:.2f}")
    print(f"  Stripe Fee ({fees['fee_percent']}): ${fees['fee']:.2f}")
    print(f"  Net to You: ${fees['net']:.2f}")
    
    # Get dashboard metrics
    metrics = processor.get_dashboard_metrics()
    print(f"\n📊 Dashboard:")
    for key, value in metrics.items():
        print(f"  {key}: {value}")
