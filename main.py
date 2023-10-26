# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 22:38:33 2023

@author: Rowland
"""
# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as soup
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import pandas as pd


def open_site():
    # use chrome to open site
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifiactions")
    driver = webdriver.Chrome(executable_path='PATH/TO/YOUR/CHROME/DRIVER',options=options)
    driver.get(r'https://www.amazon.com/ap/signin?accountStatusPolicy=P1&clientContext=261-1149697-3210253&language=en_US&openid.assoc_handle=amzn_prime_video_desktop_us&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.primevideo.com%2Fauth%2Freturn%2Fref%3Dav_auth_ap%3F_encoding%3DUTF8%26location%3D%252Fref%253Ddv_auth_ret')
    try: 
        logonElement = WebDriverWait(options, 5).until(EC.presence_of_element_located((By.ID, 'ap_email')))
        print("found element; proceeding")
    except TimeoutException:
        print("took too long to open page")
        return
    # Login
    driver.find_element_by_id('ap_email').send_keys('ENTER YOUR EMAIL ID')
    driver.find_element_by_id('ap_password').send_keys('ENTER YOUR PASSWORD',Keys.ENTER)
    sleep(2)
    search(driver)    
    
def search(driver):
    # twotabsearchtextbox
    pass
    
if __name__ == "__main__":
    print("Hello World")
    open_site()