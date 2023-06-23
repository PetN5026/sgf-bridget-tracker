import scrapy
from brid.items import BridItem


class BridgetSpider(scrapy.Spider):
    name = "bridget"
    allowed_domains = ["www.etsy.com"]
    start_urls = ["https://www.etsy.com/shop/SGFDevices"]

    def parse(self, response):

        brid_item = BridItem()
        instock = response.css("div.empty-state div ::text")
        if instock is not None:
            print("*************************************")
            print(instock.get().strip())
            brid_item["stock"] = instock.get().strip()
        else:
            brid_item["stock"] = "instock"

        yield brid_item


