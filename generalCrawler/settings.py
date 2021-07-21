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
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
SCHEDULER_PERSIST = True
REDIS_HOST = "172.31.29.232"
REDIS_PORT = 6379
REDIS_PARAMS = {
    "password": "Skrmart@2018!",
    "db": 4
}
# REDIS_URL = "redis://172.31.29.232:6379/1"
# #使用优先级调度请求队列 （默认使用）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
# 可选用的其它队列
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'generalCrawler (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'generalCrawler.middlewares.GeneralcrawlerSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'aliexpress.middlewares.ProxyAbuyunMiddlewear': 300,
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
    # 'generalCrawler.pipelines.GeneralcrawlerPipeline': 300,
    'aliexpress.pipelines.AliexpressPipeline': 300,
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
LOG_LEVEL = 'ERROR'
# 失败重试设置
RETRY_HTTP_CODES = [500,502, 503, 504, 400, 403, 404, 408,410,429]
RETRY_TIMES = 10
# 随机user-agent
HTTPERROR_ALLOWED_CODES = [301,302]
'''
可以设置成random, firefox,chrome, ie…
如果是random，就是随机取
'''
RANDOM_UA_TYPE = 'random'