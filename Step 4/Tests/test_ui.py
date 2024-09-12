import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Pages.UI_Page import ShopPage
from Utils.DataProvider import DataProvider

@allure.title("Добавление товара в корзину")
def test_add_to_cart(browser: WebDriver):
    product_id = DataProvider.get_product_id()
    shop_page = ShopPage(browser)
    shop_page.open()
    shop_page.select_product(product_id)
    shop_page.add_to_cart(product_id)
    shop_page.open_cart()

    with allure.step("Проверить, что товар добавлен в корзину"):
        product = shop_page.get_cart_product(product_id)
        assert product is not None, "Товар не был добавлен в корзину"

@allure.title("Увеличение количества товара в корзине")
def test_increase_the_quantity(browser: WebDriver):
    product_id = DataProvider.get_product_id()
    shop_page = ShopPage(browser)
    shop_page.open()
    shop_page.select_product(product_id)
    shop_page.add_to_cart(product_id)
    shop_page.open_cart()

    with allure.step("Проверить, что товар добавлен в корзину"):
        assert shop_page.get_cart_product(product_id) is not None, "Товар не был добавлен в корзину"

    shop_page.increase_quantity(product_id)

    with allure.step("Обновляем страницу"):
        browser.refresh()
    
    shop_page.open_cart_again()

    with allure.step("Проверить, что количество товара увеличилось"):
        updated_quantity = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"input[id='count_product_item_{product_id}']"))
        ).get_attribute("value")
        assert updated_quantity == "2 шт", "Количество товара не увеличилось"

        """Добавляем шаг в Allure с количеством товара"""
        allure.attach(f"Количество товара: {updated_quantity}", name="Количество товара в корзине", attachment_type=allure.attachment_type.TEXT)
        assert updated_quantity == "2 шт", f"Количество товара не увеличилось, фактически: {updated_quantity}"

@allure.title("Уменьшение количества товара в корзине")
def test_decrease_the_quantity(browser: WebDriver):
    product_id = DataProvider.get_product_id()
    shop_page = ShopPage(browser)
    shop_page.open()
    shop_page.select_product(product_id)
    shop_page.add_to_cart(product_id)
    shop_page.open_cart()

    with allure.step("Проверить, что товар добавлен в корзину"):
        assert shop_page.get_cart_product(product_id) is not None, "Товар не был добавлен в корзину"

    shop_page.increase_quantity(product_id)

    with allure.step("Обновляем страницу"):
        browser.refresh()

    shop_page.open_cart_again()

    with allure.step("Проверить, что количество товара в корзине увеличилось"):
        assert shop_page.get_cart_product(product_id)

    shop_page.decrease_quantity(product_id)

    with allure.step("Обновляем страницу"):
        browser.refresh()

    shop_page.open_cart_again()

    with allure.step("Проверить, что количество товара уменьшилось"):
        updated_quantity = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f"input[id='count_product_item_{product_id}']"))
        ).get_attribute("value")
        assert updated_quantity == "1 шт", "Количество товара не уменьшилось"

        """Добавляем шаг в Allure с количеством товара"""
        allure.attach(f"Количество товара: {updated_quantity}", name="Количество товара в корзине", attachment_type=allure.attachment_type.TEXT)
        assert updated_quantity == "1 шт", f"Количество товара не увеличилось, фактически: {updated_quantity}"

@allure.title("Удаление товара из корзине")
def test_delete_product(browser: WebDriver):
    product_id = DataProvider.get_product_id()
    shop_page = ShopPage(browser)
    shop_page.open()
    shop_page.select_product(product_id)
    shop_page.add_to_cart(product_id)
    shop_page.open_cart()

    with allure.step("Проверить, что товар добавлен в корзину"):
        assert shop_page.get_cart_product(product_id) is not None, "Товар не был добавлен в корзину"

    shop_page.delete_product(product_id)

    with allure.step("Проверить, что товар удален из корзину"):
        message = shop_page.get_empty_cart()
        assert message == "Корзина пуста, необходимо это исправить", \
            f"Ожидалось сообщение 'Корзина пуста, необходимо это исправить', но получено '{message}'"

        # Добавляем шаг в Allure с текстом сообщения о пустой корзине
        allure.attach(name="Получаем текст сообщения о пустой корзине",
                      body=message,
                      attachment_type=allure.attachment_type.TEXT)
