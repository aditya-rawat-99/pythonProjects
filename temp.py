from bs4 import BeautifulSoup as BS
import requests, sys, threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("http://www.fb.com")
def loginFB(browser):
    email = browser.find_element_by_id("email")
    email.send_keys(sys.argv[1])
    
    password = browser.find_element_by_id("pass")
    password.send_keys(sys.argv[2])

    password.submit()

    """try:
        login = browser.find_element_by_id("u_0_3")
        login.click()
    except:
        login = browser.find_element_by_id("u_0_2")
        login.click()"""
    searchBox = browser.find_element_by_class_name("_1frb")
    searchBox.send_keys(sys.argv[3] + " " + sys.argv[4])
    searchBox.submit()

    match = browser.find_element_by_css_selector("a._1ii5._2yez")
    match.click()
    
if len(sys.argv) >= 2:
    loginThread = threading.Thread(target = loginFB, args = [browser])
    loginThread.start()
