
import requests
from pyquery import PyQuery as pq
import os
import re
import time
import execjs
from urllib.parse import unquote
import random
import json

# 目录文件
project_path = os.path.abspath(os.curdir)
host = 'https://www.dm530p.net'

# 视频解析器
with open('url.js', 'r', encoding='utf-8') as f:
    jstext = f.read()
ctx = execjs.compile(jstext)
session = requests.Session()  


def start():
    isEnd = False
    
    current_page = 0
    while isEnd is False:
        params = {"region": "日本", "pageindex":0}
        ret = requests.get("https://www.dm530p.net/list/", params=params)
        if ret.status_code == 200:
            print("获取到第{}页动画列表数据，开始解析所有列表内容".format(current_page))
            doc = pq(ret.text)
            page_list= doc('.lpic')('ul').find('li')
            if page_list.size() == 0:
                isEnd = True
            for item in page_list.items():
                get_ani_data(item)
            
            isEnd = True
                
            current_page = current_page + 1

def get_ani_view_url(li):
    '''从列表获取到动画的详情页path和动画的title
    '''
    ani_doc = li
    ani_id = ani_doc('a').attr('href')
    ani_title = ani_doc('a')('img').attr('alt')
    ani_url = host + ani_id
    print('>>> 获取到动画 [{}] 链接: {}'.format(ani_title, ani_url))
    return ani_url, ani_title

def get_html_page_info(url):
    '''根据path网络获取详情页html信息
    '''
    ret = requests.get(url)
    if ret.status_code == 200:
        print('>>> 获取动画详情数据成功，准备解析数据')
        return ret.text
    else:
        print('>>> 获取动画详情数据出错了，error: {}, {}'.format(ret.status_code, ret.reason))
        return -1

def get_ani_data(li):
    ani_url, ani_title = get_ani_view_url(li)
    ani_detail = get_html_page_info(ani_url)
    if (ani_detail != -1):
        parse_ani_detail_info(ani_detail, ani_title)

def parse_ani_detail_info(detail_text, title):
    '''讲详情页信息解析出来
    '''
    
    print('>>> 开始解析数据: [{}]'.format(title))
    detail = pq(detail_text)
    ani_fc_video_id = detail('.splay')('a').attr('href').replace("/view/", "").replace(".html", '')
    
    ani_cover = "https:" + detail('.thumb')('img').attr('src')
    ani_info_doc = detail('.sinfo')
    ani_alias = ani_info_doc('p').eq(0).text().replace("别名:", "").replace(" ", "")
    ani_upload_time = ani_info_doc('span').eq(0).text().replace("上映:", "").replace(" ", "")
    ani_location = ani_info_doc('span').eq(1)('a').text().replace(" ", "")
    ani_type_tags = [i.text() for i in ani_info_doc('span').eq(2).items('a')]
    ani_season = ani_info_doc('span').eq(4)('a').eq(1)('a').text()+'月'.replace(" ", "")
    temp_status = ani_info_doc('span').eq(4)('a').eq(2).text()
    ani_status = '0' 
    if temp_status == '连载':
        ani_status = 1
    elif temp_status == '完结':
        ani_status = 2
    
    ani_update_info_doc = ani_info_doc('p').eq(1)
    ani_update_time_str = ani_update_info_doc('font').text()
    
    try:
        ani_update_time_week = re.findall(r"每\D*", ani_update_time_str)[0].replace("每", "")
    except:
        ani_update_time_week = ""
    try:
        ani_update_time_time = re.findall(r"\d\d:\d\d", ani_update_time_str)[0]
    except:
        ani_update_time_time = ""
    ani_play_doc = detail('.movurl').eq(1)

    vurls = []
    for index, item in enumerate(ani_play_doc.items('li')):
        v_url = getvideoUrl(ani_fc_video_id, 1, index)
        vurls.append(v_url)

    result_json = {
        'aid': ani_fc_video_id,
        'title': title,
        'cover': ani_cover,
        'alias': ani_alias,
        'upload_time': ani_upload_time,
        'location': ani_location,
        'tags': ani_type_tags,
        'season': ani_season,
        'status': ani_status,
        'update_week': ani_update_time_week,
        'update_time': ani_update_time_time,
        'v_urls': vurls,
    }
    print("获取动画信息结束: ", result_json)
    json_text = json.dumps(result_json)
    with open(os.path.join(project_path, 'animations', '{}.json'.format(ani_fc_video_id)), 'w+') as f:
        f.write(json_text)


def getvideoUrl(aid, pIndex, epIndex):
    print('获取动画[{}]第[{}]集url'.format(aid, epIndex))
    i = 8
    v_url = ""
    # session.cookies.clear()
    while i > 0:
        data = send_request(aid, pIndex, epIndex)
        if data == "err:timeout":
            
            t1 = round(float(session.cookies.get("t1")) / 0x3e8) >> 0x5
            k2 = (t1 * (t1 % 4096) + 39382) * (t1 % 4096) + t1;
            
            session.cookies.set(name="t2", value=str(int(time.time()*1000)))
            session.cookies.set(name="k2", value=str(k2))  

        else:
            try:
                dic = json.loads(data)
                vurl = dic["vurl"]
                if vurl != "":
                    v_urlcode = ctx.call("getvurl", vurl)
                    v_url = unquote(v_urlcode)
                    if v_url.endswith('.mp4') and v_url.startswith('http'):
                        i = -1
                    else:
                        v_url = ""
            except:
                v_url = ""
            time.sleep(3)
        i = i-1
    print(v_url)
    return v_url

def send_request(aid, pIndex, epIndex):
    try:
        num = random.random()
        response = session.get(
            url="https://www.dm530p.net/_getplay",
            params={
                "aid": str(aid),
                "playindex": "1",
                "epindex": str(epIndex),
                "r": str(num),
            },
            headers={
                "referer": "https://www.dm530p.net/play/{}-{}-{}.html".format(aid, pIndex, epIndex),
                "Content-Type": 'text/plain; charset=utf-8'
            },
            timeout=10,
        )
        print("获取链接结果:{},{}".format(response.status_code,response.content))
        return response.text
    except:
        print('获取动画[{}]第[{}]集url失败'.format(aid, epIndex))
        return ""
  
 
if __name__ == '__main__':
    start()