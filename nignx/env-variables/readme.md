# nginx as a reverse proxy

[docker-compose](docker-compose.yml)

```yaml
services:
  reverse-proxy:
    image: openresty/openresty:alpine 
    environment: 
        RESPONSE_BODY: "It's working"   
    volumes:
      - ./nginx.conf:/usr/local/openresty/nginx/conf/nginx.conf
    ports: 
      - 8080:80
 ```
 
# Check it out

HTTP
```bash
docker run -it --network=host  curlimages/curl curl -v http://127.0.0.1:8080 --insecure
```

