from django.http import JsonResponse

from api.data_analizer.data_analize import DataCollector


class RestApi(object):

    def get_products(self, prod_name: str):
        dt = DataCollector()
        dt.collect(prod_name)
        dt.sort_by_price()
        prod_list = dt.top_x_products(5)
        output = []
        if len(prod_list) > 0:
            for p in prod_list:
                output.extend(p)
            return JsonResponse(output, safe=False)
        else:
            return JsonResponse({"message": "Product not found"})
