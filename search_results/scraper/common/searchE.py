# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from search_results.scraper.common.searchEngines import SearchEngineResultSelectors
from search_results.scraper.common.searchEngines import BaiduSelectors

from search_results.scraper.common.searResultPages import searResultPages
from scrapy.selector import Selector
from w3lib.html import remove_tags
from webCrawler_scrapy.utils.common import get_md5
from scrapy.loader import ItemLoader
from webCrawler_scrapy.items import BaidukwItem

from selenium import webdriver



class SearcheSpider(Spider):

    name = 'searchE'
    allowed_domains = ['baidu.com', 'bing.com', 'google.com']
    start_urls = []
    keyword = None
    searchEngine = None
    selector = None

    def __init__(self, keyword, se='baidu', pages=5,  *args, **kwargs):
        super(SearcheSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword.lower()
        self.searchEngine = se.lower()
        self.selector = SearchEngineResultSelectors[self.searchEngine]
        pageUrls = searResultPages(keyword, se, int(pages))
        for url in pageUrls:
            print(url)
            self.start_urls.append(url)

    def parse(self, response):

        # for url in Selector(response).xpath(self.selector).extract():
        #     yield {'url': url}
        for res in Selector(response).xpath(BaiduSelectors['leftcontainerDiv']):
            print {'id': res.xpath('@id').extract()[0]}
            print {'srcid': res.xpath('@srcid').extract()[0]}
            for each in res.xpath('h3[1]//text()').extract():
                print each
            for each in res.xpath('div[contains(@class,"c-abstract")]').extract():
                print each
            print '------------------------------'
            # print {'title': res.xpath('/h3//text()').extract()[0].encode("utf-8")}
            # print {'brief': res.xpath('/div[2]//a/text()').extract().encode("utf-8")}
            # print {'idx': remove_tags(res.xpath('@id').extract()[0].encode("utf-8"))}

        # front_image_url = response.meta.get("front_image_url", "")  # 文章封面图
        # item_loader = ItemLoader(item=BaidukwItem(), response=response)
        # item_loader.add_xpath(BaiduSelectors['leftcontainerDiv'], ".entry-header h1::text")
        # item_loader.add_value("url", response.url)
        # item_loader.add_value("url_object_id", get_md5(response.url))
        # item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
        # item_loader.add_value("front_image_url", [front_image_url])
        # item_loader.add_css("praise_nums", ".vote-post-up h10::text")
        # item_loader.add_css("comment_nums", "a[href='#article-comment'] span::text")
        # item_loader.add_css("fav_nums", ".bookmark-btn::text")
        # item_loader.add_css("tags", "p.entry-meta-hide-on-mobile a::text")
        # item_loader.add_css("content", "div.entry")
        #
        # article_item = item_loader.load_item()


        # yield article_item


                #if res.xpath('@id')quechaoq

        # hrefs = response.selector.xpath('//div[contains(@class, "c-container")]/h3/a/@href').extract()
        # containers = response.selector.xpath('//div[contains(@class, "c-container")]')
        # for container in containers:
        #     href = container.xpath('h3/a/@href').extract()[0]
        #     title = remove_tags(container.xpath('h3/a').extract()[0])
        #     c_abstract = container.xpath('div/div/div[contains(@class, "c-abstract")]').extract()
        #     abstract = ""
        #     if len(c_abstract) > 0:
        #         abstract = remove_tags(c_abstract[0])
        #     request = scrapy.Request(href, callback=self.parse_url)
        #     request.meta['title'] = title
        #     request.meta['abstract'] = abstract
        #     yield request

    def parse_url(self, response):

        print "url:", response.url
        print "title:", response.meta['title']
        print "abstract:", response.meta['abstract']
        content = remove_tags(response.selector.xpath('//body').extract()[0])
        print "content_len:", len(content)


# class selenium_spider(Spider):
#
#     name =
#     allowed_urls =
#     start_urls =
#
#     def __init__(self):
#         self.browser = webdriver.Chrome(executable_path="")
#         super()
#
#     def spider_close(self):
