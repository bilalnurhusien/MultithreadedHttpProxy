import httplib, json

data = {}
data['key'] = 'value'
json_data = json.dumps(data)
headers = {'Host': 'testingproxy', 'Content-Length' : len(json_data), 'Content-Type': 'application/json'}
payload = json_data

conn = httplib.HTTPConnection(host='127.0.0.1',port=443)

conn.request("POST", "", payload, headers)
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
print 'Received post response:'
print respData
print '*************************************************'
