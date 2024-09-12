import allure

class ConfigProvider:
    """Основной URL для тестов"""
    def get_base_url():
        return "https://www.sibdar-spb.ru/"

    @allure.step("URL для API запросов")
    def get_api_url():
        return "https://www.sibdar-spb.ru/ajax/basketOrder.php"

    """Заголовки для API запросов"""
    def get_headers():
        return {
            "Content-Type": "application/x-www-form-urlencoded"
        }
