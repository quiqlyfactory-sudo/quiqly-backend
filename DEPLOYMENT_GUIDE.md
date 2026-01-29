# How to Deploy WISeRly to a Website

## Option 1: Local Testing (Right Now)

### View Login Page
```bash
cd /home/wisely/quiqly/wiserly/frontend
# Then open in browser:
# file:///home/wisely/quiqly/wiserly/frontend/login.html
```

**Demo Credentials:**
- Username: `admin`
- Password: `Qly$012026`

After login, you'll see the dashboard at `dashboard.html`

---

## Option 2: Deploy to Free Hosting

### Using Netlify (Easiest - Free)

1. **Push to GitHub**
```bash
cd /home/wisely/quiqly
git init
git add .
git commit -m "Quiqly platform with 4 intelligences"
git remote add origin https://github.com/YOUR_USERNAME/quiqly.git
git push -u origin main
```

2. **Connect to Netlify**
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Select your GitHub repo
   - Set build command: (leave blank - it's static HTML)
   - Set publish directory: `wiserly/frontend`
   - Deploy!

Your site will be live at: `https://YOUR-SITE-NAME.netlify.app/login.html`

---

### Using GitHub Pages (Also Free)

1. **Push to GitHub** (see above)

2. **Enable GitHub Pages**
   - Go to repo Settings → Pages
   - Select "Deploy from branch"
   - Branch: `main`, Folder: `/wiserly/frontend`
   - Save

Your site will be live at: `https://YOUR_USERNAME.github.io/quiqly/wiserly/frontend/login.html`

---

### Using Vercel (Free & Fast)

1. **Push to GitHub**

2. **Go to [vercel.com](https://vercel.com)**
   - Click "New Project"
   - Import from GitHub
   - Root Directory: `wiserly/frontend`
   - Deploy!

Your site will be live at: `https://quiqly-RANDOM.vercel.app/login.html`

---

## Option 3: Deploy to Your Own Server

### Using AWS S3 + CloudFront (Cheap - $1-5/month)

```bash
# Install AWS CLI
pip install awscli

# Configure AWS
aws configure

# Create S3 bucket
aws s3 mb s3://wiserly-platform --region us-east-1

# Upload files
aws s3 sync wiserly/frontend s3://wiserly-platform --acl public-read

# Set index.html as default
aws s3 website s3://wiserly-platform --index-document login.html
```

Your site: `http://wiserly-platform.s3-website-us-east-1.amazonaws.com`

---

### Using Heroku (Also Free with restrictions)

1. Create `Procfile`:
```
web: python -m http.server $PORT
```

2. Push to Heroku:
```bash
heroku login
heroku create wiserly-app
git push heroku main
```

Your site: `https://wiserly-app.herokuapp.com/wiserly/frontend/login.html`

---

## Option 4: Docker (For Production)

### Create Dockerfile

```dockerfile
FROM nginx:alpine
COPY wiserly/frontend /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

### Build & Deploy

```bash
docker build -t wiserly-app .
docker run -p 80:80 wiserly-app
```

Visit: `http://localhost/login.html`

---

## Files You Have

| File | Purpose |
|---|---|
| `login.html` | Login page (admin / Qly$012026) |
| `dashboard.html` | Dashboard after login |
| `index.html` | Landing page |
| `theme.css` | Carbon Mint design system |

---

## Quick Links for Deployment

| Platform | Cost | Time | Link |
|---|---|---|---|
| **Netlify** | FREE | 2 min | https://netlify.com |
| **Vercel** | FREE | 2 min | https://vercel.com |
| **GitHub Pages** | FREE | 5 min | https://pages.github.com |
| **AWS S3** | $1-5/mo | 10 min | https://aws.amazon.com |
| **Heroku** | FREE | 5 min | https://heroku.com |

---

## My Recommendation

**For Quick Demo:**
1. Push to GitHub
2. Deploy to Netlify (fastest)
3. Share link with team

**Then:** 
- Add SSL certificate (automatic on Netlify/Vercel)
- Connect real backend APIs (Stripe, Mercury, etc.)
- Add PDF upload functionality

---

## Test Locally First

```bash
# If you have Python
cd /home/wisely/quiqly/wiserly/frontend
python -m http.server 8000

# Then visit:
# http://localhost:8000/login.html
```

---

## Next Steps

1. ✅ You have working login/dashboard pages
2. → Choose a deployment option (Netlify = easiest)
3. → Connect to real backend
4. → Add PDF upload to AskVault
5. → Integrate real APIs (Stripe, Mercury, etc.)

All pages work **locally right now**. You just need to pick a deployment platform!
