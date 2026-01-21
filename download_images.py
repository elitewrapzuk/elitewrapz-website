# Elite Wrapz - Image Download Script
# This script helps you download images from your Wix site

import requests
from pathlib import Path
import time

# Create images directory
Path("images").mkdir(exist_ok=True)

# Images found on your site (add more URLs as needed)
images = [
    {
        "url": "https://static.wixstatic.com/media/d45174_10133f6eb43944a2a1a5a4c1d214c0c5~mv2.jpeg/v1/fill/w_1612,h_1072,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/31F5E4D7-6075-46B0-A167-865957BBF185.jpeg",
        "filename": "kitchen-before-after.jpg"
    },
    {
        "url": "https://static.wixstatic.com/media/d45174_d7a6af22f12240eb9dd8e37c1fd0930d~mv2.png/v1/fill/w_49,h_49,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/NEW%20%20ELITE%20WRAPZ%20(6)%20copy_edited.png",
        "filename": "logo.png"
    },
    {
        "url": "https://static.wixstatic.com/media/d45174_c3079a3feba74bcf81d3b2d5f618ed4b~mv2.jpg/v1/fill/w_1600,h_1232,al_c,q_90,usm_0.66_1.00_0.01,enc_avif,quality_auto/modren%20light%20kitchen%20with%20wooden%20surfaces%20and%20marble%20walls_edited_edited.jpg",
        "filename": "hero-kitchen.jpg"
    },
    {
        "url": "https://static.wixstatic.com/media/11062b_0c7a0bc354214bf0adac2603e5f17053~mv2_d_5000_3333_s_4_2.jpg/v1/fill/w_147,h_98,al_c,q_80,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/Shopping%20Mall%20Escalators.jpg",
        "filename": "commercial.jpg"
    },
    {
        "url": "https://static.wixstatic.com/media/d45174_f394eb3cc1de4aff9da22db216d6c4c1~mv2.jpeg/v1/fill/w_147,h_83,al_c,q_80,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/740D7063-B368-4551-8A79-0FDE8961983A.jpeg",
        "filename": "front-desk.jpg"
    },
    {
        "url": "https://static.wixstatic.com/media/d45174_4f141b58633144e78d6c0ce5802ff01d~mv2.png/v1/fill/w_64,h_19,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/CoverStyl_Logo-qqwhtttvaeqqjys28h96to4405zo30whhvhhwkftlg.png",
        "filename": "brand-coverstyl.png"
    },
    {
        "url": "https://static.wixstatic.com/media/d45174_d4cb0271241c471499a55813b59f67a5~mv2.png/v1/fill/w_100,h_100,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/3m-di-noc-logo_edited.png",
        "filename": "brand-3m.png"
    },
    {
        "url": "https://static.wixstatic.com/media/d45174_d97dad956e454de98ac4424e8c0bae49~mv2.png/v1/fill/w_88,h_88,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/lx-hausys-logo.png",
        "filename": "brand-lx-hausys.png"
    }
]

def download_image(url, filename):
    try:
        # Remove blur parameter to get full quality
        url = url.replace('blur_2,', '')
        
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        filepath = Path("images") / filename
        with open(filepath, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"✓ Downloaded: {filename}")
        return True
    except Exception as e:
        print(f"✗ Failed to download {filename}: {str(e)}")
        return False

def main():
    print("Elite Wrapz - Image Downloader")
    print("=" * 50)
    print(f"Downloading {len(images)} images...\n")
    
    success_count = 0
    for img in images:
        if download_image(img["url"], img["filename"]):
            success_count += 1
        time.sleep(0.5)  # Be nice to the server
    
    print("\n" + "=" * 50)
    print(f"Download complete: {success_count}/{len(images)} successful")
    print("\nImages saved to: ./images/")
    print("\nNext steps:")
    print("1. Review downloaded images")
    print("2. Update image references in index.html")
    print("3. Optimize images if needed (tinypng.com)")

if __name__ == "__main__":
    main()
