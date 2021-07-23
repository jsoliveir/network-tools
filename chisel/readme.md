# Creating an ssh tunnel thru https gateways/proxies
_https://github.com/jpillora/chisel_

**[docker-compose.yml](docker-compose.yml)**


The client is listening on port 443  _(8443 is forwared to 443)_

The requests will be forward to www.google.com thru the chisel over the http-gateway
```yaml
  chisel-client:
    image: jpillora/chisel
    command:
      - client
      - --keepalive=2s 
      - --tls-skip-verify
      - --auth=user:pass
      - http://http-gateway 
      - "443:www.google.com:443"
    ports: 
      - 8443:443
    depends_on:
      - http-gateway
      - chisel-server
```

Just a simple http gateway or reverse proxy server

```yaml   
  # just a simple http gateway or reverse proxy server
  http-gateway:
    image: mitmproxy/mitmproxy
    command:
      - mitmdump
      - --listen-port=80
      - --mode=reverse:http://chisel-server
    depends_on:
      - chisel-server
```

the server, listening for incoming requests and forward them to the remotes informed by the client

```yaml      
  chisel-server:
    image: jpillora/chisel
    environment: 
        CREDENTIALS: '{"user:pass":["www.google.com:.*"]}'
    command:
      - server
      - --port=80 
      - --keepalive=1s
      - --auth=${CREDENTIALS}
```

# check it out
```bash
docker run -it --network=host curlimages/curl curl -v https://127.0.0.1:8443 --insecure
```
