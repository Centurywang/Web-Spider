# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

result = {}
class MoviesPipeline(object):

    def process_item(self, item, spider):

        # 如果result有数据
        if len(result) > 0:
            # 如果item['movie_name']在result键中存在
            if item['movie_name'] in result.keys():
                result[item['movie_name']]['grade'].append(item['grade'])
            # 如果不存在
            else:
                result[item['movie_name']] = {'grade':[item['grade']]}
        # 如果result没有数据
        else:
            result[item['movie_name']] = {'grade': [item['grade']]}

        return item
    def __del__(self):
        print(result)
        for r in result.keys():
            result[r]['avg_grade'] = '%.4f'% float(sum(result[r]['grade'])/len(result[r]['grade']))
            result[r]['max_grade'] = max(result[r]['grade'])
            result[r]['min_grade'] = min(result[r]['grade'])
            del result[r]['grade']
        with open('text.txt','w',encoding='utf-8') as f:
            f.write(str(result))