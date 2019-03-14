import scrapy
import re
import random
# import requests
# '''获取代理'''
# PROXY_POOL_URL = 'http://localhost:5000/get'
# def get_proxy():
#     try:
#         response = requests.get(PROXY_POOL_URL)
#         if response.status_code == 200:
#             return response.text
#     except ConnectionError:
#         return None

class GradeSpider(scrapy.Spider):
    # 项目名称
    name = 'movie'
    # 开始url地址列表
    start_url = ['https://movie.douban.com/subject/26309788/reviews', 'https://movie.douban.com/subject/26606743/reviews', 'https://movie.douban.com/subject/26616690/reviews', 'https://movie.douban.com/subject/26602933/reviews', 'https://movie.douban.com/subject/25900945/reviews', 'https://movie.douban.com/subject/26828019/reviews', 'https://movie.douban.com/subject/26681656/reviews', 'https://movie.douban.com/subject/6873143/reviews', 'https://movie.douban.com/subject/26948814/reviews', 'https://movie.douban.com/subject/25818101/reviews', 'https://movie.douban.com/subject/25765735/reviews', 'https://movie.douban.com/subject/26850326/reviews', 'https://movie.douban.com/subject/26820836/reviews', 'https://movie.douban.com/subject/25934014/reviews', 'https://movie.douban.com/subject/2277018/reviews', 'https://movie.douban.com/subject/5262339/reviews', 'https://movie.douban.com/subject/4078592/reviews', 'https://movie.douban.com/subject/26354572/reviews', 'https://movie.douban.com/subject/3230115/reviews', 'https://movie.douban.com/subject/26331917/reviews', 'https://movie.douban.com/subject/26182910/reviews', 'https://movie.douban.com/subject/26818346/reviews', 'https://movie.douban.com/subject/10772258/reviews', 'https://movie.douban.com/subject/26704590/reviews', 'https://movie.douban.com/subject/26704592/reviews', 'https://movie.douban.com/subject/26378133/reviews', 'https://movie.douban.com/subject/26991765/reviews', 'https://movie.douban.com/subject/26996771/reviews', 'https://movie.douban.com/subject/26902792/reviews', 'https://movie.douban.com/subject/10465132/reviews']
    start_urls = start_url
    print(start_urls)


    def start_requests(self):
        cookies = [#{'bid': 'BnA2akUyw5A', 'gr_user_id': 'bdd8be88-de48-4224-bbf8-b92068a3ce10', 'viewed': '"1090043_1770782"', '_vwo_uuid_v2': 'D5358404EDEDE09180A313C9FA03C0E2B|ccf2307dfd4fc23937a9c335f961783d', 'll': '"118228"', '__utmv': '30149280.19078', '__yadk_uid': 'xrxM5ctl9V3rMHRI94My64vxTieVVwJh', 'ct': 'y', '__utmc': '223695111', 'ap_v': '0,6.0', 'dbcl2': '"190785423:vlsDZq9TsHE"', 'ck': '7UL8', '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1552529332%2C%22https%3A%2F%2Fopen.weixin.qq.com%2Fconnect%2Fqrconnect%3Fappid%3Dwxd9c1c6bbd5d59980%26redirect_uri%3Dhttps%253A%252F%252Fwww.douban.com%252Faccounts%252Fconnect%252Fwechat%252Fcallback%26response_type%3Dcode%26scope%3Dsnsapi_login%26state%3DBnA2akUyw5A%252523douban-web%252523https%25253A%252F%252Fmovie.douban.com%252Fsubject%252F26606743%252Freviews%25253Fstart%25253D420%22%5D', '_pk_ses.100001.4cf6': '*', '__utma': '223695111.1649275946.1551835332.1552524012.1552529332.6', '__utmz': '223695111.1552529332.6.4.utmcsr', '__utmb': '30149280.2.10.1552529332', 'push_noty_num': '0', 'push_doumail_num': '0', '__utmt': '1', '_pk_id.100001.4cf6': '30aa8e8584b73cdb.1551835332.6.1552529968.1552525856.'},
            {'bid': 'BnA2akUyw5A', 'gr_user_id': 'bdd8be88-de48-4224-bbf8-b92068a3ce10', 'viewed': '"1090043_1770782"',
             '_vwo_uuid_v2': 'D5358404EDEDE09180A313C9FA03C0E2B|ccf2307dfd4fc23937a9c335f961783d', 'll': '"118228"',
             '__yadk_uid': 'xrxM5ctl9V3rMHRI94My64vxTieVVwJh', 'ct': 'y', '__utmc': '223695111', 'ap_v': '0,6.0',
             '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1552529332%2C%22https%3A%2F%2Fopen.weixin.qq.com%2Fconnect%2Fqrconnect%3Fappid%3Dwxd9c1c6bbd5d59980%26redirect_uri%3Dhttps%253A%252F%252Fwww.douban.com%252Faccounts%252Fconnect%252Fwechat%252Fcallback%26response_type%3Dcode%26scope%3Dsnsapi_login%26state%3DBnA2akUyw5A%252523douban-web%252523https%25253A%252F%252Fmovie.douban.com%252Fsubject%252F26606743%252Freviews%25253Fstart%25253D420%22%5D',
             '_pk_ses.100001.4cf6': '*', '__utma': '223695111.1649275946.1551835332.1552524012.1552529332.6',
             '__utmz': '223695111.1552529332.6.4.utmcsr', '__utmb': '30149280.6.10.1552529332', 'push_noty_num': '0',
             'push_doumail_num': '0', 'dbcl2': '"193337836:qx88RHivkuQ"', 'ck': 'RbZN', '__utmt': '1',
             '__utmv': '30149280.19333', '_pk_id.100001.4cf6': '30aa8e8584b73cdb.1551835332.6.1552531203.1552525856.'}

        ]

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}
        cookie = random.choice(cookies)
        for url in self.start_urls:
            # 注意这里面的meta={'proxy':proxies},一定要是proxy进行携带,其它的不行,后面的proxies一定 要是字符串,其它任何形式都不行
            yield scrapy.Request(url, callback=self.parse, cookies=cookie,headers=headers,meta={'start_url':url})


    def parse(self, response):
        '''分析页面可得
        评分分为
        很差：1星  较差：2星   还行：3星   推荐：4星  力荐：5星
        '''
        # 获取评价
        contentList = response.xpath('//div[@class="review-list  "]//div[@class="main review-item"]')
        # xpath解析 注意：此处的评分在response的返回与网页内容不同
        for content in contentList:
            item = {}
            item['movie_name'] = response.xpath('//title/text()').extract_first().strip()
            item['grade'] = content.xpath('.//header[@class="main-hd"]//span/@title').extract_first()
            try:
                item['grade'] = int(['很差', '较差', '还行', '推荐', '力荐'].index(item['grade'])) + 1
            except:
                item['grade'] = 3
            print(item.values)
            yield item
        # 获取下一页

        try:
            next_url = re.findall(r'<a href="(.*?)" >后页&gt;',response.text)[0]
            next_url = response.meta['start_url'] + next_url
        except:
            next_url = None
        print('next_url:',next_url)
        # 调用此函数
        if next_url is not None:
            yield scrapy.Request(
                next_url,
                callback=self.parse
            )