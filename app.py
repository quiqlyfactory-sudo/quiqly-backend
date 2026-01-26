from flask import Flask, request, jsonify
import os
from ollama_client import OllamaClient
from gemini_client import GeminiClient

app = Flask(__name__)

# Demo user for login
DEMO_USER = {
    "username": "admin",
    "password": "Qly$012026",
    "token": "demo-token-123"
}

# Choose LLM client (Ollama or Gemini)
def get_llm_client():
    try:
        return OllamaClient(os.getenv("OLLAMA_ENDPOINT", "http://localhost:11434"))
    except Exception:
        return GeminiClient(os.getenv("GEMINI_API_KEY"))

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username == DEMO_USER["username"] and password == DEMO_USER["password"]:
        return jsonify({
            "success": True,
            "session": {
                "username": username,
                "token": DEMO_USER["token"]
            }
        })
    return jsonify({"success": False, "message": "Invalid username or password."}), 401

@app.route("/dashboard", methods=["GET"])
def dashboard():
    auth = request.headers.get("Authorization", "").replace("Bearer ", "")
    if auth != DEMO_USER["token"]:
        return jsonify({"error": "Unauthorized"}), 401
    # Example: Use LLM to generate a dashboard message
    llm = get_llm_client()
    prompt = "Generate a short compliance tip for medical professionals."
    try:
        tip = llm.generate(prompt)
    except Exception:
        tip = "Stay compliant!"
    # Return demo dashboard data
    return jsonify({
        "pdfsProcessed": 47,
        "pdfsProcessedChange": "↑ 12 this week",
        "complianceScore": "99.2%",
        "complianceScoreChange": "↑ 0.5% from last month",
        "revenueThisMonth": "$24,990",
        "activeUsers": "10 active users",
        "systemUptime": "100%",
        "incidents": "0 incidents",
        "activity": [
            {"time": "Today at 9:45 AM", "description": "✅ AskVault completed scan of 3 medical PDFs"},
            {"time": "Today at 8:30 AM", "description": "🚀 Morning briefing generated and sent"},
            {"time": "Yesterday at 11:20 PM", "description": "💰 Revenue alert: $2,499 payment received"},
            {"time": "Yesterday at 3:15 PM", "description": "🛡️ ComplianceShield audit passed (HIPAA compliant)"},
            {"time": "2 days ago at 10:00 AM", "description": "🎥 MarketingForge published new video to LinkedIn"},
            {"time": "LLM Tip", "description": tip}
        ]
    })

@app.route("/", methods=["GET"])
def index():
    return "Quiqly API is running."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
