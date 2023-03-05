from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# инициализируем драйвер Chrome
driver = webdriver.Chrome()

# открываем сайт Google
driver.get("https://www.google.com/")

# находим поле ввода запроса
search_box = driver.find_element("name", "q")

# вводим запрос "python"
search_box.send_keys("python")

# нажимаем клавишу Enter
search_box.send_keys(Keys.RETURN)

# ждем 5 секунд, чтобы страница успела загрузиться
time.sleep(5)

# проверяем, что заголовок страницы содержит слово "python"
assert "python" in driver.title.lower()

# закрываем браузер
driver.quit()
