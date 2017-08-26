from selenium import webdriver

from bs4 import BeautifulSoup
import requests

class Posters():

    def __init__(self):
        self.title = ""
        self.href = ""
        






def get_pages_link():
    
    driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
    url = "/gallery/rg1624939264?ref_=nv_ph_lp_2"
    driver.get("http://www.imdb.com"+url)
    html_text = driver.page_source
    bsObj = BeautifulSoup(html_text , 'lxml')
    page_list = []
    page_list.append(url)
    span = bsObj.find("span" , class_ = "page_list")
    for a in span.find_all("a"):
       # print(a["href"]+ '----> '+ a.text)
        page_list.append(a["href"])

    driver.quit()

    return page_list
    
def get_first_page_posters():

    url = get_pages_link()
    for u in url:
    
        driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
        driver.get(u)
        html_text = driver.page_source
        bsObj = BeautifulSoup(html_text , 'lxml')

        div = bsObj.find("div" , {"id":"media_index_thumbnail_grid"})
        for a in div.find_all("a"):
            
        #a = div.find("a")
            href = "http://www.imdb.com"+a["href"]

            driver.get(href)

            soup = BeautifulSoup(driver.page_source , "lxml")
            div = soup.find_all("div" , class_ = "pswp__item")
            img = div[2].find_all("img")
            print (img[1]["src"])

            p = open("New folder/{0}.jpg".format(a["title"].replace(":" , ""))  , "wb")
            p.write(requests.get(img[1]["src"]).content)
            p.close()


    driver.quit()
    
get_first_page_posters()

    



#get_pages_link()

        
    

