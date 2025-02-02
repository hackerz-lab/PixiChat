import os
import requests
import pywhatkit as kit
from datetime import datetime
import time

# Replace with your Stability AI API key
STABILITY_API_KEY = "YOUR_API_KEY"

def generate_image(prompt):
    url = "https://api.stability.ai/v2beta/stable-image/generate/sd3"
    headers = {
        "Authorization": f"Bearer {STABILITY_API_KEY}",
        "Accept": "image/*"
    }
    
    response = requests.post(
        url,
        headers=headers,
        files={"none": ''},
        data={
            "prompt": prompt,
            "output_format": "png",
        },
    )
    
    if response.status_code == 200:
        image_path = "generated_image.png"
        with open(image_path, "wb") as f:
            f.write(response.content)
        return image_path
    else:
        print("Error:", response.text)
        return None

def send_image_via_whatsapp(image_path, prompt):
    now = datetime.now()
    hour = now.hour
    minute = now.minute + 1  # Schedule 1 minute ahead
    
    # Replace with your target number (include country code, e.g., +1234567890)
    target_number = "+1234567890"
    
    try:
        kit.sendwhats_image(
            receiver=target_number,
            img_path=image_path,
            caption=prompt,
            wait_time=15
        )
        time.sleep(10)
        print("Image sent!")
    except Exception as e:
        print("Error sending image:", e)

if __name__ == "__main__":
    prompt = input("Enter your text prompt: ")
    image_path = generate_image(prompt)
    if image_path:
        send_image_via_whatsapp(image_path, prompt)
