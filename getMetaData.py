import requests
import os
from dotenv import load_dotenv

load_dotenv()

ACCESS_TOKEN= # YOUR_ACCESS_TOKEN

def getMetaData_desc(image_id):
    headers = {'Authorization': "Bearer {}".format(ACCESS_TOKEN)}
    
    response = requests.get(f"https://api.gyazo.com/api/images/{image_id}", headers=headers)
    response.raise_for_status()
    response_data = response.json()

    if "metadata" in response_data and "desc" in response_data["metadata"]:
	# ここでdescを取得するためのjson解析
        desc = response_data["metadata"]["desc"]
        return desc
    else:
        print("URL not found in response data.")


if __name__ == "__main__":    
    upload_id = "fcae5cfe1ba5d1672cf8f7cb06d6e3e4"

    MetaData = getMetaData_desc(upload_id)
    print(MetaData)