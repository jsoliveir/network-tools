Forwarding requests thru an http proxy

```yaml
services:
 reverse-proxy:
    image: alpine/socat    
    command:
        - -dd 
        - TCP-LISTEN:443,fork,reuseaddr 
        - PROXY:p-pt1.urban-vpn.com:www.google.com:443,proxyport=80,proxyauth=urbanvpn@urban-vpn.com:urbanvpn4321
    ports:
      - 8443:443  
 ```
 
 Check it out
 
 ```bash
docker run -it curlimages/cur curl -v https://127.0.0.1:8443 --insecure
 ```
