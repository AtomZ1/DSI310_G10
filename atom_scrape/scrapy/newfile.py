from gc import callbacks
import scrapy
import re
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#https://www.vogue.co.uk/fashion
#https://www.vogue.co.uk/fashion/article/other-stories-awake-mode-collaboration
#https://www.vogue.co.uk/fashion/article/kitten-heels-trend

class fileSpider(CrawlSpider):
    name = "file"
    allowed_domains = ['www.vogue.co.uk']
    start_urls = ['https://www.vogue.co.uk/fashion',]

    custom_settings = {
        'DEPTH_LIMIT': 1
    }

    rules = (
        Rule(LinkExtractor(allow='fashion' , deny='article')),
        Rule(LinkExtractor(allow='article'), callback='parse_links')
    )

    def parse_links(self, response):
        yield{
            'name': response.css('div.SplitScreenContentHeaderTitleBlock-hkbQxz.kmTHjj h1::text').get(),
            'grouping' : response.css('div.RubricWrapper-cSwECA.eimlmX.rubric.SplitScreenContentHeaderRubric-lcYYrD.koRKTN span::text').get(),
            'author': response.css('span.BylineName-cKjYhk.cmNGOq.byline__name a::text').get(),
            'time': response.css('div.SplitScreenContentHeaderTitleBlock-hkbQxz.kmTHjj time::text').get(),
        }

#(div.RubricWrapper-cSwECA.eimlmX.rubric.SplitScreenContentHeaderRubric-lcYYrD.koRKTN span::text)
#(div.ContentHeaderRubric ">
# (div.SplitScreenContentHeaderTitleBlock-hkbQxz.kmTHjj h1::text)

#('div.BylinesWrapper-hlZHyb.jKYZBu.bylines.SplitScreenContentHeaderByline-iCFlWP.hgnfCk')
#('p.BylineWrapper-ijrfvU.fCIMOg.byline.bylines__byline
#('span.BylineName-cKjYhk.cmNGOq.byline__name a::text')

#('div.BylinesWrapper-hlZHyb.jKYZBu.bylines.SplitScreenContentHeaderByline-iCFlWP.hgnfCk')
#('div.SplitScreenContentHeaderTitleBlock-hkbQxz.kmTHjj time::text')