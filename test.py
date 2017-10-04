#!/usr/bin/env python
import rtquery.RTQuery
import pprint

CONFIG = {
  'elastichost': "",
  'elasticport': 9200,
  'index': "quads-rt",
  'ssl_cert': "",
  'urls': {
    'search': '',
    'ticket': '',
  },
  'domain': ""
}

querystring = {
    "query":"Queue = 'openstack-' AND Content LIKE 'Red Hat product(s) being tested:' AND CF.QUADS = 'Approved'"
    }


rt = rtquery.RTQuery.RTQuery(CONFIG)
data = []
for ticket in rt.rt_search(querystring):
  print ticket
  history = rt.rt_history(ticket)
  pprint.pprint(rt.rt_history_query(ticket,history[0]['id']))

#history = rt.rt_history('454908')
  #print history
#for fields in history :
#  pprint.pprint(rt.rt_history_query('454908',fields['id']))
#  rt.es_insert_rt(ticket,request)

#print rt.rt_history_query('445254','9075671')
#print rt.es_search_rt('448736')
