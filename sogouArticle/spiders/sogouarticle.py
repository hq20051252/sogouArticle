# -*- coding: utf-8 -*-
import scrapy


class SogouarticleSpider(scrapy.Spider):
    name = "sogouarticle"
    allowed_domains = ["sogou.com"]
    start_urls = (
        'http://www.sogou.com/',
    )

    def parse(self, response):
        pass
