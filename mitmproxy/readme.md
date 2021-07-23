

# Intercepting and changing requests

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
