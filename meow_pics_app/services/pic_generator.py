import os
import requests
class PicGenerator:

    def random():
        api_url = 'https://api.thecatapi.com/v1/images/search'
        headers = {'x-api-key': f'{os.environ.get("CAT_KEY")}'}
        response = requests.get(api_url, headers=headers)
        data = response.json()
        pic_url = data[0]["url"]
        return pic_url
