# Securing incoming HTTP requests thru any OAuth provider

You may have needed to secure anonymous endpoints in your Kubernetes cluster and make sure that only requests that came from a trusted location are allowed to reach services hosted in Kubernetes.

`auth_request` is an [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/) functionality that allows forwarding requests to a given identity provider before effectively forwarding them to a Kubernetes service.


The `auth-url` can be any URL that validates a token. If it responds `200 (OK)`, the request will be proxied to the Kubernetes service.

[Ingress File](ingress.yml)

### Examples

#### 1. GitHub

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress-file
  namespace: devops
  annotations:
    kubernetes.io/ingress.class: nginx
    # securing the incomming requests againts a custom indentity provider
    # the Authorization header (token) will be forwared to the an URL
    # if the response status is 200 then the NGINX controller will proxy_pass the request
    nginx.ingress.kubernetes.io/auth-url: >
        'https://api.github.com/user'
spec:
  rules:
  - host: public.cluster.domain
    http:
      paths:
      - path: /anonymous/internal/url
        pathType: Prefix
        backend:
          service:
            name: internal-service
            port:
              number: 80
```

#### 2. Bitbucket

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress-file
  namespace: devops
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/auth-url: >
        'https://api.bitbucket.com/user'
spec:
(...)
```

#### 3. Azure

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress-file
  namespace: devops
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/auth-url: >
        'https://graph.microsoft.com/v1.0/me'
spec:
(...)
```