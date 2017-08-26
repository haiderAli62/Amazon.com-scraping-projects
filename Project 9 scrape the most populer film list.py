from selenium import webdriver

from bs4 import BeautifulSoup
import requests

driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
driver.get("http://www.imdb.com/chart/moviemeter?ref_=nv_mv_mpm_8")
html_text = driver.page_source
bsObj = BeautifulSoup(html_text , 'lxml')

def movies_list():
    movie_names = []
   # poster_href = []
    table = bsObj.find("table" , class_ = "chart full-width")
    tbody = table.find("tbody" , class_ = "lister-list")
    for tr in tbody.find_all("tr"):
        td = tr.find("td" , class_ = "titleColumn")
        a = td.find("a") 
        title = a.text
        print(title+"\n")
        movie_names.append(title)

      
        

    return movie_names
               

movies_list()
def movie_posters():
    poster_href = []
    table = bsObj.find("table" , class_ = "chart full-width")
    tbody = table.find("tbody" , class_ = "lister-list")
    for tr in tbody.find_all("tr"):
        
        tdPoster = tr.find("td" , class_ = "posterColumn")
        aPoster = tdPoster.find("a")
        print(aPoster["href"])
        poster_href.append(aPoster["href"])
    
   
    for p in poster_href:
        url = "http://www.imdb.com"+p
        driver.get(url)
        soup = BeautifulSoup(driver.page_source , "lxml")

        div = soup.find("div" , class_ = "slate_wrapper")
        innerDiv = div.find("div")
        a = innerDiv.find("a")

        print (a["href"])
        poster_href.append(a["href"])

    return poster_href


def download_poster(poster_href):

    for poster in poster_href:

        url = "http://www.imdb.com"+poster

        driver.get(url)
        soup = BeautifulSoup(driver.page_source , "lxml")

        div = soup.find_all("div" ,class_ = "pswp__zoom-wrap" )
        img = div[1].find("img" , class_ = "pswp__img")

        src = img["src"]

        f = open(".jpg"  , "wb")
        f.write(requests.get(src).content)
        f.close

        




                
        
        

        
    
