

# Intercepting and replacing requests body

[replace-body.py](replace-body.py)

[docker-compose.yml](docker-compose.yml)

https://docs.mitmproxy.org/stable/addons-examples/

```yaml
services:
  reverse-proxy:
    image: mitmproxy/mitmproxy
    command:
      - mitmdump
      - --ssl-insecure
      - --listen-port=443
      - --mode=reverse:https://www.google.com
      - -s /src/script.py
    ports:
        - 8443:443
    volumes:
        - ./replace-body.py:/src/script.py
 ```


# Check it out

```bash
docker run -it curlimages/cur curl -v https://127.0.0.1:8443 --insecure
```
