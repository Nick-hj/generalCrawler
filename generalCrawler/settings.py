# -*- coding: utf-8 -*-

# Scrapy settings for generalCrawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'generalCrawler'

SPIDER_MODULES = ['generalCrawler.spiders']
NEWSPIDER_MODULE = 'generalCrawler.spiders'
# 分布式设置
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter" # 去重
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# SCHEDULER_PERSIST = True
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_PARAMS = {
    "password": "",
    "db": 4
}
# REDIS_URL = "redis://127.0.0.1:6379/4"
# #使用优先级调度请求队列 （默认使用）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# 可选用的其它队列
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'generalCrawler (+http://www.yourdomain.com)'
# USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.1  # 请求间隔
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    'cookie': 'ali_apache_id=11.180.122.25.1598942647381.190789.8; _fbp=fb.1.1603270072511.1320845565; e_id=pt70; af_ss_a=1; traffic_se_co=%7B%7D; _bl_uid=qIkUqm7d0qU1vR9InfXF2m89dLyb; __utmz=3375712.1617094592.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=3375712.1468672364.1598942650.1617094592.1617692399.2; af_ss_b=1; aeu_cid=6b5094abd64042049a4e1bf9c8722441-1619691082317-08706-_2aeOzjW; cna=hm9PGQa2sUQCAXeIIHk+vVaW; _gcl_au=1.1.936047996.1624950474; aep_common_f=l0o8kCttTm9nB3h0T2UkDV5TeaiposY18ivsFeUB6/Pm5YMU/w4UiQ==; xman_f=Qze4yq2qfope7+cjFfCgvsCzFkyi56HpuX/o9Gl+lnIPi4accEUYJGu1V7pgT/6+VOcFAH53yXen2nvEcGFSJ8x8d5DbPGu6CnckZyvEOyLrYHg/Ba8Nq89EHja/F05PBhbBURkzjNlHJHzKkOlgaNZOoFfi5jF+By74k0U+3RU0xLId/d2pcZHezEfSIeu1ZAG/cYOPL0NNsPS+9B74hOopGDF/FjHzYvgrhqpFCv69zKDhY7Bb8AiWeFnnhgp+N5Z5DJFTLYlcff7ItrTPWOTnSZ6vTD0+epCPSJOINjBmzJyFVPPVDt554qwvr3D4qanl7P8YD31esQnhJqDGzWi8XlmQVVy35+Fj9L8Vhzp65ZKwOAbm1AsHfyZZHw6Q9mUwjBu39TaeqVNQOTIFNThPwiIm2obBQUQAgQf9i9nz/gD6Us0h5g==; aep_usuc_f=site=glo&c_tp=USD&x_alimid=1859821111&isb=y&region=HK&b_locale=en_US; ali_apache_track=mt=1|mid=cn258600111mbaae; xman_us_f=zero_order=y&x_locale=en_US&x_l=0&last_popup_time=1599737455866&x_user=CN|haijun|yu|ifm|1859821111&no_popup_today=n&x_lid=cn258600111mbaae&x_c_chg=0&x_c_synced=0&x_as_i=%7B%22aeuCID%22%3A%226b5094abd64042049a4e1bf9c8722441-1619691082317-08706-_2aeOzjW%22%2C%22affiliateKey%22%3A%22_2aeOzjW%22%2C%22channel%22%3A%22AFFILIATE%22%2C%22cv%22%3A%227%22%2C%22isCookieCache%22%3A%22N%22%2C%22ms%22%3A%220%22%2C%22pid%22%3A%22908725594%22%2C%22tagtime%22%3A1619691082317%7D&acs_rt=cf72780120e64a0ea51c1210227ab768; _gid=GA1.2.581283012.1626857207; _ga_VED1YSGNC7=GS1.1.1626865297.49.0.1626865297.0; _ga=GA1.1.1468672364.1598942650; RT="z=1&dm=aliexpress.com&si=f54d52cc-df3a-44d2-8465-b6d79f71efe5&ss=kreke3p8&sl=1&tt=9a9&bcn=%2F%2F684fc537.akstat.io%2F&ul=i49&hd=i54"; acs_usuc_t=x_csrf=1arytxidnd3hx&acs_rt=bb65fae258aa4965ad168111055b4de1; intl_locale=en_US; xman_t=gstk8Jbhecq4DHNsKNPClHS6t6qp+5E01FLVP0E7vvUMQrNMzMWdr58m2zfIdT29; intl_common_forever=rL/2OYaKthHLAWOFaYyskijgS3oMa1BaCu2lkuqB2XHtIz4enJv0Rw==; _m_h5_tk=4400d8932980b20f1a6bdf2c810dd3a3_1626946275848; _m_h5_tk_enc=cc1c297d56dceaacd50f0dd9ba30fb59; XSRF-TOKEN=bc1628ed-3e92-422c-98b5-b1dc8ddaa834; JSESSIONID=BC907F5046AB8356A984AD4F859A2A5B; xlly_s=1; tfstk=cL9GBdazJC56kvfHNA66jJYT-ModZKENzKR2LKNyhyGwtCJFisVUavUxxgLMHS1..; l=eBSlmJQqORhyH60CBOfwourza77OSIRA_uPzaNbMiOCPsDf95TXNB6T66sTpC3GVh6WkR3-IkQOzBeYBq3xonxv9OlRSMjHmn; isg=BJqaNF1Yrmzxsx10OTv5axwn60C8yx6lAJIg_KQTRi34FzpRjFtutWBl5-OLwJY9; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005002101887017%091005002126289793%094000182542791%094000736118061%091005002356115051%091005002910202634%091005002104052559%091005002104052559',
    'referer': 'https://www.aliexpress.com/'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'generalCrawler.middlewares.GeneralcrawlerSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'generalCrawler.middlewares.ProxyAbuyunMiddlewear': 300,
    'generalCrawler.middlewares.GeneralcrawlerDownloaderMiddleware': 543,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 80,  # 失败时重试
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'generalCrawler.pipelines.GeneralcrawlerPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
LOG_ENABLED = True
LOG_ENCODING = 'utf-8'
# LOG_LEVEL = 'ERROR'
LOG_LEVEL = 'DEBUG'
# 失败重试设置
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 403, 404, 408, 410, 429]
RETRY_TIMES = 10
# 随机user-agent
HTTPERROR_ALLOWED_CODES = [301, 302]
'''
可以设置成random, firefox,chrome, ie…
如果是random，就是随机取
'''
RANDOM_UA_TYPE = 'random'

# 保存Key
SAVE_GOODS_TO_REDIS_KEY = 'save_goods_data'
# 起始url key
START_URL = 'aliexpress_url'
# 评论id
REVIEW_ID = 'ae_reviews_id'
