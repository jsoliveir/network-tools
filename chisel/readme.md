# Creating a tunnel over https gateways/proxies

```yaml
services:
  # the tester
  curl:
    image: curlimages/curl
    command: curl -v https://chisel-client --insecure
    depends_on:
      - chisel-client
      
  # the client - listening on port 443
  chisel-client:
    image: jpillora/chisel
    command:
      - client
      - --keepalive=2s 
      - --tls-skip-verify
      - http://chisel-server 
      - "443:www.google.com:443"
    ports:
      - 443
    depends_on:
      - chisel-server

  # the server - forwarding requests, controlled by the client
  chisel-server:
    image: jpillora/chisel
    command:
      - server
      - --port=80 
      - --keepalive=1s
```
