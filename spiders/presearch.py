#!/usr/bin/env python
# coding=utf-8
import json
import time
import os
import random
from selenium import webdriver
from random_words import RandomWords
word_generator = RandomWords()
from datetime import datetime
import shutil
from collections import Counter

CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))

# os.system("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 &")
options = webdriver.ChromeOptions()
# options.add_experimental_option("debuggerAddress","127.0.0.1:9222") 

if not os.path.exists( os.path.join(CURRENT_DIR,"log" )):
    os.makedirs( os.path.join(CURRENT_DIR,"log" ) )

log_file = os.path.join(CURRENT_DIR,"log",datetime.utcnow().strftime("%Y%m%d.log"))
if not os.path.exists(log_file):
    open(log_file,"w").close()

# 初始化
def init():
    driver = webdriver.Chrome(options=options)
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

def main(times=30, sleep_time=15,cookie_path="./presearch_cookies/pre_cookie_1574448427_qqcom.json"):
    """
    默认搜索 30 次
    """
    driver = init()
    load_cookie(driver,cookie_path=cookie_path)
    driver.get("https://engine.presearch.org")
    for i in range(times):
        search_once(driver)
        with open(log_file,'a') as fp:
            fp.write(cookie_path+"\n")

        time.sleep(sleep_time+random.random()*sleep_time)
    driver.quit()

if __name__=='__main__':
    completed_dict = dict(Counter(open(log_file).read().split("\n")))
    print(completed_dict)
    for dirname in ['presearch_cookies',"walker_211007", "zhaolanping_211007"]:
    # for dirname in [ "zhaolanping_211007"]:
        for cookie_path in os.listdir(os.path.join(CURRENT_DIR,dirname)):
            cookie_path = os.path.join(CURRENT_DIR, dirname, cookie_path)
            print(cookie_path)
            if cookie_path.endswith(".json"):
                times = 30+random.randint(0,5)-completed_dict.get(cookie_path,0) 
                # times = 30-completed_dict.get(cookie_path,0) 
                if times > 0:
                    main(times=times,cookie_path=cookie_path)

