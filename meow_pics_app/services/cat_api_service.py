import os
import requests

class CatAPIService:

    def random_cat_url():
        api_url = 'https://api.thecatapi.com/v1/images/search'
        headers = {'x-api-key': f'{os.environ.get("CAT_KEY")}'}
        response = requests.get(api_url, headers=headers)
        data = response.json()
        random_cat_url = data[0]["url"]
        
        return random_cat_url
