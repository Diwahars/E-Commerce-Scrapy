from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose
import urllib
from imageURL import getURL
from urlparse import urlparse
import json

class ImageSpider(BaseSpider):

    name = "ImageJabong123"
    allowed_domains = []
    start_urls=getURL()
    custom_settings={"ITEM_PIPELINES" : ["scraper_app.pipelines.ImagePipeline"]}
    item_fields = {}
    folderName='/home/siddhantmanocha/Projects/testImages/'

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        """
        with open(self.folderName+(response.url).replace('/','_'),'w+') as f:
            f.write(response.body)
        print self.folderName
        obj={}

        print "success"

        yield obj
