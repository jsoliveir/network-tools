# Creating a VPN


```yml
# docker-compose

services:

  # start the server
  server:
    image: alpine/socat
    command:
      - -dd 
      - TCP-LISTEN:444,fork,reuseaddr
      - TUN:10.2.0.1/24,up
    privileged: true
    
  # start the client
  client:
      image: alpine/socat
      command: 
        - -dd 
        - TCP-CONNECT:server:444
        - TUN:10.2.0.2/24,up
      privileged: true
      depends_on: 
        - server
```


# Creating a vpn secured by SSL
```yml
# docker-compose

services:
  # generating the client and server certificates
  openssl:
    image: alpine/openssl
    entrypoint: [sh, -c]
    command:
        - |
          # server certificate
          openssl genrsa -out /cert/server.key 
          openssl req -new -key /cert/server.key -x509 -days 365 -out /cert/server.crt -subj "/C=PT/CN=server"
          cat /cert/server.key /cert/server.crt > /cert/server.pem
          # client certificate
          openssl genrsa -out /cert/client.key 
          openssl req -new -key /cert/client.key -x509 -days 365 -out /cert/client.crt -subj "/C=PT/CN=client"
          cat /cert/client.key /cert/client.crt > /cert/client.pem
    volumes:
        - certificates:/cert
        
  # start up the server
  server:
    image: alpine/socat
    command:
      - -dd 
      - OPENSSL-LISTEN:4443,cert=/cert/server.pem,cafile=/cert/client.crt
      - TUN:10.2.0.1/24,up
    volumes:
      - certificates:/cert
    privileged: true
    depends_on:
      - openssl
      
  # connect the client to the server
  client:
      image: alpine/socat
      command: 
        - -dd 
        - OPENSSL:server:4443,cert=/cert/client.pem,cafile=/cert/server.crt 
        - TUN:10.2.0.2/24,up
      volumes:
        - certificates:/cert
      privileged: true
      depends_on: 
        - openssl
        - server
volumes:
    certificates:
```

# Forwarding requests thru an http proxy

```yaml
services:
 curl:
    image: curlimages/curl
    command: curl -v https://www.google.com
    depends_on:
        - reverse-proxy
 reverse-proxy:
    image: alpine/socat    
    command:
        - -dd 
        - TCP-LISTEN:443,fork,reuseaddr 
        - PROXY:p-pt1.urban-vpn.com:www.google.com:443,proxyport=80,proxyauth=urbanvpn@urban-vpn.com:urbanvpn4321
    networks:
      default:
        aliases:
          - www.google.com
```

