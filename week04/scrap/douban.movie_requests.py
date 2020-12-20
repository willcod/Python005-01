import requests, json
import time
from bs4 import BeautifulSoup
import re

from moviedb_manager import moviedb_manager


hds=[{'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},\
{'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},\
{'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

url_highrate = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&page_limit=50&page_start=0'

response = requests.get(url_highrate, headers=hds[1])

data = json.loads(response.text);
items = data['subjects']

dbm = moviedb_manager()

for item in items:
    title = item["title"]
    url = item["url"]
    Id = item['url'].split('/')[-2]
    print('Title: ' + title + ' URL:' + url + ' ID:' + Id)

    if dbm.movie_insert(id = Id, title=title) :
        print(title + ' has been saved')
    else:
        print(title + " didn't be saved")

    time.sleep(3)
    url_comment = f'{url}comments?status=P'
    response = requests.get(url_comment, headers=hds[1])
    soup = BeautifulSoup(response.text, 'html.parser')
    comment_items = soup.select('div.comment-item')

    for comment_item in comment_items:

        rate = re.findall(r'allstar(.+) rating', str(comment_item))
        if len(rate) < 1:
            continue
        print(rate[0])

        comment = re.findall(r'<span class="short">(.+)</span>', str(comment_item))
        if len(comment) < 1: 
            continue

        print(comment[0])

        if dbm.comment_insert(move_id= Id, rate = rate[0], comment=comment[0]) :
            print('comment has been saved')
        else:
            print("comment didn't be saved")
