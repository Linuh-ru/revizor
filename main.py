# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import datetime
#Войти в хром

options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()), options=options)
driver.implicitly_wait(0.5)


#Стартовая страница (аутентификация)
driver.get("https://portal.rfc-revizor.ru/login/")

#Кнопка дополнительно
driver.implicitly_wait(1)
actual = driver.find_element(By.CSS_SELECTOR, 'button[class="secondary-button small-link"]')
# driver.execute_script("arguments[0].scrollIntoView();", actual)
driver.execute_script("arguments[0].click();", actual)

#Кнопка/ссылка забыл (дописать)
driver.implicitly_wait(1)
actual = driver.find_element(By.CSS_SELECTOR, 'a[class="small-link"]')
# driver.execute_script("arguments[0].scrollIntoView();", actual)
driver.execute_script("arguments[0].click();", actual)

#Заполнить поля логин/пароль
time.sleep(1)
email = driver.find_element(by=By.NAME, value="email")
email.send_keys("bsth@o2xygen.ru")
password = driver.find_element(by=By.NAME, value="password")
password.send_keys("Speak2me")
input('press the button')
password.send_keys(Keys.ENTER)

#Мои отчёты по качеству блокировок
driver.implicitly_wait(1)
actual = driver.find_element(By.CSS_SELECTOR, 'a[href="/cabinet/myclaims-reports/"]')
# driver.execute_script("arguments[0].scrollIntoView();", actual)
driver.execute_script("arguments[0].click();", actual)

driver.implicitly_wait(1)
actual = driver.find_element(By.CSS_SELECTOR, 'button[class="button button-add"]')
# driver.execute_script("arguments[0].scrollIntoView();", actual)
driver.execute_script("arguments[0].click();", actual)

driver.implicitly_wait(1)
actual = driver.find_element(By.CSS_SELECTOR, 'input[class="calendar hasDatepicker"]')
# driver.execute_script("arguments[0].scrollIntoView();", actual)

def yesterday_date():
    current_datetime = datetime.now()
    day= str(current_datetime.day-1)
    month = str(current_datetime.month)
    if len(month) == 1:
        month = "0"+month
    year = current_datetime.year
    return f'{day}.{month}.{year}'

actual.send_keys(yesterday_date())

#Кнопка подача
driver.implicitly_wait(1)
actual = driver.find_element(By.CSS_SELECTOR, 'button[class="button button-add"]')
# driver.execute_script("arguments[0].scrollIntoView();", actual)
driver.execute_script("arguments[0].click();", actual)
