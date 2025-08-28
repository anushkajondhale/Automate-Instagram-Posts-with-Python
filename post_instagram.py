import os
import requests
from dotenv import load_dotenv

# Load environment variables
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

        # Publish the media
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
