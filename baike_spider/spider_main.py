# -*- coding:utf-8 -*- 
# Created by Helen Cui on 2017/11/15.
#以一个入口的url来爬取数据
from baike_spider import url_manager,html_downloader,html_parser,html_outputer

class SpiderMain(object):
    def __init__(self):
        self.urls=url_manager.UrlManager()    #创建一个UrlManger类别的对象
        self.downloader=html_downloader.HtmlDownloader()   # "
        self.parser=html_parser.HtmlParser()               # "
        self.outputer = html_outputer.HtmlOutputer()       # "
    def craw(self,root_url):
        count=1  #记录当前爬取的是第几个url
        self.urls.add_new_url(root_url)   #获取待爬取的url
        while self.urls.has_new_url():    #如果有管理器里面有待爬取的url
            try:
                new_url=self.urls.get_new_url()   #获取管理器里面有待爬取的url
                print 'craw %d:%s' %(count,new_url)
                html_cont=self.downloader.download(new_url)  #下载待爬取的url的内容
                new_urls,new_data=self.parser.parse(new_url,html_cont)   #将下载好的内容传给urls,data两个变量
                self.urls.add_new_urls(new_urls)        #将该url涉及到的其他urls传入管理器
                self.outputer.collect_data(new_data)    #将该url涉及到的数据传入输出器
                if count==20:
                    print 'hey'
                    break
                count=count+1
            except Exception, e:
                print 'e.message:\t', e.message
                print 'craw failed'
        self.outputer.output_html()

if __name__=="__main__":
    root_url="http://baike.baidu.com/item/Python"
    obj_spider=SpiderMain()   #创建一个SpiderMain类的对象
    obj_spider.craw(root_url)