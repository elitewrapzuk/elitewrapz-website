#!/bin/bash

# Elite Wrapz - Quick Setup Script
# This script helps you set up and preview your new website

echo "╔═══════════════════════════════════════════════════════╗"
echo "║         Elite Wrapz Website - Setup Script           ║"
echo "║              Transform Reality | Est. 2022            ║"
echo "╚═══════════════════════════════════════════════════════╝"
echo ""

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if we're in the right directory
if [ ! -f "index.html" ]; then
    echo "❌ Error: Please run this script from the elitewrapz-new directory"
    exit 1
fi

echo "🚀 Starting setup process..."
echo ""

# Step 1: Check for images
echo "📸 Step 1: Checking for images..."
if [ -z "$(ls -A images/ 2>/dev/null | grep -v README)" ]; then
    echo "${YELLOW}⚠️  No images found in images/ directory${NC}"
    echo ""
    echo "Would you like to download images from your Wix site? (requires Python)"
    echo "1) Yes, download images now"
    echo "2) No, I'll add them manually later"
    read -p "Enter choice (1 or 2): " img_choice
    
    if [ "$img_choice" = "1" ]; then
        if command -v python3 &> /dev/null; then
            echo "Installing required Python packages..."
            pip3 install requests --quiet
            echo "Downloading images..."
            python3 download_images.py
        else
            echo "${YELLOW}⚠️  Python 3 not found. Please install Python or add images manually.${NC}"
        fi
    else
        echo "${BLUE}ℹ️  Remember to add images before deploying!${NC}"
    fi
else
    echo "${GREEN}✓ Images found!${NC}"
fi
echo ""

# Step 2: Install dependencies (if needed)
echo "📦 Step 2: Checking dependencies..."
if [ -f "package.json" ]; then
    if ! command -v npm &> /dev/null; then
        echo "${YELLOW}⚠️  npm not found. Install Node.js to use development server.${NC}"
    else
        echo "Installing npm packages..."
        npm install --silent
        echo "${GREEN}✓ Dependencies installed!${NC}"
    fi
fi
echo ""

# Step 3: Git setup
echo "🔧 Step 3: Git repository check..."
if [ -d ".git" ]; then
    echo "${GREEN}✓ Git repository initialized!${NC}"
    echo "Current commit:"
    git log -1 --oneline
else
    echo "Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit: Elite Wrapz website"
    echo "${GREEN}✓ Git repository created!${NC}"
fi
echo ""

# Step 4: Start local server
echo "🌐 Step 4: Starting local development server..."
echo ""
echo "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo "${GREEN}Your website is ready!${NC}"
echo "${GREEN}═══════════════════════════════════════════════════════${NC}"
echo ""
echo "📁 Project structure:"
echo "   ├── index.html       (Main HTML file)"
echo "   ├── css/             (Styles)"
echo "   ├── js/              (JavaScript)"
echo "   ├── images/          (Your images)"
echo "   └── README.md        (Documentation)"
echo ""
echo "🚀 To preview your site, choose an option:"
echo ""
echo "   Option 1: Simple Python server"
echo "   ${BLUE}python3 -m http.server 8000${NC}"
echo "   Then visit: http://localhost:8000"
echo ""
echo "   Option 2: PHP server (if installed)"
echo "   ${BLUE}php -S localhost:8000${NC}"
echo "   Then visit: http://localhost:8000"
echo ""
echo "   Option 3: Use npx (no installation needed)"
echo "   ${BLUE}npx serve .${NC}"
echo ""
echo "   Option 4: Live reload server"
echo "   ${BLUE}npx live-server --port=8000${NC}"
echo ""
echo "📝 Next steps:"
echo "   1. Preview your site locally"
echo "   2. Add/update images in images/ folder"
echo "   3. Customize content in index.html"
echo "   4. Test on mobile devices"
echo "   5. Deploy to hosting (see DEPLOYMENT.md)"
echo ""
echo "📚 Documentation:"
echo "   - README.md       - Project overview"
echo "   - DEPLOYMENT.md   - Deployment guide"
echo "   - images/README.md - Image setup guide"
echo ""
echo "💡 Quick tips:"
echo "   - Brand color: #01FABF (already applied)"
echo "   - Splash screen auto-plays on load"
echo "   - Fully responsive for all devices"
echo "   - SEO optimized and fast loading"
echo ""

# Ask if user wants to start server now
read -p "Would you like to start a local server now? (y/n): " start_server

if [[ $start_server =~ ^[Yy]$ ]]; then
    echo ""
    echo "Starting server..."
    
    if command -v python3 &> /dev/null; then
        echo "${GREEN}✓ Starting Python server on http://localhost:8000${NC}"
        echo "Press Ctrl+C to stop the server"
        echo ""
        python3 -m http.server 8000
    elif command -v php &> /dev/null; then
        echo "${GREEN}✓ Starting PHP server on http://localhost:8000${NC}"
        echo "Press Ctrl+C to stop the server"
        echo ""
        php -S localhost:8000
    else
        echo "${YELLOW}⚠️  No suitable server found.${NC}"
        echo "Install Python 3 or use: npx serve ."
    fi
else
    echo ""
    echo "${GREEN}Setup complete! 🎉${NC}"
    echo "Run this script again anytime to start a server."
fi
