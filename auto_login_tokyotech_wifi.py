import os
from contextlib import closing

from selenium import webdriver

import conf

URL = 'https://wlanauth.noc.titech.ac.jp/fs/customwebauth/techauth.html?switch_url=https://wlanauth.noc.titech.ac.jp/login.html&ap_mac=04:c5:a4:93:7c:60&client_mac=54:26:96:e1:0a:4f&wlan=TokyoTech&redirect=www.gstatic.com/generate_204'


def main():
    with closing(webdriver.Chrome()) as driver:
        driver.get(URL)

        username = os.getenv("TOKYOTECH_USERNAME", conf.TOKYOTECH_USERNAME)
        password = os.getenv("TOKYOTECH_PASSWORD", conf.TOKYOTECH_PASSWORD)

        driver.find_element_by_id('username').send_keys(username)
        driver.find_element_by_id('password').send_keys(password)
        driver.find_element_by_class_name('button').click()


if __name__ == '__main__':
    main()
