"""
This script get all the links from the pdfs and the html 
pages (change the name of the folder-module).
It will be called by a function in Scrapy to get the links of 
all  the areas and then get the links per career.
"""

import csv
import time

import pandas as pd
import selenium
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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

def main():
    pass



def extract_links(pdf_link):

    links = []

    try:
        browser.get(pdf_link)
        html = browser.find_element_by_tag_name('html')
        
       # _zoom_out(browser, html)
        browser.set_context("chrome")
        #Send the key combination to the window itself rather than the web content to zoom out
        #(change the "-" to "+" if you want to zoom in)
        for _ in range(12):
            browser.find_element_by_tag_name('html').send_keys(Keys.CONTROL, '-')

        browser.set_context("content")

        reps = 500
        browser.implicitly_wait(4) #Waits 9 seconds
        for _ in range(reps):
            # Scroll down to bottom
            html.send_keys(Keys.ARROW_DOWN)
            browser.implicitly_wait(0.01)

        browser.implicitly_wait(3) #Waits 9 seconds
        
        links = [link.get_attribute('title') for link in browser.find_elements_by_xpath('//a[contains(@title, "resultados")]')]

        for _ in range(reps):
            # Scroll down to bottom
            html.send_keys(Keys.ARROW_UP)
            browser.implicitly_wait(0.01) #Waits 9 seconds

        
        browser.implicitly_wait(3) #Waits 9 seconds
        links.extend( 
            [link.get_attribute('title') for link in browser.find_elements_by_xpath('//a[contains(@title, "resultados")]')]
        )
        browser.implicitly_wait(3) #Waits 5 seconds

        #links = browser.find_elements_by_xpath('//a[contains(@title, "resultados")]')

        #import pdb; pdb.set_trace()

        if len(links) == 0:
            logger.info(f'There are not results in this link: {pdf_link}')
        else:
            logger.info(f'Succesful extraction from {pdf_link}')
        return links
        #print(links_results)
    except selenium.common.exceptions.WebDriverException as e:
        logger.warning(f'There was an error: {e}')
        try:
            #click the botton to accept the conection
            button = browser.find_element_by_id('enableTls10Button')
            button.click()
            browser.implicitly_wait(5) #Waits 5 seconds
            extract_links(pdf_link)
        except selenium.common.exceptions.WebDriverException as e:
            logger.warning(f'There was an error in {pdf_link}.\n\t{e}')
        
    return links


def _zoom_out(driver, html):
    #Set the focus to the browser rather than the web content
    driver.set_context("chrome")
    #Send the key combination to the window itself rather than the web content to zoom out
    #(change the "-" to "+" if you want to zoom in)
    for i in range(6):
        html.send_keys(Keys.CONTROL + "-")
    #Set the focus back to content to re-engage with page elements
    driver.set_context("content")


def _save_links(links):
    logger.info('Saving links into a CSV')
    df = pd.DataFrame(data={'links': links})
    ## Save files in a Pandas DataFrame
    print(df)
    ## Save files in 
    df.to_csv('links_areas.csv', index=False)
    pass
    


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
    logger.info('Open CSV of websites to extract data')
    with open('last_years_results.csv') as f:
        reader = csv.reader(f)
        data = list(reader)
    data = [d[0] for d in data]
    #import pdb; pdb.set_trace()

    # Prepare the browser to scrape de PDFs
    logger.info('Loading browser to extract data')
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    links_pdfs = data

    for link in links_pdfs:
        logger.info(f'Extracting links from {link}')
        if link.endswith('.pdf'):
            links_area_results.extend(extract_links(link))
        elif link.endswith('.html'):
           #Use another functions
            pass

    browser.close()

    links_area_results = list(set(links_area_results))
    _save_links(links_area_results)
    # Show all the linkds
    for e in links_area_results:
        print(f'-- {e}')
    
    print(f'Total de links: {len(links_area_results)}')
