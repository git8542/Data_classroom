# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ComicItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    dir_name = scrapy.Field() # 文件名
    link_url = scrapy.Field() # 每个章节的每一页的链接
    img_url = scrapy.Field()   #图片连接
    image_paths = scrapy.Field() # 图片保存路径
