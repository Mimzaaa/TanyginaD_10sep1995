import pytest
import allure
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from Pages.API_Page import CartPage

@pytest.fixture
def browser():
    with allure.step("Открыть браузер"):
        browser = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        browser.implicitly_wait(3)
        browser.maximize_window()
        yield browser
        
    with allure.step("Закрыть браузер"):
        browser.quit()

@pytest.fixture
def cart_page():
    """Фикстура для создания экземпляра CartPage"""
    return CartPage()
