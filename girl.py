# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import  XiaohuaItem
import  re
class GirlSpider(CrawlSpider):
    name = 'girl'
    allowed_domains = ['xiaohuar.com']
    start_urls = ['http://www.xiaohuar.com/2014.html']

    rules = (
        Rule(LinkExtractor(allow=r'/p-1-\d+.html'), callback='parse_page', follow=False),

    )
    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i

    # http: // www.xiaohuar.com / p - 1 - 64.html
    # 从单个页面进入详情页
    # http: // www.xiaohuar.com / s - 1 - 64. html  # p1 就可以进入相册那所有的 p变为s 加了个#p1
    def parse_page(self,response):
        scheme,domain=response.url.split('//')  #scheme=http:  domain=www.xiaohuar.com / p - 1 - 64.html
        detail_url=re.sub('p','s',domain)
        detail_url=scheme+'//'+detail_url+'#p1'

        request=scrapy.Request(
           url=detail_url,
            callback=self.parse_detail,

        )
        yield  request

    def parse_detail(self,response):
        name=response.xpath('//h1/text()').get()
        a_links=response.xpath('//div[@class="inner"]/a/@href').getall()
        image_urls=list(map(lambda x:response.urljoin(x),a_links))

        item=XiaohuaItem(name=name,image_urls=image_urls)
        yield item










