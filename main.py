import os
from twocaptcha import TwoCaptcha
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def solvehCaptcha():
    api_key = os.getenv('APIKEY_2CAPTCHA', '0ca5f138913e7927893fd3ea5fb6b40b')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.hcaptcha(
            sitekey='b3f14452-58e2-4030-82ae-9d4647a77b88',
            url='https://bezkolejki.eu/luw-olp/',
        )

    except Exception as e:
        print(e)
        return False

    else:
        return result

browser = webdriver.Chrome()
browser.get('https://bezkolejki.eu/luw-olp')
# wait for iframe
# WebDriverWait(browser, 10).until(EC.presence_of_element_located(
#     (By.CSS_SELECTOR, '#root > div > main > div > section > form > div > div > div > iframe')))
result = solvehCaptcha()
if result:
    code = result['code']
    print(code)
