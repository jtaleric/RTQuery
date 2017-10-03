import KerberosTicket
import requests

class RTQuery(object):
  def __init__(self,config):
    self.CONFIG = config

  def _query(self, url,querystring=None):
    krb = KerberosTicket.KerberosTicket(self.CONFIG['domain'])
    headers = {"Authorization": krb.auth_header}
    if querystring is None :
      req = requests.get(url, headers=headers, verify=False)
    else :
      req = requests.get(url, headers=headers, params=querystring, verify=False)
    return req

  def rt_search(self,querystring):
    url = "{}".format(self.CONFIG['urls']['search'])
    r = self._query(url,querystring)
    lab_requests = {}
    for line in r.text.split('\n'): 
      if ':' in line :
        values = line.split(":")
        lab_requests[str(values[0].strip())] = str(values[1].strip())
    return lab_requests

  def rt_history(self,rt_id):
    history = [] 
    url = "{}/{}/history".format(self.CONFIG['urls']['ticket'],rt_id)
    r = self._query(url)
    for line in r.text.split('\n'): 
      if ':' in line :
        hist = {}
        values = line.split(":")
        if len(values) > 2 :
          hist['id'] = str(values[1].strip())
          hist['desc'] = str(values[2].strip())
        else :
          hist['id'] = str(values[0].strip())
          hist['desc'] = str(values[1].strip())
        history.append(hist)
    return history

  def rt_history_query(self,rt_id,hist_id):
    url = "{}/{}/history/id/{}".format(self.CONFIG['urls']['ticket'],rt_id,hist_id)
    r = self._query(url)
    request = {}
    for line in r.text.split('\n'): 
      if ':' in line :
        values = line.split(":")
        if len(values) > 2 :
          request[str(values[1].encode('utf-8').strip())] = str(values[2].encode('utf-8').strip())
        else :
          request[str(values[0].encode('utf-8').strip())] = str(values[1].encode('utf-8').strip())
    return request
