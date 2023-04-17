#http://quote.stockstar.com/stock/stock_index.htm
#所获取的数据只是沪A的
#接下来获取剩下三个板块的并存入数据库
import scrapy
from stockstar.items import StockstarItem

class StockSpider(scrapy.Spider):
    name = 'stocktest'
    allowed_domains = ['quote.stockstar.com']  # 域名
    start_urls = ['http://quote.stockstar.com/stock/stock_index.htm']  # 启动的url

    def parse(self, response):
        """
        解析函数
        :param response:
        :return:
        """
        item = StockstarItem()
        # styles = ['沪A', '沪B', '深A', '深B']

        indexs = [0,1,2,3]
        for index in indexs:
            if index==0:
                style='沪A'
                ids = response.xpath(
                    '//div[@class="w"]/div[@class="main clearfix"]/div[@class="seo_area"]/div['
                    '@class="seo_keywordsCon"]/ul[@id="index_data_' + str(index) + '"]/li/span/a/text()').getall()
                names = response.xpath(
                    '//div[@class="w"]/div[@class="main clearfix"]/div[@class="seo_area"]/div['
                    '@class="seo_keywordsCon"]/ul[@id="index_data_' + str(index) + '"]/li/a/text()').getall()
            if index == 1:
                style = '沪B'
                ids = response.xpath(
                    '//div[@class="w"]/div[@class="main clearfix"]/div[@class="seo_area"]/div['
                    '@class="seo_keywordsCon"]/ul[@id="index_data_' + str(index) + '"]/li/span/a/text()').getall()
                names = response.xpath(
                    '//div[@class="w"]/div[@class="main clearfix"]/div[@class="seo_area"]/div['
                    '@class="seo_keywordsCon"]/ul[@id="index_data_' + str(index) + '"]/li/a/text()').getall()
            if index == 2:
                style = '深A'
                ids = response.xpath(
                    '//div[@class="w"]/div[@class="main clearfix"]/div[@class="seo_area"]/div['
                    '@class="seo_keywordsCon"]/ul[@id="index_data_' + str(index) + '"]/li/span/a/text()').getall()
                names = response.xpath(
                    '//div[@class="w"]/div[@class="main clearfix"]/div[@class="seo_area"]/div['
                    '@class="seo_keywordsCon"]/ul[@id="index_data_' + str(index) + '"]/li/a/text()').getall()
            if index == 3:
                style = '深B'
                ids = response.xpath(
                    '//div[@class="w"]/div[@class="main clearfix"]/div[@class="seo_area"]/div['
                    '@class="seo_keywordsCon"]/ul[@id="index_data_' + str(index) + '"]/li/span/a/text()').getall()
                names = response.xpath(
                    '//div[@class="w"]/div[@class="main clearfix"]/div[@class="seo_area"]/div['
                    '@class="seo_keywordsCon"]/ul[@id="index_data_' + str(index) + '"]/li/a/text()').getall()

            for i in range(len(ids)):
                item['stock_type'] = style
                item['stock_id'] = str(ids[i])
                item['stock_name'] = str(names[i])
                yield item
