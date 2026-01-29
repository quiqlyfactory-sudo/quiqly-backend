# How to Get Free API Keys for Quiqly

All free tier. No credit card required for most.

---

## 1. Gemini API Key (Free: 1.5M tokens/day)

**Step 1: Go to Google AI Studio**
```
https://makersuite.google.com/app/apikey
```

**Step 2: Click "Create API Key"**
- Select "Create API key in new Google Cloud project"
- Or use existing project

**Step 3: Copy your key**
- Key format: `AIzaSy...` (starts with AIzaSy)

**Step 4: Add to `.env.local`**
```
GEMINI_API_KEY=AIzaSy...
```

✅ Free: 1.5M free tokens/day (usually enough for 1 user)

---

## 2. Stripe API Key (No upfront cost, 2.9% + $0.30 per transaction)

**Step 1: Create Stripe Account**
```
https://dashboard.stripe.com/register
```

**Step 2: Complete onboarding**
- Business info
- Bank account for deposits
- Identity verification

**Step 3: Get API keys**
- Go to: https://dashboard.stripe.com/apikeys
- Copy **Secret Key** (starts with `sk_live_...` or `sk_test_...`)

**Step 4: Get Webhook Secret** (for accepting payments)
- Go to: https://dashboard.stripe.com/webhooks
- Create endpoint to your backend
- Copy webhook signing secret

**Step 5: Add to `.env.local`**
```
STRIPE_API_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...
```

✅ Free to sign up, only pay per transaction (2.9% + $0.30)

**Test Mode vs Live Mode:**
- Test: Use `sk_test_...` keys (fake transactions)
- Live: Use `sk_live_...` keys (real money)

---

## 3. Railway Token (Free tier available)

**Step 1: Create Railway Account**
```
https://railway.app/register
```

**Step 2: Connect GitHub** (recommended)
- Easier deployments

**Step 3: Generate API Token**
- Go to: https://railway.app/dashboard/settings
- Click "API Tokens"
- Create new token
- Copy token

**Step 4: Add to `.env.local`**
```
RAILWAY_TOKEN=your-railway-token
```

✅ Free tier: 512 MB RAM, $5/month after free credits

---

## 4. Cloudflare API Token (Free tier available)

**Step 1: Create Cloudflare Account**
```
https://dash.cloudflare.com/sign-up
```

**Step 2: Get API Token**
- Go to: https://dash.cloudflare.com/profile/api-tokens
- Click "Create Token"
- Select "Custom token"
- Permissions:
  - Account → Cloudflare Pages → Edit
  - Zone → Zone Settings → Read

**Step 3: Copy token and Account ID**
- Token: starts with `v1.0_...`
- Account ID: found at https://dash.cloudflare.com/

**Step 4: Add to `.env.local`**
```
CLOUDFLARE_API_TOKEN=v1.0_...
CLOUDFLARE_ACCOUNT_ID=your-account-id
```

✅ Free: Unlimited static site hosting on Cloudflare Pages

---

## 5. MongoDB Connection String (Free tier M0)

**Step 1: Create MongoDB Atlas Account**
```
https://www.mongodb.com/cloud/atlas/register
```

**Step 2: Create Cluster**
- Click "Create a Deployment"
- Select M0 (Free)
- Choose region (closest to you)
- Click "Create Cluster"

**Step 3: Add IP Address**
- Go to: "Security" → "Network Access"
- Click "Add IP Address"
- Choose "Allow access from anywhere" (0.0.0.0/0)
- Confirm

**Step 4: Create Database User**
- Go to: "Security" → "Database Access"
- Click "Add New Database User"
- Username: `admin`
- Password: Generate secure password
- Click "Add User"

**Step 5: Get Connection String**
- Go to: "Deployment" → "Drivers"
- Select "Node.js"
- Copy connection string
- Replace `<username>` and `<password>` with your credentials

**Step 6: Add to `.env.local`**
```
MONGODB_URI=mongodb+srv://admin:PASSWORD@cluster.mongodb.net/quiqly?retryWrites=true&w=majority
```

