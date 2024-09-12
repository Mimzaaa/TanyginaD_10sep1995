import allure

@allure.title("Добавление товара в корзину")
def test_add_product_cart(cart_page):
    resp = cart_page.add_to_cart()
    with allure.step("В теле ответа получен код статус 200"):
        assert resp.status_code == 200, f"Ожидаемый код статус 200, но получили {resp.status_code}"
    with allure.step("Получен ответ:" + resp.text):
        assert resp.text == "1", f"Unexpected response body: {resp.text}"

@allure.title("Увеличение количества товара в корзине")
def test_increase(cart_page):
    resp = cart_page.increase_quantity()
    with allure.step("В теле ответа получен код статус 200"):
        assert resp.status_code == 200, f"Ожидаемый код статус 200, но получили {resp.status_code}"
    with allure.step("Получен ответ:" + resp.text):
        assert resp.text == "2", f"Unexpected response body: {resp.text}"

@allure.title("Уменьшение количества товара в корзине")
def test_decrease(cart_page):
    resp = cart_page.decrease_quantity()
    with allure.step("В теле ответа получен код статус 200"):
        assert resp.status_code == 200, f"Ожидаемый код статус 200, но получили {resp.status_code}"
    with allure.step("Получен ответ:" + resp.text):
        assert resp.text == "1", f"Unexpected response body: {resp.text}"

@allure.title("Удаление товара из корзине")
def test_delete_item(cart_page):
    resp = cart_page.delete_product()
    with allure.step("В теле ответа получен код статус 200"):
        assert resp.status_code == 200, f"Ожидаемый код статус 200, но получили {resp.status_code}"
    with allure.step("Получен ответ:" + resp.text):
        assert resp.text == "0", f"Unexpected response body: {resp.text}"


# def test_add_product_cart():
#     # Задаем URL и заголовки
#     base_url = "https://www.sibdar-spb.ru/ajax/basketOrder.php"
#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
    
#     # Тело запроса, аналогичное тому, что отправляется в Postman
#     data = {
#        "data": json.dumps({"idCookie": "343118", "idProd": "204", "type": "add"})
#     }
    
#     # Отправляем POST запрос
#     resp = requests.post(base_url, headers=headers, data=data)
    
#     # Проверяем, что статус ответа 200
#     assert resp.status_code == 200, f"Unexpected status code: {resp.status_code}"

#     # Проверяем заголовок Content-Type
#     expected_content_type = "text/html; charset=UTF-8"
#     assert resp.headers["Content-Type"] == expected_content_type, (
#         f"Unexpected Content-Type: {resp.headers['Content-Type']}. "
#         f"Expected: {expected_content_type}"
#     )

#     # Проверяем, что тело ответа содержит "1"
#     assert resp.text == "1", f"Unexpected response body: {resp.text}"

# def test_increase():
#     """Тест увеличения количества товара в корзине"""
#     base_url = "https://www.sibdar-spb.ru/ajax/basketOrder.php"
#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
    
#     # Перед тестом мы уверены, что в корзине уже 1 товар
#     # Тело запроса для увеличения количества товара
#     data = {
#         "data": json.dumps({"idCookie": "343118", "idProd": "204", "type": "plus"})
#     }
    
#     # Отправляем POST запрос для увеличения количества товара
#     resp = requests.post(base_url, headers=headers, data=data)
    
#     # Проверяем статус ответа
#     assert resp.status_code == 200, f"Unexpected status code: {resp.status_code}"

#     # Проверяем заголовок Content-Type
#     expected_content_type = "text/html; charset=UTF-8"
#     assert resp.headers["Content-Type"] == expected_content_type, (
#         f"Unexpected Content-Type: {resp.headers['Content-Type']}. "
#         f"Expected: {expected_content_type}"
#     )

#     # Проверяем, что количество товара увеличилось до 2
#     assert resp.text == "2", f"Unexpected response body: {resp.text}"

# def test_decrease():
#     # Задаем URL и заголовки
#     base_url = "https://www.sibdar-spb.ru/ajax/basketOrder.php"
#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
    
#     # Тело запроса, аналогичное тому, что отправляется в Postman
#     data = {
#         "data": json.dumps({"idCookie": "343118", "idProd": "204", "type": "minus"})
#     }
    
#     # Отправляем POST запрос
#     resp = requests.post(base_url, headers=headers, data=data)
    
#     # Проверяем, что статус ответа 200
#     assert resp.status_code == 200, f"Unexpected status code: {resp.status_code}"

#     # Проверяем заголовок Content-Type
#     expected_content_type = "text/html; charset=UTF-8"
#     assert resp.headers["Content-Type"] == expected_content_type, (
#         f"Unexpected Content-Type: {resp.headers['Content-Type']}. "
#         f"Expected: {expected_content_type}"
#     )

#     # Проверяем, что тело ответа содержит "1"
#     assert resp.text == "1", f"Unexpected response body: {resp.text}"

# def test_delete_item():
#     # Задаем URL и заголовки
#     base_url = "https://www.sibdar-spb.ru/ajax/basketOrder.php"
#     headers = {
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
    
#     # Тело запроса, аналогичное тому, что отправляется в Postman
#     data = {
#         "data": json.dumps({"idCookie": "343118", "idProd": "204", "type": "delete"})
#     }
    
#     # Отправляем POST запрос
#     resp = requests.post(base_url, headers=headers, data=data)
    
#     # Проверяем, что статус ответа 200
#     assert resp.status_code == 200, f"Unexpected status code: {resp.status_code}"

#     # Проверяем заголовок Content-Type
#     expected_content_type = "text/html; charset=UTF-8"
#     assert resp.headers["Content-Type"] == expected_content_type, (
#         f"Unexpected Content-Type: {resp.headers['Content-Type']}. "
#         f"Expected: {expected_content_type}"
#     )

#     # Проверяем, что тело ответа содержит "0"
#     assert resp.text == "0", f"Unexpected response body: {resp.text}"