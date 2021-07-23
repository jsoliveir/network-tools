# nginx as a reverse proxy

[docker-compose](docker-compose.yml)

```yaml
services:
  reverse-proxy:
    image: openresty/openresty:alpine    
    volumes:
      - ./nginx.conf:/usr/local/openresty/nginx/conf/nginx.conf
    ports: 
      - 8443:443
 ```
 
# Check it out
 
HTTPS
```bash
docker run -it --network=host --add-host='www.google.com:127.0.0.1' curlimages/curl curl -v https://www.google.com:8443 --insecure
```

HTTP
```bash
docker run -it --network=host  curlimages/curl curl -v -H'Host:www.blackle.com' http://127.0.0.1:8080 --insecure
```