✅ Free: 512MB storage, no credit card required

---

## 6. OpenRouter API Key (Fallback, pay-as-you-go)

**Only needed if Gemini free tier runs out**

**Step 1: Go to OpenRouter**
```
https://openrouter.ai/keys
```

**Step 2: Create Account**
- Sign up with email or GitHub

**Step 3: Generate API Key**
- Go to: https://openrouter.ai/keys
- Create new key
- Copy key

**Step 4: Add to `.env.local`**
```
OPENROUTER_KEY=sk-or-...
```

✅ Free to sign up, pay per API call (backup only)

---

## Quick Setup (5 minutes)

```bash
# 1. Create .env.local
cp .env.example .env.local

# 2. Get Gemini key
# https://makersuite.google.com/app/apikey

# 3. Get Stripe keys
# https://dashboard.stripe.com/apikeys

# 4. Get Railway token
# https://railway.app/dashboard/settings

# 5. Get Cloudflare token
# https://dash.cloudflare.com/profile/api-tokens

# 6. Get MongoDB connection string
# https://cloud.mongodb.com/

# 7. Fill in .env.local with all keys

# 8. Deploy
bash deploy.sh
```

---

## Complete `.env.local` Template

```env
# AI Models
GEMINI_API_KEY=AIzaSy...
OLLAMA_ENDPOINT=http://localhost:11434
OPENROUTER_KEY=sk-or-...

# Payments
STRIPE_API_KEY=sk_live_...
STRIPE_WEBHOOK_SECRET=whsec_...

# Hosting
RAILWAY_TOKEN=your-railway-token
CLOUDFLARE_API_TOKEN=v1.0_...
CLOUDFLARE_ACCOUNT_ID=your-account-id

# Database
MONGODB_URI=mongodb+srv://admin:PASSWORD@cluster.mongodb.net/quiqly

# Optional
WHATNOT_TOKEN=your-whatnot-token
EBAY_KEY=your-ebay-key
AMAZON_KEY=your-amazon-key
```

---

## Cost Summary

| Service | Cost | Limits |
|---|---|---|
| **Gemini 1.5 Flash** | Free | 1.5M tokens/day |
| **Stripe** | 2.9% + $0.30 | Unlimited transactions |
| **Railway** | Free | 512 MB, then $5/mo |
| **Cloudflare Pages** | Free | Unlimited sites |
| **MongoDB Atlas** | Free | 512 MB storage |
| **OpenRouter** | Pay-as-you-go | Backup only |
| **TOTAL** | **$0/month** | **Pay on revenue** |

---

## Verification

After adding all keys to `.env.local`:

```bash
# Test Gemini
python -c "import os; print('✅ GEMINI_API_KEY found') if os.getenv('GEMINI_API_KEY') else print('❌ Missing')"

# Test Stripe
python -c "import os; print('✅ STRIPE_API_KEY found') if os.getenv('STRIPE_API_KEY') else print('❌ Missing')"

# Test MongoDB
python -c "import os; print('✅ MONGODB_URI found') if os.getenv('MONGODB_URI') else print('❌ Missing')"
```

---

## Troubleshooting

**Q: "Free tier" requires credit card?**
A: Only Stripe and Railway might ask. They're legitimate companies and won't charge without authorization.

**Q: How much will this actually cost?**
A: $0/month until you make revenue. First $1,000 in sales = ~$970 profit after Stripe fees.

**Q: Can I use test keys?**
A: Yes! Use `sk_test_...` keys from Stripe to test before going live.

**Q: What if I exceed free tier limits?**
A: Add OpenRouter fallback or upgrade to paid plan. But first 100 customers will be on free tier.

---

## Next Steps

1. ✅ Get all 6 API keys
2. ✅ Fill in `.env.local`
3. ✅ Run `bash deploy.sh`
4. ✅ Your site is live!

**Questions?** Check [config.py](../config.py)
