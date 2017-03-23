# koovs_spider
A scrapy spider to crawl all products from [Koovs](http://koovs.com)  

Downloading
===========

```bash
$ git clone https://github.com/sreecodeslayer/koovs_spider.git
```

Usage
======

```bash
$ cd koovs_spider/koovs
$ scrapy crawl koovs_spider -o koovs.csv
```

> This spider for now only support CSV Feed export, but you can enable other Feeds inside `settings.py`
