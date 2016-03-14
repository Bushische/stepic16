bind = "0.0.0.0:8080"
workers = 2

#from cgi import parse_qs

def application(environ, start_response):
  start_response('200 OK', [('Content-Type', 'text/plain')])
  instr = environ['QUERY_STRING']
  print 'in str = "' + instr+'"'
#  qs = parse_qs(environ['QUERY_STRING'])
  ret = instr.replace("&", "\r\n")
  return ret
#  return ['%s=%s\n' % (k, qs[k][0]) for k in qs]
