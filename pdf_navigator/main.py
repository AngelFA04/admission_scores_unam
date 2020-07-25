"""
This script get all the links from the pdfs and the html 
pages (change the name of the folder-module).
It will be called by a function in Scrapy to get the links of 
all  the areas and then get the links per career.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time 
import csv

class LinkGetter():
    """
    This function extracts the links from PDF files and HTML files.
    The links are all
    """
    pass

    def extract_links_pdf(self, link, xpath):
        pass
    
    def extract_links_html(self, link, xpath):
        pass

    def extract_links():
        """
        This function generalize the behavior of the previous ones.
        """
        pass

def extract_links(pdf_link):
    try:
        browser.get(pdf_link)
        #Scroll all the pages
        html = browser.find_element_by_tag_name('html')
        SCROLL_PAUSE_TIME = 0.2
        i = 0
        browser.implicitly_wait(9) #Waits 9 seconds
        while i < 1000:
            # Scroll down to bottom
            html.send_keys(Keys.ARROW_DOWN)
            i += 1

        browser.implicitly_wait(5) #Waits 5 seconds

        links = browser.find_elements_by_xpath('//a[contains(@title, "resultados")]')
        
        #This list may change
        links_results = [link.get_attribute('title') for link in links]

        if len(links_results) == 0:
            print(f'There are not results in this link: {pdf_link}')
        print(f'Succesful extraction from {pdf_link}')
        return links_results
        #print(links_results)
    except selenium.common.exceptions.WebDriverException as e:
        try:
            #click the botton to accept the conection
            button = browser.find_element_by_id('enableTls10Button')
            button.click()
            browser.implicitly_wait(5) #Waits 5 seconds
            extract_links(pdf_link)
        except selenium.common.exceptions.WebDriverException as e:
            print(f'There was an error in {pdf_link}.\n\t{e}')
        return []


LINKS = [
    'https://escolar1.unam.mx/Febrero2019/resultados.pdf', 
    ]

XPATHS = {
    'resultados_nuevos':'//a[contains(@title, "resultados")]',
    'atributo_nuevos':'',
    'atributo:viejos':'',
    'resultados_antiguos':'',
}

if __name__ == "__main__":
    links_area_results = []
    #File with links
    with open('last_years_results.csv') as f:
        reader = csv.reader(f)
        data = list(reader)
 
    data = [d[0] for d in data]
    #import pdb; pdb.set_trace()

    # Prepare the browser to scrape de PDFs
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    links_pdfs = data

    for link in links_pdfs:
        links_area_results.extend(extract_links(link))
    browser.close()

    links_area_results = list(set(links_area_results))
    # Show all the linkds
    for e in links_area_results:
        print(f'-- {e}')
    
    print(f'Total de links: {len(links_area_results)}')