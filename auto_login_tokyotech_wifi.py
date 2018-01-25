import os
from selenium import webdriver

URL = 'https://wlanauth.noc.titech.ac.jp/fs/customwebauth/techauth.html?switch_url=https://wlanauth.noc.titech.ac.jp/login.html&ap_mac=04:c5:a4:93:7c:60&client_mac=54:26:96:e1:0a:4f&wlan=TokyoTech&redirect=www.gstatic.com/generate_204'

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get(URL)

    username = os.getenv("TOKYOTECH_USERNAME", "username")
    password = os.getenv("TOKYOTECH_PASSWORD", "password")

    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_class_name('button').click()

    driver.quit()
    driver.close()