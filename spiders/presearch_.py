#!/usr/bin/env python
# coding=utf-8
import requests
import json
from lxml import etree
session = requests.Session()
from random_words import RandomWords
word_generator = RandomWords()
from urllib.parse import urlencode

headers = {
    'authority': 'engine.presearch.org',
    'sec-ch-ua': '"Chromium";v="94", "Google Chrome";v="94", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-dest': 'document',
    'referer': 'https://engine.presearch.org/search?q=sons',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2MzMyMzI5MjUsImV4cCI6MTYzMzgzNzcyNSwidXNlcl9pZCI6MjY5MzQ3OCwidXNlcl9hcGlfa2V5IjoiUFRvd3M0WXh0Z0NpY2VLck44SkRieHhVSFFFTlhVUXJZd1NYcDRIMnM0SlpOMjRwdTJmeVN4V3BYbzlCZ3l5R29aWVh4RkFXWnNKTVMxNFk0dVJJMGw2NEJ0aEFQUkFEY1hneW95cTZnTzE2WDVuOHY3NzlYc3RBWUN4YXdUamh6bHIyaDQxUktUZWpFaUc1TmdIeU9XIiwiYmV0YXMiOltdfQ.FvhdScR-Al0o5ZuetJmVpvIwAKGmCY2gkQHY6wm7oCerkHZAxxzHEzBgZozeEPls5FSJnZQgzzW98cTXR8fSZAa5VQjXdPh6qCLrIuDW8GeFt2epzf5Pm7jebnrxibslRTLU5f5iVUHrFZWXRk-y3ZIV784MzNN0LohT1dGTjCAnwF6JyKNzpZC5QPwatYbihp8CYT3Ns4s35DEJiemDaS2orU8zAsTB9SbK7wB7u9aHSgjuN-VWUSbMI2Sk5Pqhz_EkdgCImxV-lAihRbC-W_2bZvJZ-ukBrABZw3OBaP7GS2sxxAo3gWxbqF8jDR5Z5oyfbO8bm_M-KBStcfbnkA; b=0; presearch_session=eyJpdiI6Ik44K0E3akdZMEZQTkVCWFwvVFVBK2dRPT0iLCJ2YWx1ZSI6IjlwY3FaZDk1RUY3dVRlNjl6KzFxNnE2MnU0V0xZRTBhRGZ5T21uaTl1ZjRVWElyOXQrT3BJOUx3SEdYdm13dlJpWUR1emlYMXdqUm9EUVN4Z1hJTXl6VENDKzBDZEVIMkloSG5SNFV5RGVpT1ByREpUcFRzeExVZFwvQisyNWs0RSIsIm1hYyI6ImY2ZTllOWVkNGYwOTNjZTVkYjAwZDVlNjQzMTBiNTY4Y2E0YjZhNDg0Mzk5NWExMGUzYzdjZGM5MGM1ZDBiODMifQ%3D%3D; AWSALB=hNzZLr94jgLdigCSVEbsWpbZY3kAEXNXVY8G708LJgwNpQ/sFGMzP9IH9U3HgITcoJaIXFTYsfWgEJ40shC/NVGFguGUvmnJcDuwsHrK4yUPWJsvIYW6J+QiyWf4; XSRF-TOKEN=eyJpdiI6ImwySkpyd1N2RWNmdXRNblZSNlRDV3c9PSIsInZhbHVlIjoiYkNyTFwvTExCekhKUlloUUhIZ0NTOHdUT3RFQ1VINVYxZVh3eithYkN4SlJlcGVNZm1yNnA0ZzZOWU5mMU5UK0QiLCJtYWMiOiIwZTk4NjFkZGQ4ZTI0NTAxZGFkN2ZmOTJlODMyY2FlMDBiNDVhYzM3MTUxZTc1MmM0YzdkODA2M2I0Yjc1YzYzIn0%3D; AWSALB=Gumnsz/mEj/5aZULsc7kQVk1WwVevIbsuvp40M/U7Lj9NvL6aA3SD3zBNftJogl1UZ79ALubzm/YHR/HtNgLNYPdgkVLNpte8MYxEGJeW6SxQ7+ZNnj+jgpZRyAi; b=1',
}

params = (
    ('q', 'sons'),
    ('r', '1'),
)

response = requests.get('https://engine.presearch.org/search', headers=headers, params=params)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://engine.presearch.org/search?q=sons&r=1', headers=headers)

def load_cookies(session, cookie_path=""):
    cookies = json.loads(open(cookie_path,encoding="utf-8").read())

    jar = requests.cookies.RequestsCookieJar()
    for cookie in cookies:
        jar.set(cookie.get("name"),cookie.get("value"))
    session.cookies.update(jar)

def search_once(session, word_generator=word_generator):





