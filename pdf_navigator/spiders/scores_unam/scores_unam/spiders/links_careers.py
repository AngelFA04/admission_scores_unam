import scrapy


class DataCareer(scrapy.Spider):
    name = 'careers'
    
    #URLs saved in CSV 
    start_urls = [
        'https://www.dgae.unam.mx/Febrero2020/resultados/26.html'
    ]

    def parse(self, response):

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
        #item
        yield 
        {
            name:'',

        }

    def parse_career_page_old(){

    }
