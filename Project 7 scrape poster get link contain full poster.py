from selenium import webdriver

from bs4 import BeautifulSoup
import requests

driver = webdriver.PhantomJS("E:\\Udemy web scraping\\phantomjs-2.1.1-windows\\bin\\phantomjs")
driver.get("http://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2398042102&pf_rd_r=1GVHSWA3013388XHX6RX&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1")
html_text = driver.page_source
bsObj = BeautifulSoup(html_text , 'lxml')


div = bsObj.find("div" , class_="poster")

a = div.find("a")
url = "http://www.imdb.com"+a["href"]

driver.get(url)

soup = BeautifulSoup(driver.page_source , "lxml")

div1 = soup.find_all("div" , class_ = "pswp__zoom-wrap")

img = div1[1].find_all("img")

f = open("shown_Shank_poste.jpg" , "wb")
f.write(requests.get(img[1]["src"]).content)
f.close()


driver.quit()
