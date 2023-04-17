#http://quote.stockstar.com/stock/stock_index.htm
#所获取的数据只是沪A的
#接下来获取剩下三个板块的并存入数据库
import scrapy
from stockstar.items import StockstarItem

class StockSpider(scrapy.Spider):
    name = 'stock'
    allowed_domains = ['quote.stockstar.com']  # 域名
    start_urls = ['http://quote.stockstar.com/stock/stock_index.htm']  # 启动的url

    def parse(self, response):
        """
        解析函数
        :param response:
        :return:
        """
        item = StockstarItem()
        styles = ['沪A', '沪B', '深A', '深B']
        index = 0
        for style in styles:
            # print('********************本次抓取' + style[index] + '股票********************')
            print(str(index))
            ids = response.xpath(
                '//div[@class="w"]/div[@class="main clearfix"]/div[@class="seo_area"]/div['
                '@class="seo_keywordsCon"]/ul[@id="index_data_' + str(index) + '"]/li/span/a/text()').getall()
            names = response.xpath(
                '//div[@class="w"]/div[@class="main clearfix"]/div[@class="seo_area"]/div['
                '@class="seo_keywordsCon"]/ul[@id="index_data_' + str(index) + '"]/li/a/text()').getall()
            # print('ids = '+str(ids))
            # print('names = ' + str(names))
            for i in range(len(ids)):
                item['stock_type'] = style
                item['stock_id'] = str(ids[i])
                item['stock_name'] = str(names[i])
                yield item
