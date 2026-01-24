#!/usr/bin/env python3
import re
import glob

# Mapping of old URLs to new URLs
url_map = {
    'href="../index.html"': 'href="/"',
    'href="what-we-wrap.html"': 'href="/whatwewrap/"',
    'href="our-work.html"': 'href="/ourwork/"',
    'href="payment-plans.html"': 'href="/paymentplans/"',
    'href="areas-we-serve.html"': 'href="/areasweserve/"',
    'href="faq.html"': 'href="/faq/"',
    'href="contact.html"': 'href="/contact/"',
    'href="get-a-quote.html"': 'href="/getaquote/"',
    'href="privacy-policy.html"': 'href="/privacypolicy/"',
    'href="terms-and-conditions.html"': 'href="/termsandconditions/"',
    'href="locations/birmingham-vinyl-wrapping.html"': 'href="/birminghamvinylwrapping/"',
    'href="locations/solihull-vinyl-wrapping.html"': 'href="/solihullvinylwrapping/"',
}

# Files to update
files = [
    "ourwork/index.html",
    "paymentplans/index.html",
    "areasweserve/index.html",
    "faq/index.html",
    "contact/index.html",
    "getaquote/index.html",
    "privacypolicy/index.html",
    "termsandconditions/index.html",
    "birminghamvinylwrapping/index.html",
    "solihullvinylwrapping/index.html",
]

for file_path in files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Apply all replacements
        for old_url, new_url in url_map.items():
            content = content.replace(old_url, new_url)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Updated: {file_path}")
    except Exception as e:
        print(f"Error updating {file_path}: {e}")

print("All files updated!")
