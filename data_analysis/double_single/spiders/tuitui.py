# -*- coding: utf-8 -*-
import scrapy


from double_single.items import DoubleSingleItem


class TuituiSpider(scrapy.Spider):
    name = 'tuitui'
    allowed_domains = ['chengdu.tuitui99.com']
    # for i in range(1, 101):
    #     start_urls = 'https://chengdu.tuitui99.com/Community/p%d.html&sp=30' % i

    def start_requests(self):
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'chengdu.tuitui99.com',
            'Content-Type': 'text/html; charset=utf-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }

        for i in range(1, 101):
            yield scrapy.Request(
                url='https://chengdu.tuitui99.com/Community/p%d.html&sp=30' % i,
                headers=headers,
                method='GET',
                callback=self.parse
            )

    def parse(self, response):
        house_item = DoubleSingleItem()
        info = response.xpath('//ul[@class="h_list"]')
        name = info.xpath('//div[@class="fl h_info"]/h3/a/@title').extract()
        place = info.xpath('//span[@id="comm"]/text()').extract()
        price = info.xpath('//div/div[2]/div/div[2]/div[@class="price"]/span/text()').extract()
        for j in range(30):
            house_item['name'] = name[j]
            house_item['place'] = place[j]
            house_item['price'] = price[j]
            yield house_item
