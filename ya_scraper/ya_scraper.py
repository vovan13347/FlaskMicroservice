# Скрэпинговый файл



from concurrent import futures
import random

import requests
from bs4 import BeautifulSoup


import grpc

from ya_pb2 import (
	YaProductShow,
    YaProductInfoResponse,
    
)

import ya_pb2_grpc

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
			time.sleep(2)
			continue
		link = 'https://1ya.ru/?q={0}'.format(query['Search_Result'])
		print(query['Search_Result'])
		break
	except:
		print('Server is not running.')
		time.sleep(2)

response = requests.get(link, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
name = []
prod_price = []
prod_rating = []
prod_image_link = []
prod_url_link = []
shops=soup.find_all('div',class_='offer_link')
for x in range(0,len(shops)): 
	name.append(shops[x].find('a',class_='stretched-link').text)
	
	try:
		prc = shops[x].find('div',class_="product-price").text
		prc = prc[1:-3]
		prod_price.append(prc)
	except Exception:
		print('no price')
		prod_price.append('0')
	
	try:
		img_link = shops[x].find('img',class_='img-fluid').get('src')
		if not img_link.startswith('https://1ya.ru'):
			img_link = 'https://1ya.ru' + img_link
		prod_image_link.append(img_link)
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
print(prod_image_link)
products_list = {0: [YaProductShow(id=1, 
	product_name=name,
	price=prod_price,
	rating=prod_rating,
	image_link=prod_image_link,
	shop_link=prod_url_link )] }

class YaProductService(
    ya_pb2_grpc.YaProductsServicer
):

    def YaShowProducts(self, request, context):
        if request.detail not in products_list:
            context.abort(grpc.StatusCode.NOT_FOUND, "Product not found")
        product_list = products_list[request.detail]
        num_results = min(request.max_results, len(product_list))
        product_show = random.sample(
            product_list, num_results
        )

        return YaProductInfoResponse(products=product_show)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    ya_pb2_grpc.add_YaProductsServicer_to_server(
        YaProductService(), server
    )
    server.add_insecure_port("[::]:50052")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()