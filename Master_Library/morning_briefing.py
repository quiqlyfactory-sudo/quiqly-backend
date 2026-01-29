def generate_briefing():
    askvault_stats = "3 new PDFs processed (100% accuracy)"
    forge_stats = "LinkedIn video: 5k views"

    briefing = f"""
    Good morning. Here's your Quiqly status:

    💰 Sales: Stripe earned $1,200 this week. 1 pending invoice.
    📧 Mail: 1 new letter from IRS - filed digitally in 'Legal' silo.
    🎥 Marketing: Your video is trending with {forge_stats}.
    🔒 AskVault: {askvault_stats}.
    """
    return briefing

print(generate_briefing())
