from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/SHIVANSHU/Desktop/python/chromedriver")
browser.get(START_URL)
time.sleep(10)
def scrape():
    headers = ["v mag", "Proper_name", "Brayer_designation", "Distance(in_light_year)", "Spectral_Class","Mass","Radius","Luminocity"]
    Star_data = []

    Soup=BeautifulSoup(browser.page_source,"html.parser")
    for td_tag in Soup.find_all("td"):
        tr_tag=td_tag.find_all("tr")
        temp_list=[]
        for index,tr__tag in enumerate(tr_tag):
            if index==0:
                temp_list.append(tr__tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.append(tr_tag.contents[0])
                except:
                    temp_list.append(" ")
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("empty2.csv","w")as f:
        csvwriter=csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(Star_data)

            

scrape()
