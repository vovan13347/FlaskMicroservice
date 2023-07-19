# Скрэпинговый файл



from concurrent import futures
import random

import requests
from bs4 import BeautifulSoup


import grpc

from pleer_pb2 import (
	ProductShow,
    ProductInfoResponse,
    
)

import pleer_pb2_grpc

import time


headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept-Language': 'ru-RU, en;q=0.5'
}

while True:
	try:
		resp = requests.get('http://127.0.0.1:5000/searchval')
		query = resp.json()
		print('SR:', query['Search_Result'])
		if query['Search_Result'] == '' or query['Search_Result'] is None:
			print('Search_Result is null')
			time.sleep(3)
			continue
		link = 'https://www.pleer.ru/search_{0}.html'.format(query['Search_Result'])
		print(query['Search_Result'])
		break
	except:
		print('Server is not running.')
		time.sleep(3)

response = requests.get(link, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
name = []
prod_price = []
prod_rating = []
prod_image_link = []
prod_url_link = []
shops=soup.find_all('div',class_='section_item')
for x in range(0,len(shops)): 
	name.append(shops[x].find('span',class_='item_name').text)
	
	try:
		p = shops[x].find('div',class_="product_price product_price_color1 small")
		p2 = p.find('div',class_="price").text
		#p3 = p2.find('span',class_="price_disk").text
		k = p2.find('б')
		s=''
		s=s+p2[:k+1]
		prod_price.append(s)
	except Exception:
		print('no price')
		prod_price.append('0')
	
	try:
		prod_image_link.append(shops[x].find('a',class_='product_preview_img').get('href'))
	except Exception:
		print('no image_link')
		prod_image_link.append('')
	
	try:
		n = random.triangular(1,5,5)
		x = round(n, 1)
		r = ''
		r = r + 'оценка = ' + str(x) + ' из 5'
		prod_rating.append(r)
	except Exception:
		print('no rating')
		prod_rating.append('0')
	
	try:
		prod_url_link.append(link)
	except Exception:
		print('no link')
		prod_url_link.append('')
	 
	


print('имя товара',name)
print('цена',prod_price)
print('рейтинг',prod_rating)
products_list = {0: [ProductShow(id=1, 
	product_name=name,
	price=prod_price,
	rating=prod_rating,
	image_link=prod_image_link,
	shop_link=prod_url_link)] }

class ProductService(
    pleer_pb2_grpc.ProductsServicer
):

    def ShowProducts(self, request, context):
        if request.detail not in products_list:
            context.abort(grpc.StatusCode.NOT_FOUND, "Product not found")
        product_list = products_list[request.detail]
        num_results = min(request.max_results, len(product_list))
        product_show = random.sample(
            product_list, num_results
        )

        return ProductInfoResponse(products=product_show)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pleer_pb2_grpc.add_ProductsServicer_to_server(
        ProductService(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()