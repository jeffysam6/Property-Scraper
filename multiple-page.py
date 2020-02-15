import json

import csv

import pandas as pd

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup

import re

from tabulate import tabulate

from time import sleep 


def adding_post(post_list,writer):
    for i in post_list:
        link = i.find_element_by_id('srp_tuple_property_title').get_attribute('href')
        print(link)
            # print(i.find_element_by_id('srp_tuple_price').text.split('\n'))
            # print(i.find_element_by_id('srp_tuple_primary_area').text.split('\n'))
            # print(i.find_element_by_id('srp_tuple_bedroom').text.split('\n'))
        try:
            if(len(i.find_element_by_id('srp_tuple_price').text.split('\n'))==2 and 
                len(i.find_element_by_id('srp_tuple_primary_area').text.split('\n'))==2 and
                len(i.find_element_by_id('srp_tuple_primary_area').text.split('\n'))==2):
                    writer.writerow([i.find_element_by_id('srp_tuple_price').text.split('\n')[0][2:]
                                    ,i.find_element_by_id('srp_tuple_price').text.split('\n')[1][2:]
                                    ,i.find_element_by_id('srp_tuple_primary_area').text.split('\n')[0]
                                    ,i.find_element_by_id('srp_tuple_bedroom').text.split('\n')[0]
                                    ,i.find_element_by_id('srp_tuple_bedroom').text.split('\n')[1]
                                    ,i.find_element_by_id('srp_tuple_property_title').get_attribute('href')])
        except:
            print("Missing values")



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


    pages = driver.find_elements_by_xpath("//div[@class='Pagination__srpPageBubble list_header_semiBold']/a")

    with open('results.csv','w',encoding='utf-8') as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerow(["Total Price","Cost/Square Ft","Square Ft","Bedroom","Bathroom","Contact"])
        for page in range(0,len(pages)):

            p = pages[page].get_attribute('href')
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(p)

            post_list = driver.find_elements_by_xpath("//div[@class='pageComponent srpTop__tuplesWrap']/div[@class='pageComponent srpTuple__srpTupleBox srp']")

            adding_post(post_list,writer)

            sleep(10)
            driver.close()
            driver.switch_to.window(driver.window_handles[0])



    # post_list = driver.find_elements_by_xpath("//div[@class='pageComponent srpTop__tuplesWrap']/div[@class='pageComponent srpTuple__srpTupleBox srp']")

    # print(post_list)

    # with open('results.csv','w',encoding='utf-8') as f:
    #     writer = csv.writer(f,delimiter=',')
    #     writer.writerow(["Total Price","Cost/Square Ft","Square Ft","Bedroom","Bathroom","Contact"])
    #     for i in post_list:
    #         link = i.find_element_by_id('srp_tuple_property_title').get_attribute('href')
    #         print(link)
    #         print(i.find_element_by_id('srp_tuple_price').text.split('\n'))
    #         print(i.find_element_by_id('srp_tuple_primary_area').text.split('\n'))
    #         print(i.find_element_by_id('srp_tuple_bedroom').text.split('\n'))
    #         writer.writerow([i.find_element_by_id('srp_tuple_price').text.split('\n')[0][2:]
    #                         ,i.find_element_by_id('srp_tuple_price').text.split('\n')[1][2:]
    #                         ,i.find_element_by_id('srp_tuple_primary_area').text.split('\n')[0]
    #                         ,i.find_element_by_id('srp_tuple_bedroom').text.split('\n')[0]
    #                         ,i.find_element_by_id('srp_tuple_bedroom').text.split('\n')[1]
    #                         ,i.find_element_by_id('srp_tuple_property_title').get_attribute('href')])

       

        # link = i.find_element_by_id('srp_tuple_property_title').get_attribute('href')
        # print(link)
        # print(i.find_element_by_id('srp_tuple_price').text.split('\n'))
        # print(i.find_element_by_id('srp_tuple_primary_area').text.split('\n'))
        # print(i.find_element_by_id('srp_tuple_bedroom').text.split('\n'))



    # driver.implicitly_wait(30)

    # driver.close()
    

    # def get_name(comment_id):

    #     if(comment_id in d):

    #         return d[comment_id]

    #     else:
    #         url_2 = f"https://mobile.facebook.com/{comment_id}"
    #         driver.execute_script("window.open('');")
    #         sleep(10)
    #         driver.switch_to.window(driver.window_handles[1])
    #         driver.get(url_2)
    #         sleep(10)
    #         driver.implicitly_wait(30)
    #         names = driver.find_elements_by_class_name('_2b05')
    #         names_text = [x.text for x in names]
    #         comment_ids = driver.find_elements_by_xpath("//div[@class='_2b06']/div[@data-sigil='comment-body']")
    #         for i,j in enumerate(comment_ids):
    #             d[j.get_attribute('data-commentid')] = names_text[i]

    #         driver.close()
    #         driver.switch_to.window(driver.window_handles[0])

    #         return d.get(comment_id,None)









    # with open('results2.csv','w',encoding='utf-8') as f:
    #     writer = csv.writer(f,delimiter=',')
    #     writer.writerow(["Facebook Post ID","Facebook Comment ID","Facebook Comment Content","Posted By","Created Date and Time"])

    #     for i in comment_data:

    #         if("comments" in i):

    #             for j in i["comments"]['data']:

    #                 # print(i['id'],j['id'],j['message'],type(j['id']),j['created_time'])
    #                 writer.writerow([i['id'],j['id'],j['message'],get_name(j['id']),j['created_time']])


    #         else:
    #             writer.writerow([i['id'],"Na N","Na N","Na N"])





    # with open('data.json','w') as f:
    #     json.dump(videos['videos']['data'],f)

    # df = pd.read_json('data.json')
    
    # df.to_csv("results.csv")


main()