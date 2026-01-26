import requests

class OllamaClient:
    def __init__(self, endpoint: str):
        self.endpoint = endpoint.rstrip('/')

    def generate(self, prompt: str, model: str = "mistral:latest") -> str:
        url = f"{self.endpoint}/api/generate"
        payload = {
            "model": model,
            "prompt": prompt
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "")
