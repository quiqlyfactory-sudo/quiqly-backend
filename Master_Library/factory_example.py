# Recursive Library in Action
# Example: Cloning WISeRly Security for Software #3

from quiqly_core.factory import QuiqlyFactory

# After building WISeRly, you've harvested the security module
factory = QuiqlyFactory()

# Now you want to start "LegalVault" (Software #3)
factory.spawn_new_software("LegalVault")

# Quiqly automatically copies:
# - SecurityVault.py (AskVault logic)
# - payment_card.py (Stripe integration)
# - identity_setup.py (Domain/email config)
# - marketing_forge.py (Content generation)

# You only need to add the NEW logic specific to LegalVault
# The foundation is instant.
