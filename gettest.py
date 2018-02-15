import httplib

conn = httplib.HTTPConnection(host='127.0.0.1',port=443)

conn.request("GET", "")
resp = conn.getresponse()

print '*************************************************'
print 'Received post status and reason:'
print resp.status, resp.reason
print '*************************************************'

try:
    respData = resp.read()
except httplib.IncompleteRead as e:
    respData = e.partial

print '*************************************************'
print 'Received get response:'
print respData
print '*************************************************'
