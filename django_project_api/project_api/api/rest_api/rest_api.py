from api.data_analizer.data_analize import DataCollector

class RestApi(object):

    def get_products(self, prod_name: str):
        instance = DataCollector()
        instance.collect(prod_name)
        instance.sort_by_price()
        ls = instance.top_x_products(5)
        output = []
        for l in ls:
            output.extend(l)
        return output
