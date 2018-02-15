from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
import cgi, httplib, sys,  threading

class HTTPHandler(BaseHTTPRequestHandler):

    def do_POST(self):
		try:
			conn = httplib.HTTPConnection(host='httpbin.org')
			conn.set_debuglevel(2)

			self.protocol_version = 'HTTP/1.1'
			headers = {'Host': self.headers.get('Host'), 'Content-Type': self.headers.get('Content-Type'), 'Content-Length':  self.headers.get('Content-Length')}
			content_len = int(self.headers.getheader('Content-Length', 0))
			post_body = self.rfile.read(content_len)

			print '*************************************************'
			print 'Received post request from :'
			print self.client_address
			print '*************************************************'

			print '*************************************************'
			print 'Routing request to httpbin.org'
			print headers, post_body
			print '*************************************************'

			conn.request('POST','/post', headers=headers, body=post_body)
			resp = conn.getresponse()
			respData = resp.read()

			print '*************************************************'
			print 'Received post response:'
			print respData
			print '*************************************************'

			headList = resp.getheaders()
			headDict = dict(headList)
			headers = self.protocol_version + ' ' + str(resp.status) + ' ' + resp.reason + '\r\n'
			headers = headers + 'Content-Length: ' + headDict['content-length'] + '\r\n'
			headers = headers + 'Content-Type: ' + headDict['content-type'] + '\r\n'
			headers = headers + 'Date: ' + headDict['date'] + '\r\n'

			self.wfile.write(headers + respData)
			conn.close()
		except:
			print sys.exc_info()[0]
			return

    def do_GET(self):
		try:
			conn = httplib.HTTPConnection(host='httpbin.org')
			conn.set_debuglevel(2)

			print '*************************************************'
			print 'Received get request from :'
			print self.client_address
			print '*************************************************'

			print '*************************************************'
			print 'Routing request to httpbin.org'
			print '*************************************************'

			conn.request('GET','/get')
			resp = conn.getresponse()
			respData = resp.read()

			print '*************************************************'
			print 'Received get response:'
			print respData
			print '*************************************************'

			headList = resp.getheaders()
			headDict = dict(headList)
			headers = self.protocol_version + ' ' + str(resp.status) + ' ' + resp.reason + '\r\n'
			headers = headers + 'Content-Length: ' + headDict['content-length'] + '\r\n'
			headers = headers + 'Content-Type: ' + headDict['content-type'] + '\r\n'
			headers = headers + 'Date: ' + headDict['date'] + '\r\n'

			self.wfile.write(headers + respData)
			conn.close()
		except:
			print sys.exc_info()[0]
			return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""

def run(server_class=ThreadedHTTPServer, handler_class=HTTPHandler, port=443):
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	print 'Starting httpd server, use <Ctrl-C> to stop...'

	httpd.serve_forever()

if __name__ == '__main__':
    if len(sys.argv) == 2:
		run(HTTPServer, PostHandler, int(sys.argv[1]))
    else:
		run()


