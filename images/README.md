# Images Directory

Place your website images here.

## Required Images:

1. **logo.png** - Your Elite Wrapz logo (transparent background recommended)
2. **hero-kitchen.jpg** - Main hero section background
3. **kitchen-before-after.jpg** - Kitchen transformation showcase
4. **commercial.jpg** - Commercial property example
5. **front-desk.jpg** - Office/desk wrapping example
6. **brand-3m.png** - 3M DI-NOC logo
7. **brand-coverstyl.png** - Coverstyl logo
8. **brand-lx-hausys.png** - LX Hausys logo
9. **icon-192.png** - App icon (192x192px)
10. **icon-512.png** - App icon (512x512px)

## How to Get Images:

### Option 1: Download from Wix (Easiest)
Run the Python script:
```bash
pip install requests
python download_images.py
```

### Option 2: Manual Download
1. Visit your current Wix site
2. Right-click on images
3. Save image as...
4. Place in this folder

### Option 3: Use Browser DevTools
1. Open www.elitewrapz.uk in Chrome
2. Press F12 (DevTools)
3. Go to Network tab
4. Refresh page
5. Filter by "Img"
6. Right-click image URLs and download

## Image Optimization Tips:

- **Compress images** using [TinyPNG](https://tinypng.com)
- **Target size**: < 200KB per image
- **Use WebP format** for better compression (with JPG/PNG fallback)
- **Dimensions**: 
  - Hero images: 1920x1080px
  - Service images: 800x600px
  - Logos: Keep original size
  - Icons: 192x192 and 512x512

## After Adding Images:

Update the `index.html` file to reference your images:

```html
<!-- Example -->
<img src="images/logo.png" alt="Elite Wrapz Logo" width="150" height="150">
```

## WebP Conversion (Optional):

```bash
# Install cwebp (on macOS)
brew install webp

# Convert images
cwebp -q 80 hero-kitchen.jpg -o hero-kitchen.webp
```

Then use picture element:
```html
<picture>
  <source srcset="images/hero-kitchen.webp" type="image/webp">
  <img src="images/hero-kitchen.jpg" alt="Kitchen">
</picture>
```
