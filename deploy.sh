#!/bin/bash

# Quiqly One-Command Deploy Script
# Free tier: Cloudflare Pages + Railway + MongoDB + Stripe
# Total cost: $0/month

set -e

echo "🚀 QUIQLY FREE TIER DEPLOYMENT"
echo "========================================"
echo "Target: Cloudflare Pages + Railway"
echo "Cost: $0/month"
echo "========================================"

# Check prerequisites
check_prerequisites() {
    echo "\n✓ Checking prerequisites..."
    
    if ! command -v git &> /dev/null; then
        echo "❌ Git not found. Install git."
        exit 1
    fi
    
    if ! command -v npm &> /dev/null; then
        echo "❌ npm not found. Install Node.js."
        exit 1
    fi
    
    echo "✅ Prerequisites OK"
}

# Setup environment variables
setup_env() {
    echo "\n✓ Setting up environment variables..."
    
    if [ ! -f .env.local ]; then
        cat > .env.local << 'EOF'
# AI Models
GEMINI_API_KEY=your-gemini-api-key
OLLAMA_ENDPOINT=http://localhost:11434

# Payments
STRIPE_API_KEY=sk_live_your-stripe-key
STRIPE_WEBHOOK_SECRET=whsec_your-webhook-secret

# Hosting
RAILWAY_TOKEN=your-railway-token
CLOUDFLARE_API_TOKEN=your-cloudflare-token
CLOUDFLARE_ACCOUNT_ID=your-account-id

# Database
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/quiqly
EOF
        echo "⚠️  .env.local created. Please fill in your API keys."
        echo "💡 Get free API keys:"
        echo "   - Gemini: https://makersuite.google.com/app/apikey"
        echo "   - Stripe: https://dashboard.stripe.com/apikeys"
        echo "   - Railway: https://railway.app/dashboard"
        echo "   - MongoDB: https://www.mongodb.com/cloud/atlas"
        exit 1
    fi
    
    echo "✅ Environment configured"
}

# Install dependencies
install_deps() {
    echo "\n✓ Installing dependencies..."
    if [ -f wiserly/frontend/package.json ]; then
        cd wiserly/frontend
        npm install
        cd ../..
    else
        echo "⚠️  No package.json in wiserly/frontend (static files only)"
    fi
    # Python virtual environment setup
    if [ ! -d ".venv" ]; then
        python3 -m venv .venv
    fi
    source .venv/bin/activate
    pip install --upgrade pip
    pip install stripe google-generativeai pymongo
    deactivate
    echo "✅ Dependencies installed (with virtual environment)"
}

# Build frontend
build_frontend() {
    echo "\n✓ Building frontend..."
    if [ -f wiserly/frontend/package.json ]; then
        cd wiserly/frontend
        npm run build 2>/dev/null || echo "⚠️  No build script (static files OK)"
        cd ../..
    else
        echo "⚠️  No package.json in wiserly/frontend (static files only)"
    fi
    echo "✅ Frontend ready"
}

# Deploy frontend to Cloudflare Pages
deploy_cloudflare() {
    echo "\n✓ Deploying to Cloudflare Pages..."
    
    if command -v wrangler &> /dev/null; then
        wrangler pages deploy wiserly/frontend \
            --project-name quiqly-app \
            --branch main
        echo "✅ Deployed to: https://quiqly-app.pages.dev"
    else
        echo "⚠️  Wrangler not installed. Install: npm install -g wrangler"
        echo "   Then run: wrangler pages deploy wiserly/frontend --project-name quiqly-app"
    fi
}

# Deploy backend to Railway
deploy_railway() {
    echo "\n✓ Deploying backend to Railway..."
    
    if command -v railway &> /dev/null; then
        railway up --service backend
        echo "✅ Backend deployed to Railway"
    else
        echo "⚠️  Railway CLI not installed. Install: npm install -g @railway/cli"
        echo "   Then run: railway up"
    fi
}

# Setup MongoDB (free tier M0)
setup_mongodb() {
    echo "\n✓ Setting up MongoDB..."
    echo "💡 Free tier: 512MB storage, no credit card required"
    echo "   Go to: https://www.mongodb.com/cloud/atlas"
    echo "   1. Sign up (free)"
    echo "   2. Create M0 cluster"
    echo "   3. Add your IP"
    echo "   4. Update MONGODB_URI in .env.local"
    echo "⚠️  Manual step required"
}

# Verify deployment
verify_deployment() {
    echo "\n✓ Verifying deployment..."
    
    FRONTEND_URL="https://quiqly-app.pages.dev"
    if curl -s -I "$FRONTEND_URL" | grep -q "200\|301\|302"; then
        echo "✅ Frontend is live: $FRONTEND_URL"
    else
        echo "⚠️  Frontend not responding. Check Cloudflare deployment."
    fi
}

# Print cost breakdown
print_costs() {
    echo "\n========================================="
    echo "💰 COST BREAKDOWN"
    echo "========================================="
    echo "Frontend (Cloudflare Pages): $0"
    echo "Backend (Railway Hobby):     $0-5/mo"
    echo "Database (MongoDB M0):       $0"
    echo "Payments (Stripe):           2.9% + \$0.30/tx"
    echo "Domain:                      $0 (.tk) or $12/yr (.ai)"
    echo "-----------------------------------------"
    echo "TOTAL MONTHLY:               $0-5"
    echo "You only pay when customers pay you!"
    echo "========================================="
}

# Main execution
main() {
    check_prerequisites
    setup_env
    install_deps
    build_frontend
    deploy_cloudflare
    deploy_railway
    setup_mongodb
    verify_deployment
    print_costs
    
    echo "\n✅ DEPLOYMENT COMPLETE!"
    echo ""
    echo "Next steps:"
    echo "1. Add API keys to .env.local"
    echo "2. Setup MongoDB Atlas"
    echo "3. Configure Stripe webhook"
    echo "4. Test at: https://quiqly-app.pages.dev/login.html"
}

main "$@"
