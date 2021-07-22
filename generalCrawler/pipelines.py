# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

from generalCrawler.lib.base_fun import logger
import redis
from scrapy.utils.project import get_project_settings

settings = get_project_settings()


class GeneralcrawlerPipeline(object):
    @property
    def redis_conn(self):
        r = redis.StrictRedis(host=settings['REDIS_HOST'], db=settings['REDIS_PARAMS']['db'],
                              password=settings['REDIS_PARAMS']['password'])
        return r

    def process_item(self, item, spider):
        if spider.name == 'aliexpress':
            if item['success']:
                goods_info = {
                    'code': True,
                    'item': item
                }
                ae_reviews_id = {
                    'product_id': item["productId"],
                    'owner_member_id': item['ownerMemberId']
                }
                self.redis_conn.lpush(settings['SAVE_GOODS_TO_REDIS_KEY'], json.dumps(goods_info))
                self.redis_conn.lpush(settings['REVIEW_ID'], json.dumps(ae_reviews_id))
                logger.info(f'成功===={item["url"]}')
            else:
                self.redis_conn.lpush(settings['START_URL'], item['url'])
