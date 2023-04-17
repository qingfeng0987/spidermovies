# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockstarItem(scrapy.Item):
    """
    定义需要爬取的字段名称
    """
    # define the fields for your item here like:
    # name = scrapy.Field()
    # stock_type = scrapy.Field()  # 股票类型
    # stock_id = scrapy.Field()  # 股票ID
    # stock_name = scrapy.Field()  # 股票名称

    # name=scrapy.Field()
    # url = scrapy.Field()# 编剧
    # bj = scrapy.Field()# 图片
    # img = scrapy.Field()# 导演

    href = scrapy.Field()
    title = scrapy.Field()
    detail = scrapy.Field()
