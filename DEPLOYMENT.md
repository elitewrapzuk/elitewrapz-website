# Elite Wrapz Website - Deployment Guide

## 🚀 Quick Deploy Options

### Option 1: Netlify (Recommended - Easiest)

1. **Push to GitHub**
   ```bash
   cd /tmp/elitewrapz-new
   git init
   git add .
   git commit -m "Initial commit - Elite Wrapz website"
   git branch -M main
   git remote add origin https://github.com/yourusername/elitewrapz.git
   git push -u origin main
   ```

2. **Deploy on Netlify**
   - Go to [netlify.com](https://netlify.com)
   - Click "Add new site" → "Import an existing project"
   - Connect to GitHub and select your repo
   - Click "Deploy site"
   - Your site will be live in seconds!

3. **Custom Domain**
   - In Netlify dashboard: Domain settings → Add custom domain
   - Point your domain's DNS to Netlify:
     - A record: `75.2.60.5`
     - Or CNAME: `your-site.netlify.app`

### Option 2: Vercel

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Deploy**
   ```bash
   cd /tmp/elitewrapz-new
   vercel
   ```

3. **Follow prompts** and your site is live!

### Option 3: GitHub Pages (Free)

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin YOUR_REPO_URL
   git push -u origin main
   ```

2. **Enable GitHub Pages**
   - Go to repo Settings → Pages
   - Source: Deploy from branch
   - Branch: main / (root)
   - Save

3. **Your site will be at**: `https://yourusername.github.io/elitewrapz/`

### Option 4: Cloudflare Pages

1. Go to [pages.cloudflare.com](https://pages.cloudflare.com)
2. Connect GitHub repo
3. Deploy (automatic)
4. Free SSL and CDN included!

## 📝 Before Deployment Checklist

- [ ] Download images using `python download_images.py`
- [ ] Update image paths in HTML
- [ ] Test on mobile devices
- [ ] Verify contact information
- [ ] Check all links work
- [ ] Test form submissions (if added)
- [ ] Optimize images (compress)
- [ ] Update meta descriptions
- [ ] Add favicon
- [ ] Test page load speed

## 🖼️ Image Setup

1. **Download your images**:
   ```bash
   pip install requests
   python download_images.py
   ```

2. **Optimize images**:
   - Use [TinyPNG](https://tinypng.com) or [Squoosh](https://squoosh.app)
   - Aim for < 200KB per image
   - Use WebP format when possible

3. **Update HTML**:
   Replace image placeholders with actual paths:
   ```html
   <img src="images/logo.png" alt="Elite Wrapz Logo">
   ```

## 🔧 Performance Optimization

### 1. Minify CSS & JS (before production)
```bash
npm install -g minify
minify css/styles.css > css/styles.min.css
minify js/script.js > js/script.min.js
```

Update HTML to use minified versions.

### 2. Enable Compression
Most hosting providers (Netlify, Vercel) do this automatically.

### 3. Add Service Worker (PWA)
Create `sw.js` for offline functionality (optional).

## 📊 Analytics Setup

### Google Analytics 4
Add before `</head>`:
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

## 🔒 Security Headers (Netlify)

Create `netlify.toml`:
```toml
[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    X-XSS-Protection = "1; mode=block"
    Referrer-Policy = "strict-origin-when-cross-origin"
```

## 🎯 SEO Setup

1. **Google Search Console**
   - Add your site
   - Submit sitemap (create sitemap.xml)
   - Monitor indexing

2. **Bing Webmaster Tools**
   - Similar to Google Search Console

3. **Local SEO**
   - Add to Google My Business
   - Get listed in local directories

## 📱 Testing

Test your site on:
- Mobile devices (iOS & Android)
- Different browsers
- Different screen sizes
- PageSpeed Insights
- Mobile-Friendly Test

## 🆘 Troubleshooting

**Images not loading?**
- Check file paths are correct
- Ensure images are in the correct folder
- Check file permissions

**Site not loading?**
- Clear browser cache
- Check DNS settings
- Verify hosting service is active

**Animations not working?**
- Check JavaScript console for errors
- Ensure script.js is loaded
- Test in different browsers

## 📞 Support

For issues or questions:
- Email: contact@elitewrapz.uk
- Phone: 07424 088434

## 🎉 Go Live!

Once deployed, share your new site:
- Update business cards
- Update social media profiles
- Submit to search engines
- Tell your customers!

---

**Your new site is faster, more powerful, and looks amazing! 🚀**
