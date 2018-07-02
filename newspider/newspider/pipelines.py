# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BaidustocksPipeline(object):
    def process_item(self, item, spider):
        return item

class BaidustocksInfoPipeline(object):
    def open_spider(self, spider):
        self.f = open('BaiduStockInfo.txt', 'w')

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        try:
            line = str(dict(item)) + '\n'
            self.f.write(line)
        except:
            pass
        return item

class PicPipeline(object):

    def open_spider(self,spider):
        self.file=open('category_info.jl','w',encoding='utf-8')

    def close_spider(self,spider):
        self.file.close()

    def process_item(self,item,spider):

        try:
            content = str(dict(item))
            self.file.write(content+'\n')
        except:
            pass

        return item