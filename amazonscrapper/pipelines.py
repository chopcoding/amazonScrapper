# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import csv
class AmazonPipeline:
    def open_spider(self, spider):
        self.file = open('test.csv', 'w')

    def close_spider(self, spider):
        self.file.close()
    def process_item(self, item, spider):
        with self.file:
            fieldnames = ['product_name', 'product_author', 'product_price']
            writer = csv.DictWriter(self.file, fieldnames=fieldnames)
            writer.writeheader()
            temps=ItemAdapter(item).asdict()
            writer.writerow(temps)
            # writer.writerow(item.asdict())
            

            # line = json.dumps(ItemAdapter(item).asdict()) + "\n"
            # self.file.write(line)
            return item
