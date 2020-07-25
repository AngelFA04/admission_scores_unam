from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import csv

def extract_links(pdf_link):
    browser.get(pdf_link)
    #Hace falta hacer scroll hasta las ultimas paginas
    html = browser.find_element_by_tag_name('html')
    SCROLL_PAUSE_TIME = 0.2
    i = 0
    while i < 1000:
        # Scroll down to bottom
        html.send_keys(Keys.ARROW_DOWN)
        i += 1

    browser.implicitly_wait(5) #Waits 10 seconds

    links = browser.find_elements_by_xpath('//a[contains(@title, "resultados")]')

    links_results = [link.get_attribute('title') for link in links]

    print(links_results)

    return links_results


LINKS = [
    'https://escolar1.unam.mx/Febrero2019/resultados.pdf', 
    ]

if __name__ == "__main__":
    
    data = csv.reader('resultados-años-pasados.txt')
    
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    _links = []
    for link in LINKS:
        _links.extend(extract_links(link))
    browser.close()

    for e in _links:
        print(f'-- {e}')
    
    print(f'Total de links: {len(_links)}')
    data.
    print(data)