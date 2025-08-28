# 📷 Post on Instagram via Python

This project demonstrates how to publish a post on **Instagram** using Python and the **Instagram Graph API**.

---

⚙️ Setup Instructions

1. Install dependencies:
   pip install requests python-dotenv

2. Configure environment variables:
   Create a file named .env based on env.example.txt and update with your credentials:

   INSTAGRAM_ACCESS_TOKEN=your_long_lived_access_token
   INSTAGRAM_USER_ID=your_instagram_business_or_creator_id
   IMAGE_URL=https://example.com/sample.jpg

3. Run the script:
   python3 post_instagram.py

---

📜 Example Script (post_instagram.py)

import os
import requests
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN = os.getenv("INSTAGRAM_ACCESS_TOKEN")
USER_ID = os.getenv("INSTAGRAM_USER_ID")
IMAGE_URL = os.getenv("IMAGE_URL")

def post_image(caption):
    url = f"https://graph.facebook.com/v19.0/{USER_ID}/media"
    payload = {
        "image_url": IMAGE_URL,
        "caption": caption,
        "access_token": ACCESS_TOKEN
    }
    response = requests.post(url, data=payload)
    result = response.json()

    if "id" in result:
        creation_id = result["id"]
        publish_url = f"https://graph.facebook.com/v19.0/{USER_ID}/media_publish"
        publish_payload = {
            "creation_id": creation_id,
            "access_token": ACCESS_TOKEN
        }
        publish_response = requests.post(publish_url, data=publish_payload)
        if publish_response.status_code == 200:
            print("✅ Successfully posted to Instagram!")
        else:
            print("❌ Failed to publish:", publish_response.json())
    else:
        print("❌ Upload failed:", result)

if __name__ == "__main__":
    post_image("Hello Instagram! 🚀 #Python #Automation")

---

📌 Notes
- Requires a **Business or Creator Instagram account** linked to a **Facebook Page**.
- Needs a valid **Long-Lived Access Token** with `instagram_basic` and `pages_show_list` permissions.
- Can be extended to post videos, carousels, or scheduled content.
