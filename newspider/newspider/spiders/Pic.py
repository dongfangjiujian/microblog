import scrapy
from ..items import PicItem
from scrapy.http.response import  urljoin


class getPic(scrapy.Spider):
    name = 'pic'
    base_urls="http://www.ivsky.com/tupian/index_{}.html"
    def start_requests(self):

        for i in range(1,10):
            url = self.base_urls.format(i)
            print(url)
            yield scrapy.Request(url,self.parse)

    def parse(self, response):
        category=response.css('div.il_img')

        for c in category:
            if c is not  None:
                item = PicItem()
                item["category_title"]= c.css('a::attr(title)').extract_first()
                category_url = c.css('a::attr(href)').extract_first()
                item["category_url"] = response.urljoin(category_url)
                yield item
                # yield {
                #     'title':category_name,
                #     'url':category_url
                # }
                #yield scrapy.Request(url=url,callback=self.getCategory)

    def getCategory(self,response):
        #print(response.meta)
        print("response.url=="+response.url)


