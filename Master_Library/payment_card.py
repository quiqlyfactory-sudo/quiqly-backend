import stripe

stripe.api_key = "YOUR_STRIPE_KEY"

def create_payment_link(price, product_name):
    """Generates $2,499 checkout page"""
    link = stripe.PaymentLink.create(
        line_items=[{"price": price, "quantity": 1}]
    )
    return link.url

print(create_payment_link("price_123ABC", "WISeRly Lifetime License"))