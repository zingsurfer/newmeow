# import os
# import requests
from .cat_api_service import CatAPIService
class PicGenerator:

    def random():
        # api_url = 'https://api.thecatapi.com/v1/images/search'
        # headers = {'x-api-key': f'{os.environ.get("CAT_KEY")}'}
        # response = requests.get(api_url, headers=headers)
        # data = response.json()
        # pic_url = data[0]["url"]
        pic_url = CatAPIService.random_cat_url()
        
        return pic_url
