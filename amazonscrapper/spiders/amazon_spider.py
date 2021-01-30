import scrapy
from amazonscrapper.items import AmazonItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.com/s?bbn=2&rh=n%3A2%2Cp_n_publication_date%3A1250227011&dc&qid=1611827871&rnid=1250225011&ref=lp_2_nr_p_n_publication_date_1'
    ]

    def parse(self, response):
        '''
        does the scrapping work.
        '''
        items = AmazonItem()

        product_name = response.css('h2 a.a-link-normal::text').extract_first()
        product_author = response.css('.sg-col-12-of-20 .sg-col-12-of-20 .a-color-secondary .a-size-base:nth-child(2)').css('::text').extract()
        product_img_link = response.css('.s-image::attr(src)').extract()
        product_price = response.css('.a-spacing-top-small .a-price-fraction , .a-spacing-top-small .a-price-whole').css('::text').extract()
        product_stars = response.css('.aok-align-bottom span::text').extract()
        product_ratings = response.css('.a-row a .a-size-base::text').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_img_link'] = product_img_link
        items['product_price'] = product_price
        items['product_stars'] = product_stars
        items['product_ratings'] = product_ratings

        yield items
