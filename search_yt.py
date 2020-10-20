from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
from time import sleep
import urllib

#search string is query term for YT search, 
#page number is the number of result page (from search)
def youtube_search(search_string, page_number): 
    options = Options()
    options.add_argument("start-maximized")
    options.add_argument("--headless")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)

    textToSearch = search_string
    page_number = urllib.parse.quote(page_number)
    query = urllib.parse.quote(textToSearch)
    #query = urllib.parse.quote(textToSearch)
    url = "https://www.youtube.com/results?search_query=" + query +"&page=" + page_number
    driver.get(url)
    # driver.execute_script("window.scrollTo(0, 3000)")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # time.sleep()
    container=driver.find_elements_by_xpath('//*[(@id = "video-title")]')

    contain_top=container

    links=[]
    for page in contain_top:
        url=page.get_attribute("href")
        links.append((url,page.text))

    # print((links))
    driver.close()
    total_vid = len(links)

    return links, total_vid

print(youtube_search("ecommerce","1"))