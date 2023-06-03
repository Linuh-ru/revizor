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
import urllib.request
import requests
from PIL import Image
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
'''
time.sleep(1)
email = driver.find_element(by=By.NAME, value="email")
email.send_keys("help@o2-cloud.ru")
password = driver.find_element(by=By.NAME, value="password")
password.send_keys("O2xygen9357200")
'''
captcha_img = driver.find_element(By.CSS_SELECTOR, 'img[alt="captcha"]')
'''
captcha = (captcha_img.get_attribute('src'))
#urllib.request.urlretrieve(captcha, 'captcha.jpg')
filename = captcha.split('/')[-1]
r = requests.get(captcha, allow_redirects=True, verify=False)
open(filename+'.png', 'wb').write(r.content)

location = element.location

# print(location)
'''
location = captcha_img.location
def get_captcha_text(location, size):
    im = Image.open('screenshot.png')
    left = location['x']
    top = location['y']
    right = location['x'] + size['width']
    bottom = location['y'] + size['height']
    im = im.crop((left, top, right, bottom))  # defines crop points
    im.save('screenshot.png')
    return True

size = captcha_img.size
driver.save_screenshot('screenshot.png')

get_captcha_text(location, size)


