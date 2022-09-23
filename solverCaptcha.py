import os
from twocaptcha import TwoCaptcha


def solveRecaptcha(sitekey, url):
    api_key = os.getenv('APIKEY_2CAPTCHA', '0ca5f138913e7927893fd3ea5fb6b40b')

    solver = TwoCaptcha(api_key)

    try:
        result = solver.recaptcha(
            sitekey=sitekey,
            url=url)

    except Exception as e:
        print(e)

    else:
        return result