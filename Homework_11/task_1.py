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
saby_more = "https://tensor.ru/about"

try:
    # Преходим в полноэкранный режим и переходим по адресу сайта
    browser.maximize_window()
    browser.get(site_saby)

    # Находим и открываем раздел контакты
    contact = browser.find_element(By.LINK_TEXT, 'Контакты')
    contact.click()
    time.sleep(1)

    # Находим и открываем баннер "Тензор"
    tensor_banner = browser.find_element(By.CSS_SELECTOR, 'a[href="https://tensor.ru/"]')
    tensor_banner.click()

    # Ссылка открылась в новой вкладке, переключаемся на работу в ней
    handles = browser.window_handles
    browser.switch_to.window(handles[1])

    # Находим баннер "Сила в людях", скроллим до него, а то не видно на видео, проверяем его отображение
    power_in_people = browser.find_element(By.CSS_SELECTOR, 'div[class="s-Grid-container tensor_ru-Index__block4"]')
    power_in_people.location_once_scrolled_into_view
    assert power_in_people.is_displayed(), 'Баннер "Сила в людях" не отображается'

    # Переходим в подробнее и проверяем адрес страницы
    more = browser.find_element(By.CSS_SELECTOR, 'a[href="/about"]')
    more.click()
    assert browser.current_url == saby_more

finally:
    browser.quit()
