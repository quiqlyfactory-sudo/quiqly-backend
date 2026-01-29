from marketing_forge import MarketingForge

forge = MarketingForge(elevenlabs_key="YOUR_KEY")

# Generate first video
script = forge.generate_viral_script("Conservative Care auditing")
video = forge.render_digital_twin(script, avatar="Sovereign_Founder_V2")
forge.broadcast_to_social(video)
