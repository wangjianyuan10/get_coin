#!/usr/bin/env python
# coding=utf-8
import json
import time
import random
from selenium import webdriver
from random_words import RandomWords
word_generator = RandomWords()

# 初始化
def init():
    driver = webdriver.Chrome()
    driver.get("https://engine.presearch.org")
    return driver



def load_cookie(driver,cookie_path="pre_cookie.json"):
    """
    加载 cookie
    """
    cookies = json.loads(open(cookie_path).read())
    for cookie in cookies:
        for key in ["expiry", "expirationDate", "sameSite"]:
            try:
                cookie.pop(key)
            except:
                pass
        driver.add_cookie(cookie)
def search_once(driver,word_generator=word_generator):
    """
    搜索一次
    """
    input_ele = driver.find_element_by_xpath("//input")
    input_ele.clear()
    input_ele.send_keys(word_generator.random_word())
    input_ele.submit()

def main(times=30, sleep_time=15):
    """
    默认搜索 30 次
    """
    driver = init()
    load_cookie(driver,cookie_path="./presearch_cookies/pre_cookie_1574448427_qqcom.json")
    driver.get("https://engine.presearch.org")
    for i in range(times):
        search_once(driver)
        time.sleep(sleep_time+random.random()*sleep_time)
    driver.quit()

if __name__=='__main__':
    main(times=30)

