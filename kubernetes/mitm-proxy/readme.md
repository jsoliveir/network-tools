
# Intercepting Requests / Centralizing access tokens

If you need to get URL proxied and requests/responses manipulated on the fly, this might be something interesting for you.

_The sensive data should be mapped thru Kubernetes secrets_

[Kubernetes Authentication Proxy](authentication-proxy.yml)

In the following example we are exposing an azure devops package source thru the internet by centralizing access tokens internally in Kubernetes

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: "mitm-proxy-gw"
  namespace: devops
  labels:
    app: "mitm-proxy-gw"
spec:
  selector:
    matchLabels:
      app: mitm-proxy-gw
  template:
    metadata:
      labels:
        app: mitm-proxy-gw
    spec:
      containers:
      - name: mitm-proxy-gw
        image: mitmproxy/mitmproxy
        command:
          - mitmdump
          - --ssl-insecure
          - --listen-port=8080
          - --mode=reverse:https://pkgs.dev.azure.com
          - --modify-headers=:Host:pkgs.dev.azure.com
          # Authorization Header injection
          - --modify-headers=:Authorization:Basic <personal access token>
          # Response body replacement
          - --modify-body=|~s|https://pkgs.dev.azure.com|https://pkgs.my.domain.com
        ports:
          - containerPort: 8080
            name:  http

---
apiVersion: v1
kind: Service
metadata:
  name: mitm-proxy-gw
  namespace: devops
spec:
  selector:
    app: mitm-proxy-gw
  type: NodePort
  ports:
  - name: mitm-proxy-gw
    protocol: TCP
    targetPort: 8080
    nodePort: 30000
    port: 80
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress-file
  namespace: devops
  annotations:
    kubernetes.io/ingress.class: nginx
spec:
  rules:
  - host: pkgs.my.domain.com
    http:
      paths:
      - path: /feed/public
        pathType: Prefix
        backend:
          service:
            name: mitm-proxy-gw
            port: 80
```