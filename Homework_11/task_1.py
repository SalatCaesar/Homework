# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


browser = webdriver.Chrome()
saby_site = "https://saby.ru/"

time.sleep(2)
try:
    browser.get("https://saby.ru/")
    time.sleep(2)

    contact = browser.find_element(By.LINK_TEXT, 'Контакты')
    contact.click()
    time.sleep(2)

    tensor_banner = browser.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    tensor_banner.click()
    time.sleep(2)
    handles = browser.window_handles
    browser.switch_to.window(handles[1])

    power_in_people = browser.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4')
    power_in_people.location_once_scrolled_into_view
    time.sleep(2)

    power_in_people.is_displayed()
    more = browser.find_element(By.CSS_SELECTOR, 'a[href*="/about"]')
    more.click()
    time.sleep(2)








finally:
    browser.quit()
