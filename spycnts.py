import scrapy

class SpycntsSpider(scrapy.Spider):
    name = 'spycnts'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['https://books.toscrape.com/']


    def parse(self, response):
        lst_books = response.xpath("//article[@class='product_pod']")
        
        for book in lst_books:
            title = book.xpath(".//h3//@title").extract_first()
            yield{
                "Title": title,
            }
        
        nxt_page = response.xpath("//li[@class='next']/a/@href").extract_first()
        if nxt_page:
            yield response.follow(nxt_page, callback=self.parse)