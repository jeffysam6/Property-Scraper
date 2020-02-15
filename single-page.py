import json

import csv

import pandas as pd

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

import re

from tabulate import tabulate

from time import sleep 




def main():
    

    #code for structured csv

    location = "kamothe"

    url = "https://www.99acres.com/"
    option = webdriver.ChromeOptions()
    option.add_argument("-incognito")
    # option.add_argument('--headless')
    driver = webdriver.Chrome(executable_path='chromedriver',chrome_options=option)
    driver.implicitly_wait(30)
    driver.get(url)
    search =  driver.find_element_by_id('keyword')
    search.send_keys(location)
    submit = driver.find_element_by_id('submit_query')
    submit.click()

    sleep(10)
    driver.implicitly_wait(50)




    post_list = driver.find_elements_by_xpath("//div[@class='pageComponent srpTop__tuplesWrap']/div[@class='pageComponent srpTuple__srpTupleBox srp']")

    print(post_list)

    with open('results.csv','w',encoding='utf-8') as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerow(["Total Price","Cost/Square Ft","Square Ft","Bedroom","Bathroom","Contact"])
        for i in post_list:
            link = i.find_element_by_id('srp_tuple_property_title').get_attribute('href')
            print(link)
            print(i.find_element_by_id('srp_tuple_price').text.split('\n'))
            print(i.find_element_by_id('srp_tuple_primary_area').text.split('\n'))
            print(i.find_element_by_id('srp_tuple_bedroom').text.split('\n'))
            writer.writerow([i.find_element_by_id('srp_tuple_price').text.split('\n')[0][2:]
                            ,i.find_element_by_id('srp_tuple_price').text.split('\n')[1][2:]
                            ,i.find_element_by_id('srp_tuple_primary_area').text.split('\n')[0]
                            ,i.find_element_by_id('srp_tuple_bedroom').text.split('\n')[0]
                            ,i.find_element_by_id('srp_tuple_bedroom').text.split('\n')[1]
                            ,i.find_element_by_id('srp_tuple_property_title').get_attribute('href')])

       

        # link = i.find_element_by_id('srp_tuple_property_title').get_attribute('href')
        # print(link)
        # print(i.find_element_by_id('srp_tuple_price').text.split('\n'))
        # print(i.find_element_by_id('srp_tuple_primary_area').text.split('\n'))
        # print(i.find_element_by_id('srp_tuple_bedroom').text.split('\n'))



    driver.implicitly_wait(30)

    driver.close()
    

   


main()