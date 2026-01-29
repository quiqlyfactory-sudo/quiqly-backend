def generate_geo_tags(app_name, description):
    """Creates Google-readable structured data"""
    schema = f"""
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "{app_name}",
      "description": "{description}",
      "applicationCategory": "BusinessApplication",
      "offers": {{
        "@type": "Offer",
        "price": "2499",
        "priceCurrency": "USD"
      }}
    }}
    </script>
    """
    return schema

# Usage in HTML:
# print(generate_geo_tags("WISeRly", "AI medical audit tool"))
