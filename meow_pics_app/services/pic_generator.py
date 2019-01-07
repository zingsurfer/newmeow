from .cat_api_service import CatAPIService

class PicGenerator:

    def random():
        pic_url = CatAPIService.random_cat_pic_url()

        return pic_url
