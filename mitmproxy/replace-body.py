from mitmproxy import ctx
from mitmproxy import http
flag=False
def response(flow: http.HTTPFlow):
    flow.response.content=bytes("THE POWER BELONGS TO PEOPLE HOW TAKE IT","UTF-8")
    ctx.log.info("RESPONSE SENT")
