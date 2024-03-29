# Creating a vpn secured by SSL

[docker-compose.yml](docker-compose.yml)

```yml
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
