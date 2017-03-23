# -*- coding: utf-8 -*-
import scrapy
from koovs.items import KoovsItem

class KoovsSpiderSpider(scrapy.Spider):
    name = "koovs_spider"
    allowed_domains = ["koovs.com"]
    start_urls = ['http://koovs.com/men/brands','http://www.koovs.com/women/brands']

    def parse(self, response):
        BRANDS_URLS_XPATH = "//div[contains(@class,'brandsBlockList')]//a//@href"
        brand_urls = response.xpath(BRANDS_URLS_XPATH).extract()
        for url in brand_urls:
            yield scrapy.Request(url=url,callback=self.parse_brands)
    def parse_brands(self, response):
        ITEM_URLS_XPATH = "//div[@class='prodDescp']//a[@class='product_url']/@href"
        item_urls = response.xpath(ITEM_URLS_XPATH).extract()
        if item_urls:
            for link in item_urls:
                yield scrapy.Request(link, callback=self.parse_item)
        NEXT_PAGE_XPATH = "//div[@id='search_page_pagination_bottom']//a[position()=(last())]/@href"
        next_page = response.xpath(NEXT_PAGE_XPATH).extract()
        if next_page:
            yield scrapy.Request(next_page[0],callback=self.parse_brands)
    def parse_item(self, response):
        BRAND_URL_XPATH = "//span[@class='brandSection']//a/@href"
        BRAND_NAME_XPATH = "//span[@class='brandSection']//a/text()"
        ITEM_NAME_XPATH = "//span[@itemprop='name']/text()"
        ITEM_PRICE_XPATH = "//span[@itemprop='price']/text()"
        MAIN_IMAGE_XPATH = "//img[@itemprop='image']/@src"


        name = response.xpath(ITEM_NAME_XPATH).extract_first()
        url = response.url.split('?')[0]
        brand = response.xpath(BRAND_NAME_XPATH).extract_first()
        brand_url = response.xpath(BRAND_URL_XPATH).extract_first()
        price = response.xpath(ITEM_PRICE_XPATH).extract_first()
        img = response.xpath(MAIN_IMAGE_XPATH).extract_first()

        item = KoovsItem(
            name = name,
            url = url,
            brand = brand,
            brand_url = brand_url,
            price = price,
            img = img
        )
        yield item
