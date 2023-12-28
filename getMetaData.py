import requests
import os
from dotenv import load_dotenv

load_dotenv()

GYAZO_ACCESS_TOKEN=os.getenv("GYAZO_ACCESS_TOKEN")

def getMetaData_desc(image_id):
    headers = {'Authorization': "Bearer {}".format(GYAZO_ACCESS_TOKEN)}
    
    response = requests.get(f"https://api.gyazo.com/api/images/{image_id}", headers=headers)
    response.raise_for_status()
    response_data = response.json()

    if "metadata" in response_data and "desc" in response_data["metadata"]:
        # ここでdescを取得
        print(response_data)
        desc = response_data["metadata"]["desc"]
        return desc
    else:
        print("URL not found in response data.")


if __name__ == "__main__":    
    upload_id = "864127743b07d870a98912c11afa5656"

    MetaData = getMetaData_desc(upload_id)
    print(MetaData) 