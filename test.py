#!/usr/bin/env python
import rtquery.RTQuery

CONFIG = {
        'ssl_cert': "",
        'urls': {
            'search': 'https://path.to.com/rt/REST/1.0/search/ticket',
            'ticket': 'https://path.to.com/rt/REST/1.0/ticket',
            },
        'domain': "USER@path.to.com"
        }

querystring = {
        "query":"Queue = 'query' AND Content LIKE 'product(s) being tested:'"
        }

rt = rtquery.RTQuery.RTQuery(CONFIG)
data = []
for _id in rt.rt_search(querystring) :
  init = rt.rt_history(_id)
  request = rt.rt_history_query(_id,init[0]['id'])
  data.append(request)
