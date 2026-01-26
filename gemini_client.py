import requests

class GeminiClient:
    def __init__(self, api_key: str, model: str = "gemini-1.5-flash"):
        self.api_key = api_key
        self.model = model
        self.endpoint = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"

    def generate(self, prompt: str) -> str:
        headers = {"Content-Type": "application/json"}
        payload = {
            "contents": [{"parts": [{"text": prompt}]}]
        }
        response = requests.post(self.endpoint, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        # Gemini returns candidates list
        return data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
