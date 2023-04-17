# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter



import pymysql


class StockstarPipeline:
    def process_item(self, item, spider):
        # print('股票类型>>>>' + item['stock_type'] + '股票代码>>>>' + item['stock_id'] + '股票名称>>>>' + item['stock_name'])
        return item

    # fp = None
    #
    # def open_spider(self, spider):
    #     self.fp = open('dianying.txt', mode='w', encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     href = item["href"]
    #     title = item["title"]
    #     self.fp.write(title + href + '\n')
    #     # detail = item["detail"]
    #     # self.fp.write(title + href + detail + '\n')
    #     return item
    #
    # def close_spider(self, spider):
    #     self.fp.close()


# class MySQLPipeline():
#     # 开始爬取数据之前被调用
#     # 读取配置文件，初始化连接以及游标
#     def open_spider(self, spider):
#         host = spider.settings.get("MYSQL_DB_HOST", "127.0.0.1")
#         port = spider.settings.get("MYSQL_DB_PORT", 3306)
#         dbname = spider.settings.get("MYSQL_DB_NAME", "emp")
#         user = spider.settings.get("MYSQL_DB_USER", "root")
#         pwd = spider.settings.get("MYSQL_DB_PASSWORD", "123456")
#
#         self.db_conn = pymysql.connect(host=host, port=port,
#                                        db=dbname, user=user, password=pwd)
#         self.db_cur = self.db_conn.cursor()
#     # 每解析完一个 item 调用
#     # 插入数据
#
#     def process_item(self, item, spider):
#         values = (
#             item['stock_id'],
#             item['stock_name'],
#             item['stock_type']
#         )
#         sql = "insert into stock(stock_id,stock_name,stock_type) values(%s,%s,%s)"
#         self.db_cur.execute(sql, values)   #执行sql语句
#         return item
#
#
#     # 爬取完全部数据后被调用
#     # 提交数据，释放连接
#     def close_spider(self, spider):
#         self.db_conn.commit()
#         self.db_cur.close()
#         self.db_conn.close()

