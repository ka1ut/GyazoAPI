import requests
import os
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()

ACCESS_TOKEN=os.getenv("GYAZO_ACCESS_TOKEN")
URL="https://upload.gyazo.com/api/upload"  

def pil_to_binary(pil_img, format="JPEG"):
    if pil_img.mode == "RGBA" and format == "JPEG":
        pil_img = pil_img.convert("RGB")
    buffered = io.BytesIO()
    pil_img.save(buffered, format=format)
    return buffered.getvalue()

def singleUpload(img, description):
    headers = {'Authorization': "Bearer {}".format(ACCESS_TOKEN)}
    img_binary = pil_to_binary(img)
    files = {'imagedata': ('image.jpg', img_binary, 'image/jpeg')}
    response = requests.post(URL, headers=headers, files=files, data={"desc": description})
    response.raise_for_status()

    # JSONデータの取得
    response_data = response.json()

    # URLの存在チェックと表示
    if "url" in response_data:
        print(response_data)
        url = response_data["url"]
        return url
    else:
        print("URL not found in response data.")

if __name__ == "__main__":    
    apple_image1 = Image.open("./images/banana.png")
    description = "神秘的なバナナ"
    upload_id = singleUpload(apple_image1, description)