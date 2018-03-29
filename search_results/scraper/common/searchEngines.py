# -*- coding: utf-8 -*-
# @Time    : 2017/8/29 16:45
# @Author  : Alkad


SearchEngines = {
    'google': 'https://www.google.com/search?qk={0}&start={1}',
    'bing': 'http://www.bing.com/search?q={0}&first={1}',
    'baidu': 'http://www.baidu.com/s?wd={0}&pn={1}'
}

SearchEngineResultSelectors = {
    'google': '//h3/a/@href',
    'bing': '//h2/a/@href',
    'baidu': '//h3/a/@href',
}

#------------------------BAIDU---------------------------------
#response.xpath('//*[@id="content_left"]/div[@id]').extract()

baiduSelectors = {
    'searchnum': '//div[@class="head_nums_cont_inner"]/div[@class="nums"]/text()',#搜索量
    'leftcommend': '//*[@id="content_left"]/div[@class="leftBlock"]',#为您推荐
    'leftcontainer': '//*[@id="content_left"]',#为您推荐

    'leftcontainerDiv': '//div[@id="content_left"]/div[@srcid]', #左侧结果
    # 'coloum'
    'leftcontainerAdup': '//*[@id="content_left"]//div[@data-pos]', #左侧广告

    'leftcontainerAddown': '//*[@id="content_left"]//div[@id=clone]', #左侧

    'rightAds': '',
    'right': '',
}

BaiduResultSelectors = {
    'rightAds': '',
    'right': '',
}

