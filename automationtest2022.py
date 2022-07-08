from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
from time import sleep

driver = webdriver.Chrome("/Users/defnedoken/Documents/chromedriver")

if 3==2:
    time.sleep(2)
    driver.get('https://www.middlebury.edu')

    AdmissionsURL = "//a[@href='http://www.middlebury.edu/admissions']"
    ButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(AdmissionsURL))
    ButtonElement.click()

    ApplyURL = "//a[@href='https://www.middlebury.edu/college/admissions/apply/instructions']"
    ButtonElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(ApplyURL))
    ButtonElement.click()

    AppFee = "//dt[contains(text(), 'Application Fee')]/following::dd[1]"
    Fee = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(AppFee))
    print (Fee.text)

if 3==2:
    time.sleep(2)
    driver.get('https://www.pcmag.com/deals')
    Apple = "//a[contains(text(), 'Apple')]"
    AppleDeals = driver.find_elements_by_xpath(Apple)

    for value in AppleDeals:
        print(value.text)

if 3==2:
    time.sleep(2)
    driver.get('https://www.usnews.com/best-colleges/rankings/national-universities')
    Tuition = "//dd[contains(text(), '$')]"
    Tuitions = driver.find_elements_by_xpath(Tuition)

    for value in Tuitions:
        val = value.text
        newval = (val[1:])
        price = int(newval.replace(',', ''))
        if (price < 60000):
            print(price)
if 3==2:
    time.sleep(2)
    driver.get('https://reslife.brown.edu/housing-options/residence-halls/special-interest')
    Specialty = "//h2[@class='section_break_header_title']"
    Specialties = driver.find_elements_by_xpath(Specialty)
    print("Types of Special Interest Housing at Brown University")
    for value in Specialties:
        type = value.text
        print(type)

if 3==3:
    time.sleep(2)
    driver.get('https://www.target.com/c/crayons-writing-supplies-school-office/-/N-ln37z')
    priceelement = "//div[@data-test='current-price']/span"
    time.sleep(5)
    Prices = driver.find_elements_by_xpath(priceelement)
    price_list = list()
    for value in Prices:
        try:
            val = value.text
            price = float(val[1:])
            price_list.append(price)
        except Exception as e:
            continue
    price_list.sort()
    Cheap = (str(price_list[:1]).replace('[', ''))
    Cheapest = Cheap.replace(']', '')
    productTitle = "//span[contains(text(), '" + Cheapest + "')]/ancestor::div[4]/preceding::div[8]/child::a"
    ProductTitle = driver.find_element_by_xpath(productTitle)
    print("The cheapest product is " + ProductTitle.text, " at $" + Cheapest)





    

