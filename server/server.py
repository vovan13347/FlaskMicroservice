# Фласковый файл
import os

from flask import Flask, flash, render_template, request, redirect
import grpc

from forms_search import SearchForm
from pleer_pb2 import ProductInfoRequest
from pleer_pb2_grpc import ProductsStub

from ya_pb2 import YaProductInfoRequest
from ya_pb2_grpc import YaProductsStub

from flask import jsonify

import time

# from concurrent import futures

# import threading

globsearch = ''

app = Flask(__name__)

product_host = os.getenv("PRODUCT_HOST", "localhost")
product_channel = grpc.insecure_channel(f"{product_host}:50051")
product_client = ProductsStub(product_channel)

ya_host = os.getenv("PRODUCT_HOST", "localhost")
ya_channel = grpc.insecure_channel(f"{ya_host}:50052")
ya_client = YaProductsStub(ya_channel)

search_res  = ''

'''
class Search(productshow_pb2_grpc.SearchServicer):
    def SearchProduct(self,request, context):
        global search_res
        return productshow_pb2.SearchRequest(search_res)

    def __init__(self, stop_event):
        self.stop_event = stop_event

    def Stop(self, request, context):
        self._stop_event.set()
        return Search_pb2.ShutdownResponse()
'''

'''
def serve():
#    stop_event = threading.Event()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    productshow_pb2_grpc.add_SearchServicer_to_server(Search(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
 #   stop_event.wait()
 #   server.stop()
    server.wait_for_termination()
'''


@app.route('/', methods=['GET', 'POST'])
def index():
    search = SearchForm(request.form)
    global globsearch
    globsearch = search.data['search']
    if request.method == 'POST':
        time.sleep(10)
        return search_results(search)
    return render_template('index.html', form=search)


@app.route('/searchval', methods = ['GET'])
def ReturnJSON():
    global globsearch
    if (request.method == 'GET'):
        data = {
            "Search_Result": globsearch,
        }
        return jsonify(data)

@app.route("/search_results")
def search_results(search):
#    global search_res
#    search_res = search
#    serve()
    results = []
    product_request = ProductInfoRequest(
        user_id=1, detail=0, max_results=3
    )
    product_response = product_client.ShowProducts(
        product_request
    )
    pleer_product = product_response.products



    ya_product_request = YaProductInfoRequest(
        user_id=1, detail=0, max_results=3
    )

    ya_product_response = ya_client.YaShowProducts(
        ya_product_request
    )

    ya_product =  ya_product_response.products

    # total_products = ya_product[:] 

    total_products = pleer_product[:] + ya_product[:] 

    n = total_products[0].product_name
    m = total_products[1].product_name
    print
    #print('shop_link = ', total_products[1].shop_link)
    print('n =')
    print(' --- ')
    print(n)
    print(' --- ')
    print('m = ')
    print(' *** ')
    print(m)
    print(' ***')
    #print('total_products[1] = ', total_products[1].product_name)
    return render_template(
        "search_results.html",
        n = total_products, l = min(len(n), len(m))
    )
#    return render_template('search_results.html')


if __name__ == "__main__":
    app.run()