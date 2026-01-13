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
site_saby = "https://saby.ru/"
# Добавил после каждого действия ожидание, а то ничего на видео непонятно
try:
    # Открываем браузер.
    # Хочу видеть полноэкранный режим

    browser.get(site_saby)
    browser.maximize_window()

    # Находим и открываем раздел контакты

    contact = browser.find_element(By.LINK_TEXT, 'Контакты')
    contact.click()
    time.sleep(1)

    # Находим и открываем баннер "Тензор"

    tensor_banner = browser.find_element(By.CSS_SELECTOR, 'a[href="https://tensor.ru/"]')
    tensor_banner.click()
    time.sleep(1)


    # Ссылка открылась в новой вкладке, переключаемся на работу в ней

    handles = browser.window_handles
    browser.switch_to.window(handles[1])

    # Находим баннер "Сила в людях", пролистываю до него, а то не видно на видео
    # Проверяем его отображение

    power_in_people = browser.find_element(By.CSS_SELECTOR, 'div[class="s-Grid-container tensor_ru-Index__block4"]')
    power_in_people.location_once_scrolled_into_view
    power_in_people.is_displayed()
    time.sleep(1)

    # Переходим в подробнее
    # Проверяем ссылку

    more = browser.find_element(By.CSS_SELECTOR, 'a[href="/about"]')
    more.click()
    saby_more = "https://tensor.ru/about"
    assert browser.current_url == saby_more
    time.sleep(1)

finally:
    browser.quit()
