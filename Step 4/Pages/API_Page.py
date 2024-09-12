from Utils.ConfigProvider import ConfigProvider
from Utils.DataProvider import DataProvider
import requests
import json
import allure

class CartPage:
    """Класс для работы с API тестами"""
    def __init__(self):
        self.base_url = ConfigProvider.get_api_url()
        self.headers = ConfigProvider.get_headers()

    @allure.step("Отправляется POST запрос")
    def post_request(self, data):
        response = requests.post(self.base_url, headers=self.headers, data=data)
        response.raise_for_status()
        return response
    
    @allure.step("Добавляется товар в корзину")
    def add_to_cart(self, id_cookie=None, product_id=None):
        id_cookie = id_cookie or DataProvider.get_id_cookie()
        product_id = product_id or DataProvider.get_product_id()
        data = {"data": json.dumps({"idCookie": id_cookie, "idProd": product_id, "type": "add"})}
        return self.post_request(data)

    @allure.step("Увеличивается количество товара в корзине, нажимая на +")
    def increase_quantity(self, id_cookie=None, product_id=None):
        id_cookie = id_cookie or DataProvider.get_id_cookie()
        product_id = product_id or DataProvider.get_product_id()
        data = {"data": json.dumps({"idCookie": id_cookie, "idProd": product_id, "type": "plus"})}
        return self.post_request(data)

    @allure.step("Уменьшается количество товара в корзине, нажимая на -")
    def decrease_quantity(self, id_cookie=None, product_id=None):
        id_cookie = id_cookie or DataProvider.get_id_cookie()
        product_id = product_id or DataProvider.get_product_id()
        data = {"data": json.dumps({"idCookie": id_cookie, "idProd": product_id, "type": "minus"})}
        return self.post_request(data)

    @allure.step("Удаляется товар из корзины, нажимая на крестик")
    def delete_product(self, id_cookie=None, product_id=None):
        id_cookie = id_cookie or DataProvider.get_id_cookie()
        product_id = product_id or DataProvider.get_product_id()
        data = {"data": json.dumps({"idCookie": id_cookie, "idProd": product_id, "type": "delete"})}
        return self.post_request(data)