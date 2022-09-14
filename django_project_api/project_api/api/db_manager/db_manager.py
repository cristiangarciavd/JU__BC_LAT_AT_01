from .project_api.api.models import Product, Search
import datetime

DAYS_TO_UPDATE = 4

class DbManager(object):
    def find_term(self, search_term):
        #time_threshold = datetime.datetime.now() - datetime.timedelta(DAYS_TO_UPDATE)
        #search = list(Search.objects.filter(name=search_term).filter(created_at__range = [time_threshold, datetime.datetime.now()]).values())
        search = Search.objects.filter(name=search_term)
        if len(search) > 0:
            return search
        else:
            return False

    def term_up_today(self, search):
        print("term_up_today ", type(search))
        time_threshold = datetime.datetime.now() - datetime.timedelta(DAYS_TO_UPDATE)
        search = list(search.filter(created_at__range = [time_threshold, datetime.datetime.now()]).values())
        if len(search) > 0:
            return search
        else:
            return False

    def find_products(self, search):
        if search:
            if len(search) > 0:
                products = list(Product.objects.filter(search=search[0]['id']).values())
                datos={'message':"success", 'products': products}
            else:
                datos={'message':'products not found'}
            return datos
        else:
            datos={'message': 'Error, no argument passed'}
            return datos

    def delete_search(self, search_term):
        search = list(Search.objects.filter(name=search_term))
        if len(search) > 0:
            Search.objects.filter(name=search_term).delete()
            datos={'message':"success"}
        else:
            datos={'message':  'search term not found'}
        return datos

    def create(self, products, search_term):
        if len(products) > 0:
            search = Search.objects.create(name=search_term)
            for p in products:
                prod = Product.objects.create(
                    name = p['name'],
                    price = p['price'],
                    image_url = p['image_url'],
                    url = p['url'],
                    search = search
                )
                #search.add(prod)
                #prod.search.add(search)
            datos={'message':"success"}
        else:
            datos={'message':  'No items passed'}
        return datos
        
