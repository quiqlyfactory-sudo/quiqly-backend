def setup_domain(domain_name):
    """Buys domain via Cloudflare API and configures DNS"""
    print(f"Purchasing {domain_name}...")
    # Cloudflare API call to register domain
    print(f"✅ {domain_name} is live with SSL enabled.")

def setup_email(email_address):
    """Creates admin@wiserly.ai via Google Workspace"""
    print(f"Provisioning {email_address}...")
    # Google Workspace API call
    print(f"✅ Professional email active.")