import scrapy
from scrapypyppeteer.items import ScrapypyppeteerItem
from gerapy_pyppeteer import PyppeteerRequest

class YiqingSpider(scrapy.Spider):
    name = 'yiqing'
    allowed_domains = ['www.nhc.gov.cn']
    
    # base_url = 'https://dynamic5.scrape.center/page/{page}'
    max_page = 33
    
    def start_requests(self):
        # start_url = f'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd.shtml'
        # yield PyppeteerRequest(start_url, callback=self.parse, wait_for='.zxxx_list')

        for page in range(2, self.max_page + 1):
            base_url = f'http://www.nhc.gov.cn/xcs/yqtb/list_gzbd_{page}.shtml'
            yield PyppeteerRequest(base_url, callback=self.parse, wait_for='.zxxx_list')


    def parse(self, response):
       quotes = response.css('.zxxx_list li')
       for quote in quotes:
           one_url = quote.css('a::attr(href)').extract_first()
           new_url = 'http://www.nhc.gov.cn'+one_url
           yield PyppeteerRequest(new_url, callback=self.sub_parse, wait_for='#xw_box')

    def sub_parse(self, response):
        item = ScrapypyppeteerItem()
        item['title'] = response.css('.tit::text').extract_first()
        all_text = response.xpath('//*[@id="xw_box"]//text()').getall()

        temp = ''
        for one_text in all_text:
            if ('\n' not in one_text) and ('window' not in one_text):
                temp += one_text

        item['text'] = temp
        yield item