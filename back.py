import pycurl
import os
import sys
import io
import json
import requests

url = "https://localhost:9090/reservation"
data={'number': 12524}
'''
d = "12-09-2020-15:45"
data = json.dumps({"fecha": d})
c = pycurl.Curl()
response = io.StringIO()
c.setopt(pycurl.URL, url)
c.setopt(pycurl.SSL_VERIFYPEER, 0)
c.setopt(pycurl.SSL_VERIFYHOST, 0)
c.setopt(pycurl.HTTPHEADER, ['Accept: application/json'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, data)
c.setopt(c.WRITEFUNCTION, response.write)
c.getinfo(pycurl.RESPONSE_CODE)
response.write(c.perform())
content = response.getvalue()
c.close()
'''
requests = requests.Session()
requests.verify = False
r = requests.post(url, data)
print(r.status_code, r.reason)
print(r.content)
print("conectado")