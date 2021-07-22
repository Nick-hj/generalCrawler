# -*- coding: utf-8 -*-
# @Time    : 2021/7/22 14:51
# @Author  : Haijun
from scrapy.cmdline import execute

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
# execute(["scrapy","crawl","shopify"])
# execute(["scrapy","crawl","shopify_many"])
execute(["scrapy", "crawl", "aliexpress"])
