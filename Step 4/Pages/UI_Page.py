from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.common.exceptions import TimeoutException

class ShopPage:
    """Класс для работы с UI тестами"""
    def __init__(self, driver: WebDriver) -> None:
        self.__url = "https://www.sibdar-spb.ru/"
        self.__driver = driver
    
    @allure.step("Открыть сайт")
    def open(self):
        self.__driver.get(self.__url)
    
    @allure.step("Выбрать продукт")
    def select_product(self, product_id):
        product_selector = f"div[id='bx_3218110189_{product_id}']"
        self.__driver.find_element(By.CSS_SELECTOR, product_selector).click()
    
    @allure.step("Нажать на кнопку - В корзину")
    def add_to_cart(self, product_id):
        add_button_xpath = f"//button[@onclick=\"addToCard('{product_id}', this, event);\"]"
        WebDriverWait(self.__driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, add_button_xpath))
        ).click()
    
    @allure.step("Открыть корзину")
    def open_cart(self):
        self.__driver.find_element(By.CSS_SELECTOR, "a[class='bask_btn_right']").click()
    
    @allure.step("Выбранный товар в корзине")
    def get_cart_product(self, product_id):
        product_in_cart_selector = f"div[id='or_{product_id}']"
        try:
            product_element = WebDriverWait(self.__driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, product_in_cart_selector))
            )
            return product_element
        except TimeoutException:
            return None

    @allure.step("Увеличить количества товара")
    def increase_quantity(self, product_id):
        plus_button_xpath = f"//span[@class='plus_prod' and contains(@onclick, '{product_id}')]"
        self.__driver.find_element(By.XPATH, plus_button_xpath).click()

    @allure.step("Открыть корзину повторно")
    def open_cart_again(self):
        self.__driver.find_element(By.CSS_SELECTOR, "a[class='bask_btn']").click()

    @allure.step("Уменьшить количества товара")
    def decrease_quantity(self, product_id):
        minus_button_xpath = f"//span[@class='minus_prod' and contains(@onclick, '{product_id}')]"
        self.__driver.find_element(By.XPATH, minus_button_xpath).click()
    
    @allure.step("Удалить товар из корзины")
    def delete_product(self, product_id):
        delete_button_css = f"button.delet_pr_bas[onclick='deleteCardItem(this, {product_id})']"
        self.__driver.find_element(By.CSS_SELECTOR, delete_button_css).click()
    
    @allure.step("Результат")
    def get_empty_cart(self) -> str:
        try:
            # Находим элемент с текстом "Корзина пуста, необходимо это исправить"
            empty_cart_element = self.__driver.find_element(By.CSS_SELECTOR, "div.body_order h2")
            # Возвращаем текст из элемента
            return empty_cart_element.text
        except Exception as e:
            # Возвращаем сообщение об ошибке, если элемент не найден
            return f"Ошибка: {str(e)}"
