
from json import load
from pytest import param
import requests
from pyquery import PyQuery as pq
import os
import re
import time
import execjs
from urllib.parse import unquote
import random
import json

import urllib3

# def get_ani_data(i, li):
#     ani_url, ani_title = get_ani_view_url(li)
#     ani_detail = get_html_page_info(ani_url)
#     if (ani_detail != -1):
#         parse_ani_detail_info(ani_detail, ani_title)
#     return li

# def get_ani_view_url(li):
#     '''从列表获取到动画的详情页path和动画的title
#     '''
#     ani_doc = pq(li)
#     ani_id = ani_doc('a').attr('href')
#     ani_title = ani_doc('a')('img').attr('alt')
#     ani_url = host + ani_id
#     print('>>> 获取到动画 {} 链接: {}'.format(ani_title, ani_url))
#     return ani_url, ani_title

# def get_html_page_info(url):
#     '''根据path网络获取详情页html信息
#     '''
#     ret = requests.get(url)
#     if ret.status_code == 200:
#         print('>>> 获取动画详情数据成功，准备解析数据')
#         return ret.text
#     else:
#         print('>>> 获取动画详情数据出错了，error: {}, {}'.format(ret.status_code, ret.reason))
#         return -1
    
# def parse_ani_detail_info(detail, title):
#     '''讲详情页信息解析出来
#     '''
    
#     print('>>> 开始解析数据: {}'.format(title))
#     ani_fc_video_id = detail('.splay')('a').attr('href').replace("/view/", "").replace(".html", '')
    
#     ani_cover = "https:" + detail('.thumb')('img').attr('src')
#     ani_info_doc = detail('.sinfo')
#     ani_alias = ani_info_doc('p').eq(0).text().replace("别名:", "").replace(" ", "")
#     ani_upload_time = ani_info_doc('span').eq(0).text().replace("上映:", "").replace(" ", "")
#     ani_location = ani_info_doc('span').eq(1)('a').text().replace(" ", "")
#     ani_type_tags = [i.text() for i in ani_info_doc('span').eq(2).items('a')]
#     ani_season = ani_info_doc('span').eq(4)('a').eq(1)('a').text()+'月'.replace(" ", "")
#     temp_status = ani_info_doc('span').eq(4)('a').eq(2).text()
#     ani_status = '0' 
#     if temp_status == '连载':
#         ani_status = 1
#     elif temp_status == '完结':
#         ani_status = 2
    
#     ani_update_info_doc = ani_info_doc('p').eq(1)
#     ani_update_time_str = ani_update_info_doc('font').text()
#     ani_update_time_week = re.findall(r"每\D*", "(每周四01:00更新)")[0].replace("每", "")
#     ani_update_time_time = re.findall(r"\d\d:\d\d", "(每周四01:00更新)")[0]

#     ani_play_doc = detail('.movurl').eq(1)
#     index = 0
#     for item in ani_play_doc.items('li'):
#         random_num = random.random()
#         get_video_url = host+'_getplay?aid={}&playindex=1&pindex={}&r={}'.format(ani_fc_video_id, index, random_num)
            
#         data = load(f) 
#         vurl = data['vurl']

#         with open('url.js', 'r', encoding='UTF-8') as f:
#              jstext = f.read()
#         ctx = execjs.compile(jstext)
#         video_url = ctx.call('getplayurl', vurl)
#         video_url = unquote(video_url)
#         print(video_url)
        
        
#         index+=1
#         time.sleep(2)

# project_path = os.path.abspath(os.curdir)

# host = 'https://www.dm530p.net'

# file_path = os.path.join(project_path, "result.html")
# test_path = os.path.join(project_path, "test.html")
# if os.path.exists(file_path) is False:
#     print("load locally")
#     print("load request")
#     params = {"region": "日本", "pageindex":0}
#     ret = requests.get("https://www.dm530p.net/list/", params=params)

    
#     with open(file_path, "w+") as f:
#         f.write(ret.text)
    
# doc = pq(filename=file_path)


if __name__ == '__main__':
    randomNum = random.random()
    url = "https://www.dm530p.net/_getplay"
    params = {
        "aid": "22410",
        "playindex": "1",
        "epindex": "1",
        "r": randomNum
    }
    res = requests.post(url, params=params, headers={
        "referer": "https://www.dm530p.net/play/22410-1-1.html",
        "Server": "cloudflare",
        "Content-Type":"text/plain; charset=utf-8",
        "Transfer-Encoding": "chunked"
        })
    try:
        print(res.status_code, res.text, res.request.url, res.cookies)
    except:
        print('error parse')