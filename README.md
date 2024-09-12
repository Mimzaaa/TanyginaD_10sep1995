# TanyginaD_10sep1995

## Финальное тестовое задание

### Первое задание - Step 1
#### Составьте в Excel чек-лист наиболее важных, на ваш взгляд, нефункциональных проверок для интернет-магазина https://www.sibdar-spb.ru/.

##### При проведении тестирования использовала такие инструменты:
- lambdatest
- PageSpeed Insights
- Консоль разработчика
- SSL Server Test
- WebPageTest

#### Так же приложен файл с багами.

### Второе задание - Step 2
#### Составьте коллекцию Postman, которая поможет провести смоук-тест корзины интернет-магазина https://www.sibdar-spb.ru/, и инструкцию по работе с ней.

### Третье задание - Step 3
#### Написать SQL-запросы.

### Четвертое задание - Step 4
#### Напишите хотя бы три API и три UI-теста функциональности корзины интернет-магазина https://www.sibdar-spb.ru/.
Необходимо использовать: Python, Selenium, Requests, pytest, Allure.

#### __Шаги:__
- Склонировать проект 'git clone https://github.com/Mimzaaa/TanyginaD_10sep1995'
- Установить зависимости 'pip install -r requirements.txt'
- Запустить тесты 'pytest --alluredir=./allure-results'
- Сгенерировать отчет 'allure generate allure-results -o allure-report'
- Открыть отчет 'allure serve allure-results'

#### __Стек:__
- pytest
- selenium
- webdriver manager
- requests
- allure
- config
- json

#### __Струткура:__
- ./Test - тесты
- ./Pages - описание страниц
- ./Utils - вспомогательные функции для работы с запросами
- ./requirements.txt - зависимости

#### __Полезные ссылки:__
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore/)
- [Про pip freeze](https://pip.pypa.io/en/stable/cli/pip_freeze/)