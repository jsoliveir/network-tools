# Securing http requests thru any oauth provider

You may need to allow public request to your kubernetes cluster and make sure that only requests came from a trusted location are allowed to reach an http endpoint hosted in kubernetes 

By using the NGINX Ingress Controller Kubernetes you can take the advantage of the `auth_request` functionality and authorize the request using a custom identity provider.

[Installing the NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/)

The incomming requests to the NGINX ingress controller and all HTTP headers `(Authorization headers)` will be forwared to a given auth endpoint

If the target auth endpoint responds `200 (OK)` then the request will be proxied to the kubernetes service specified, otherwise a `401` will be replied back to the requester.

[Ingress File](oauth-validation-ingress.yml)


### Examples

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