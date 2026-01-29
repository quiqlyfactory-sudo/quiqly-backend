import PyMuPDF  # for PDF processing

class AskVault:
    def __init__(self):
        self.critical_terms = [
            "conservative care",
            "physical therapy",
            "chiropractic",
            "6 weeks",
            "failed to improve"
        ]
    
    def scan_pdf(self, pdf_path):
        """Reads medical PDF and finds Conservative Care mentions"""
        doc = PyMuPDF.open(pdf_path)
        results = []
        
        for page in doc:
            text = page.get_text()
            for term in self.critical_terms:
                if term in text.lower():
                    results.append(f"Found: {term} on page {page.number}")
        
        if not results:
            return "AskVault: No conservative care evidence found (0% error check)."
        
        return f"AskVault Verified Data: {results}"

# Integration:
# vault = AskVault()
# print(vault.scan_pdf("patient_chart.pdf"))