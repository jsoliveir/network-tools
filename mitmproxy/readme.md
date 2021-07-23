

# Intercepting and changing requests

```yaml
services:
 man-in-the-midle:
    image: mitmproxy/mitmproxy
    command:
      - mitmdump
      - --ssl-insecure
      - --listen-port=8080
      - --mode=reverse:https://pkgs.dev.azure.com
      - --modify-headers=:Host:pkgs.dev.azure.com
      # Authorization Header injection
      - --modify-headers=:Authorization:Basic <personal access token>
      # Response body manipulation
      - --modify-body=|~s|https://pkgs.dev.azure.com|http://pkgs.dev.internbank.api:30000
 ```
