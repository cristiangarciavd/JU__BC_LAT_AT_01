from api.data_analizer.data_analize import DataCollector

class RestApi(object):

    def get_products(self, prod_name: str):
        instance = DataCollector()
        instance.collect(prod_name)
        instance.sort_by_price()
        ls = instance.top_x_products()
        for l in ls:
            return l









