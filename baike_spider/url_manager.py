# -*- coding:utf-8 -*- 
# Created by Helen Cui on 2017/11/15.
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()  #待爬取的url
        self.old_urls = set()  #已经爬取过的url

    def add_new_url(self,url):   #添加新的url
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:   #说明这个url是个全新的
            self.new_urls.add(url)

    def add_new_urls(self,urls):   #添加新url涉及到其他新url
        if urls is not None and len(urls)!=0:
            for url in urls:
                self.add_new_url(url)   #可以不传入self
            else:
                return

    def has_new_url(self):    #判断是否有新的待爬取的url
        return len(self.new_urls)!=0

    def get_new_url(self):    #获取是否有新的待爬取的url
        if len(self.new_urls)!=0:
            new_url=self.new_urls.pop()   #从列表中获取一个url，并从列表中移除这个url
            self.old_urls.add(new_url)
        return new_url


