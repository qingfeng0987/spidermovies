import scrapy
from stockstar.items import StockstarItem
#有的时候深层次爬取不出内容，看哈主网址和第二层次网址的域名相同不
class StockSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.1905.com']  # 域名
    start_urls = ['https://www.1905.com/vod/list/n_1_t_1/o3.html?fr=vodhome_js_lx']

    url = 'https://www.1905.com/vod/list/n_1_t_1/o3p%d.html'
    page = 2

    def parse(self, response):
        divs = response.xpath('//*[@id="content"]/section[4]/div[@class="grid-2x grid-3x-md grid-6x-sm"]')
        for div in divs:
            href = div.xpath('a/@href')[0].extract()
            title = div.xpath('a/@title')[0].extract()
            item = StockstarItem()
            item["href"] = href
            item["title"] = title
            yield scrapy.Request(href, callback=self.parse_detail, meta={'item': item})
            # if self.page < 4:
            #     url = format(self.url % self.page)
            #     yield scrapy.Request(url, callback=self.parse)
            #     self.page += 1

#前面的数据都能准确爬出，但是到进一步解析就不能爬
    def parse_detail(self, response):
        detail = response.xpath('//*[@id="playerBoxIntroCon"]/text()')[0].extract()
        item = response.meta['item']
        item["detail"] = detail
        yield item