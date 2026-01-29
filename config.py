# Quiqly Configuration: Free/Cheapest AI Factory

import os
from typing import Dict

class QuiqlyConfig:
    """Global config for free-tier Quiqly deployment"""
    
    # ====================
    # AI MODEL STRATEGY
    # ====================
    # PRIMARY: Ollama (local, free, infinite)
    # FALLBACK: Gemini 1.5 Flash (free tier: 1.5M tokens/day)
    # OVERFLOW: OpenRouter fallback if needed
    
    AI_CONFIG = {
        "primary": {
            "type": "ollama",
            "endpoint": "http://localhost:11434",
            "model": "mistral:latest",  # Free, fast, multimodal
            "cost": "$0"
        },
        "fallback": {
            "type": "gemini",
            "api_key": os.getenv("GEMINI_API_KEY"),
            "model": "gemini-1.5-flash",
            "free_limit": "1.5M tokens/day",
            "cost": "$0 (free tier)"
        },
        "overflow": {
            "type": "openrouter",
            "api_key": os.getenv("OPENROUTER_KEY"),
            "model": "openrouter/auto",
            "cost": "pay-as-you-go (fallback only)"
        }
    }
    
    # ====================
    # HOSTING STRATEGY
    # ====================
    # FRONTEND: Cloudflare Pages (free, global CDN)
    # BACKEND: Railway (free tier or $5/mo hobby)
    # DATABASE: MongoDB Atlas (free tier: 512MB)
    
    HOSTING_CONFIG = {
        "frontend": {
            "platform": "cloudflare_pages",
            "repo": "your-github-repo",
            "build_command": "cd wiserly/frontend && npm run build",
            "publish_dir": "wiserly/frontend",
            "cost": "$0"
        },
        "backend": {
            "platform": "railway",
            "dyno_type": "hobby",
            "auto_scale": False,
            "cost": "$0 (free tier) or $5/mo (hobby)"
        },
        "database": {
            "platform": "mongodb_atlas",
            "tier": "M0",
            "storage": "512MB",
            "cost": "$0"
        }
    }
    
    # ====================
    # PAYMENT STRATEGY
    # ====================
    # STRIPE ONLY: 2.9% + 30¢
    # NO MONTHLY FEES, NO HIDDEN COSTS
    # Mercury = add later when revenue > $10k/month
    
    PAYMENT_CONFIG = {
        "primary": {
            "provider": "stripe",
            "api_key": os.getenv("STRIPE_API_KEY"),
            "fee": "2.9% + $0.30 per transaction",
            "cost": "$0 upfront"
        },
        "add_later": {
            "provider": "mercury",
            "tier": "tier_when_revenue_high",
            "cost": "Only when profitable"
        }
    }
    
    # ====================
    # TOTAL COST BREAKDOWN
    # ====================
    MONTHLY_COST = {
        "ai_models": "$0 (Ollama free + Gemini free tier)",
        "hosting": "$0-5 (Cloudflare free + Railway hobby)",
        "database": "$0 (MongoDB free tier)",
        "payments": "$0 upfront (pay on each transaction)",
        "domain": "$12/year (or free .tk domain)",
        "total_first_month": "$0",
        "total_monthly": "$0-5"
    }
    
    @staticmethod
    def get_ai_client():
        """Get AI client with fallback logic"""
        try:
            # Try Ollama first (local, free, always available)
            from ollama_client import OllamaClient
            return OllamaClient(QuiqlyConfig.AI_CONFIG["primary"]["endpoint"])
        except:
            try:
                # Fallback to Gemini 1.5 Flash (free tier)
                from gemini_client import GeminiClient
                return GeminiClient(QuiqlyConfig.AI_CONFIG["fallback"]["api_key"])
            except:
                # Last resort: OpenRouter
                from openrouter_client import OpenRouterClient
                return OpenRouterClient(QuiqlyConfig.AI_CONFIG["overflow"]["api_key"])
    
    @staticmethod
    def print_cost_breakdown():
        """Print free tier strategy"""
        print("\n" + "="*60)
        print("QUIQLY: FREE/CHEAPEST NON-HUMAN AI FACTORY")
        print("="*60)
        print("\n🎯 MONTHLY COST: $0-5\n")
        print("AI Models:")
        print("  • Ollama (local): $0")
        print("  • Gemini 1.5 Flash (free tier): $0")
        print("  • Fallback via OpenRouter: pay-as-you-go\n")
        print("Hosting:")
        print("  • Cloudflare Pages (frontend): $0")
        print("  • Railway Hobby (backend): $0-5/mo\n")
        print("Database:")
        print("  • MongoDB Atlas (M0): $0\n")
        print("Payments:")
        print("  • Stripe: 2.9% + $0.30 (no monthly fee)\n")
        print("Domain:")
        print("  • .tk domain: $0 (free)")
        print("  • .ai domain: $12/year\n")
        print("="*60)
        print("TOTAL: $0/month operating cost")
        print("Revenue model: Only pay when customers pay you")
        print("="*60 + "\n")

if __name__ == "__main__":
    QuiqlyConfig.print_cost_breakdown()
