import scrapy


class PharmeasySpiderSpider(scrapy.Spider):
    name = 'pharmeasy_spider'
    allowed_domains = ['pharmeasy.in']
    start_urls = ['https://pharmeasy.in/health-care/personal-care-89']

    def parse(self, response):
        # Extracting product details
        products = response.css('.ProductCard_productCardWrapper__7UI_Q')

        for product in products:
            # Extracting product name
            name = product.css('a.ProductCard_displayBlock__Ovf5P').attrib['title']
            
            # Extracting product price
            price = product.css('.ProductCard_salePrice__iLWF7.ProductCard_otcListingSalePrice__x8Y_C::text').getall()



            yield {
                'name': name,
                'price': price
            }

