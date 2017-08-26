from selenium import webdriver

from bs4 import BeautifulSoup

class Film():

    def __init__(self):
        self.title = ""
        self.year = ""
        self.rank = ""
        self.link = ""
        


film_list = []

def film_list_details():
    
    driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
    driver.get("http://www.imdb.com/chart/top?ref_=nv_mv_250_6")
    html_text = driver.page_source
    bsObj = BeautifulSoup(html_text , 'lxml')

    table = bsObj.find("table" , class_="chart full-width")

    for td in table.find_all("td" , class_ = "titleColumn"):
        full_title = td.text.strip().replace("\n","").replace("      "," ")

        rank = full_title.split(".")[0]
        title = full_title.split(".")[1].split("(")[0]
        year = full_title.split("(")[1][:-1]

        a = td.find("a")
        link = a["href"]
        new_film = Film()
        new_film.title = title
        new_film.rank = rank
        new_film.year = year
        new_film.link = link

        film_list.append(new_film)



    driver.quit()
    return (film_list)

film_list = film_list_details()

for f in film_list:
    print (f.title)
    print (f.rank)
    print (f.year)
    print (f.link)


    
