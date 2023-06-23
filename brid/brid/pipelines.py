# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.mail import MailSender
from dotenv import load_dotenv
load_dotenv()
import os
email = os.environ["EMAIL"]
password = os.environ["PASSWORD"]
mailer = MailSender(mailfrom="*@gmail.com", smtphost="smtp.gmail.com", smtpport=587, smtppass=password, smtpuser=email)
class BridPipeline:
    def process_item(self, item, spider):

        adapter = ItemAdapter(item)
        if adapter.get("stock") != "instock":
            adapter["stock"] = "NOT IN STOCK"
            print("not sending email")
            print("*******************************")
        else :
            print("in stock, sending email")
            print("********************************")
            mailer.send(to=[email], subject="Bridget in stock", body="Click https://www.etsy.com/shop/SGFDevices")
        return item
    def close_spider(self, item):
        pass
