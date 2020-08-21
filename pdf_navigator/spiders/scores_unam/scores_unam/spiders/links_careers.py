import scrapy
from ..items import Career

class SpiderDataCareer(scrapy.Spider):
    name = 'careers'
    
    #URLs saved in CSV. Urls from each career
    start_urls = [

        'https://www.dgae.unam.mx/Febrero2020/resultados/26.html'
    ]

    def parse(self, response):
        """
        This function will receive all the links extracted from the spider links_areas
        """
        pass
        
        #All the next block should be in other function
        post_careers = response.xpath('//div[@class="post-preview"]')
        for post in post_careers:
            links_careers = post.xpath('./p/a[contains(@class, "btn btn-link")]/@href').getall()
            name_career = post.xpath('./h3/text()').get().split()[0]
            name_faculty = post.xpath('./p/a[contains(@class, "btn btn-link")]/text()').get()

            import pdb; pdb.set_trace()
            for link in links_careers:
                yield response.follow(link, callback=self.parse_career_page, 
                cb_kwargs={'url': response.urljoin(link), 'name_career': name_career})



    def parse_career_page_new(self, response, *args, **kwargs):
        """
        Method to extract all the scores from each career page. 
        This one is designed for the new websites (2017-Present)
        """
        pass
        #Select everything not only the text
        aspirants_raw_scores = response.xpath('//table/tbody//tr//td[2]')
        aspirants_raw_status = response.xpath('//table/tbody//tr//td[3]')

        scores = []
        #Cleaning data
        for aspirant in aspirants_raw_scores:
            scores.append( (aspirant.xpath('./text()').get(default='')) )

        import pdb; pdb.set_trace()


        scores = response.xpath('//table/tbody//tr//td[2]/text()').getall()
        scores = list(map(str.strip, scores))
        
        #Yield an item with the data
        name = response.xpath()

        career = Career()
        #Fill career with data
        #career['area'] = ...
        #career['name'] = ...

        yield career


    def parse_career_page_old():
        """
        Method to extract all the scores from each career page. 
        This one is designed for the old websites (2010-2016).
        This method will extract the data bases mostly in regex.
        """

    
