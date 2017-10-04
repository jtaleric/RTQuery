#!/usr/bin/env python
import rtquery.RTQuery

CONFIG = {
  'elastichost': "",
  'elasticport': 9200,
  'ssl_cert': "",
  'urls': {
    'search': '',
    'ticket': '',
  },
  'domain': ""
}

querystring = {
    "query":"Queue = '-' AND Content LIKE 'Hat product(s) being tested:'"
    }

rt = rtquery.RTQuery.RTQuery(CONFIG)
data = []
rt.es_search_rt('448736')
