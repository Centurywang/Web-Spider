'''
数据处理，读取网页并将所有电影 name 、id（id在li中存在），
'''
import re
import json

def read_file(path):
    '''读取文件'''
    with open(path,encoding='utf8') as f:
        content = f.read()
    return content

def write_file(path,content):
    '''写入文件'''
    with open(path,'w')as f:
        f.write(content)

def search_id(html):
    '''使用re读取电影名以及url'''
    result = re.findall(r'<li id="(.*?)" class="list-item" data-title="(.*?)"',html)
    # result结果 [('26309788', '金刚：骷髅岛'), ('26606743', '嫌疑人X的献身'),....
    return result

def handel_movie(movieInfo):
    '''生成评价页面url
    解析页面得 评价页面url规律为 https://movie.douban.com/subject/ + 影片id + /reviews
    '''
    result = []
    for i in movieInfo:
        url = 'https://movie.douban.com/subject/' + i[0] + '/reviews'
        #title = i[1]
        #result.append([title,url])
        result.append(url)
    return result



if __name__ == '__main__':
    # 读取文件
    html = read_file('movie_review.htm')
    # 搜寻结果
    result = search_id(html)
    # 生成评价页面url
    result = handel_movie(result)
    print(result)
    # 格式化为json
    result = json.dumps(result)
    # 保存到文件中
    write_file('movies/movies/spiders/urls.data',result)