# -*- coding: utf-8 -*-
import re

import scrapy
import json
from scrapy_redis.spiders import RedisSpider


class AeReviewsSpider(scrapy.Spider):
    name = 'ae_reviews'
    allowed_domains = ['aliexpress.com']
    start_urls = ['http://aliexpress.com/']
    redis_key = 'ae_reviews_id'

    def make_requests_from_url(self, url):
        data = json.loads(url)
        request_url = 'https://feedback.aliexpress.com/display/productEvaluation.htm'
        product_id = data['product_id']
        owner_member_id = data['owner_member_id']
        item = {
            'productId': product_id,
            'ownerMemberId': owner_member_id,
            'orderReviews': []
        }
        data = self.request_data(product_id, owner_member_id, 1)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4115.0 Safari/537.36'
        }
        return scrapy.Request(url=request_url, method="POST", headers=headers, body=json.dumps(data), dont_filter=True,
                              meta={'item': item, 'headers': headers, 'request_url': request_url, 'flat': True})

    def parse(self, response):
        item = response.meta.get('item')
        product_id = item['productId']
        owner_member_id = item['ownerMemberId']
        headers = item['headers']
        request_url = item['request_url']
        div_list = response.xpath('//div[@class="feedback-list-wrap"]/div')
        if not div_list:
            yield None
        else:
            for div in div_list:
                data_dict = {}
                data_dict['userName'] = self._user_name(div)
                data_dict['country'] = self._country(div)
                data_dict['star'] = self._star(div)
                data_dict['orderInfo'] = self._order_info(div)
                data_dict['contentsText'] = self._contents_text(div)
                data_dict['imageList'] = self._image_list(div)
                if data_dict['userName']:
                    item['orderReviews'].append(data_dict)
            if item['flat']:
                n = self.pages(response)
                if n > 1:
                    for _page in range(2, n + 1):
                        data = self.request_data(product_id, owner_member_id, _page)
                        yield scrapy.Request(url=request_url, method="POST", headers=headers, body=json.dumps(data),
                                             dont_filter=True,
                                             meta={'item': item, 'headers': headers, 'url': request_url, 'flat': True})

    @staticmethod
    def request_data(product_id, owner_member_id, page):
        data = {
            'ownerMemberId': owner_member_id,  # 251128372 240039249
            'memberType': 'seller',
            'productId': product_id,  # 1005003002680274 1005001798022744
            'companyId': '',
            'evaStarFilterValue': 'all Stars',
            'evaSortValue': 'sortlarest@feedback',  # sortdefault@feedback  sortlarest@feedback
            'page': 1,
            'currentPage': 1,
            'startValidDate': '',
            'i18n': 'true',
            'withPictures': 'false',
            'withAdditionalFeedback': 'false',
            'onlyFromMyCountry': 'false',
            'version': '',
            'isOpened': 'true',
            'translate': 'Y',
            'jumpToTop': 'false',
            'v': 2
        }
        return data

    def pages(self, html):
        total_reviews = html.xpath('//div[@class="customer-reviews"]/text()').get()
        if total_reviews:
            number = re.search(r'(\d+)', total_reviews).group(1)
            total_page = int(int(number) / 10) + 1
            if total_page >= 5:
                n = 5
            else:
                n = total_page
            return n

    @staticmethod
    def _user_name(div):
        u = div.xpath('./div[@class="fb-user-info"]/span[@class="user-name"]/a/text()').get()
        if not u:
            u = div.xpath('./div[@class="fb-user-info"]/span[@class="user-name"]/text()').get()
        return u

    @staticmethod
    def _country(div):
        return div.xpath('./div[@class="fb-user-info"]/div[@class="user-country"]/b/text()').get()

    @staticmethod
    def _star(div):
        _width = div.xpath(
            './div[@class="fb-main"]/div[@class="f-rate-info"]/span[@class="star-view"]/span/@style').get()
        try:
            n = int(_width.split(':')[1].replace('%', '')) / 20
        except AttributeError as e:
            n = 0
        return n

    @staticmethod
    def _order_info(div):
        spans = div.xpath('./div[@class="fb-main"]/div[@class="user-order-info"]/span')
        property_list = []
        for span in spans:
            prop_dict = {}
            _prop_name = span.xpath('./strong/text()').get()
            prop_dict['propName'] = _prop_name
            _prop_value = span.xpath('./text()').extract()
            _prop_value = [k.strip() for k in
                           [i.replace('\n', '').replace('\t', '').replace('\xa0', ' ') for i in _prop_value] if
                           k.strip()] if _prop_value else None
            prop_dict['propValue'] = _prop_value[0] if _prop_value else None
            property_list.append(prop_dict)
        return property_list

    @staticmethod
    def _contents_text(div):
        return div.xpath(
            './div[@class="fb-main"]/div[@class="f-content"]/dl[@class="buyer-review"]/dt[@class="buyer-feedback"]/span[1]//text()').get()

    @staticmethod
    def _image_list(div):
        return div.xpath(
            './div[@class="fb-main"]/div[@class="f-content"]/dl[@class="buyer-review"]/dd[@class="r-photo-list"]/ul[@class="util-clearfix"]/li/@data-src').extract()
