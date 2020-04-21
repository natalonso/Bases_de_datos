# -*- coding: utf-8 -*-

import json

with open('./jsondata.json') as f:
  data = json.load(f)

# articles= data['dblp']['article']
# inproceedings= data['dblp']['inproceedings']
incollections = data['dblp']['incollection']


# with open('articles.json', 'w', encoding='utf-8') as articles_json:
#     json.dump(articles, articles_json)

# with open('inproceedings.json', 'w', encoding='utf-8') as inproceedings_json:
#     json.dump(inproceedings, inproceedings_json, ensure_ascii=False)

with open('incollections.json', 'w', encoding='utf-8') as incollections_json:
    json.dump(incollections, incollections_json, ensure_ascii=False)
