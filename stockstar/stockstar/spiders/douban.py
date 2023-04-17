
import scrapy
from stockstar.items import StockstarItem


class StockSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']


    def parse(self, response):
        for row in response.xpath('//*[@id="content"]/div/div[1]/ol/li/div'):
            item = StockstarItem()  # 实例化
            item['name'] = row.xpath("div[2]/div/a/span[1]/text()").extract()[0]  # 获取电影名
            item['img'] = row.xpath("div[1]/a/img/@src").getall()  # 图片链接
            item['url'] = row.xpath("div/a/@href").extract()[0]  # 电影链接
            yield scrapy.Request(item['url'], meta={'item': item}, callback=self.parse_detail)
        # 爬取250条的
        '''next_url = response.xpath("//span[@class='next']/a")
        if next_url:
            next_url = "https://movie.douban.com/top250" + next_url.xpath("@href").get()
            yield scrapy.Request(next_url, callback=self.parse)'''

    def parse_detail(self, response):
        item = response.meta['item']  #item为字典的key
        # item['bj'] = response.xpath("// *[ @ id = 'info'] / span[1] / span[2] / a / text()").extract()
        #一直没有数据爬出
        item['bj'] = response.xpath("//div[@id='info']/span[2]/span[2]/a/text()").get()  # 导演
        yield item
